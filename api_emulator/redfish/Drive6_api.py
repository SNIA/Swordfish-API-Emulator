#
# Copyright (c) 2017-2024, The Storage Networking Industry Association.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# Neither the name of The Storage Networking Industry Association (SNIA) nor
# the names of its contributors may be used to endorse or promote products
# derived from this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
#  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
#  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
#  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
#  THE POSSIBILITY OF SUCH DAMAGE.

# Resource implementation for - /redfish/v1/ResourceBlocks/{ResourceBlockId}/Drives/{DriveId}
# Program name - Drive6_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import check_authentication, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, create_collection, send_event
from .templates.Drive6 import get_Drive6_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# Drive6 Collection API
class Drive6CollectionAPI(Resource):
    def __init__(self, **kwargs):
        logging.info('Drive6 Collection init called')
        self.root = PATHS['Root']
        self.auth = kwargs['auth']

    # HTTP GET
    def get(self, ResourceBlockId):
        logging.info('Drive6 Collection get called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'ResourceBlocks/{0}/Drives', 'index.json').format(ResourceBlockId)
            return get_json_data(path)
        else:
            return msg, code

    # HTTP POST Collection
    def post(self, ResourceBlockId):
        logging.info('Drive6 Collection post called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            if request.data:
                config = json.loads(request.data)
                if "@odata.type" in config:
                    if "Collection" in config["@odata.type"]:
                        return "Invalid data in POST body", 400

            if ResourceBlockId in members:
                resp = 404
                return resp
            path = create_path(self.root, 'ResourceBlocks/{0}/Drives').format(ResourceBlockId)
            redfish_path = create_path('/redfish/v1/', 'ResourceBlocks/{0}/Drives').format(ResourceBlockId)
            parent_path = os.path.dirname(path)
            if not os.path.exists(path):
                os.mkdir(path)
                create_collection (path, 'Drive', parent_path)

            res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
            if request.data:
                config = json.loads(request.data)
                if "@odata.id" in config:
                    return Drive6API.post(self, ResourceBlockId, os.path.basename(config['@odata.id']))
                else:
                    return Drive6API.post(self, ResourceBlockId, str(res))
            else:
                return Drive6API.post(self, ResourceBlockId, str(res))
        else:
            return msg, code

# Drive6 API
class Drive6API(Resource):
    def __init__(self, **kwargs):
        logging.info('Drive6 init called')
        self.root = PATHS['Root']
        self.auth = kwargs['auth']

    # HTTP GET
    def get(self, ResourceBlockId, DriveId):
        logging.info('Drive6 get called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'ResourceBlocks/{0}/Drives/{1}', 'index.json').format(ResourceBlockId, DriveId)
            return get_json_data (path)
        else:
            return msg, code

    # HTTP POST
    # - Create the resource (since URI variables are available)
    # - Update the members and members.id lists
    # - Attach the APIs of subordinate resources (do this only once)
    # - Finally, create an instance of the subordinate resources
    def post(self, ResourceBlockId, DriveId):
        logging.info('Drive6 post called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'ResourceBlocks/{0}/Drives/{1}').format(ResourceBlockId, DriveId)
            redfish_path = create_path('/redfish/v1/', 'ResourceBlocks/{0}/Drives/{1}').format(ResourceBlockId, DriveId)
            collection_path = create_path(self.root, 'ResourceBlocks/{0}/Drives', 'index.json').format(ResourceBlockId)

            # Check if collection exists:
            if not os.path.exists(collection_path):
                Drive6CollectionAPI.post(self, ResourceBlockId)

            if DriveId in members:
                resp = 404
                return resp
            try:
                global config
                wildcards = {'ResourceBlockId':ResourceBlockId, 'DriveId':DriveId, 'rb':g.rest_base}
                config=get_Drive6_instance(wildcards)
                config = create_and_patch_object (config, members, member_ids, path, collection_path)
                resp = config, 200
                send_event(
                    "ResourceCreated",
                    "ResourceEvent.1.4.2.ResourceCreated",
                    "The resource was created successfully.",
                    "OK",
                    path,
                    None
                )

            except Exception:
                traceback.print_exc()
                resp = INTERNAL_ERROR
            logging.info('Drive6API POST exit')
            return resp
        else:
            return msg, code

    # HTTP PUT
    def put(self, ResourceBlockId, DriveId):
        # Read old version and compare with new data for event logic
        old_version = None
        try:
            with open(path, 'r') as data_json:
                old_version = json.load(data_json)
        except Exception:
            old_version = {}
        health_changed_to = None
        state_changed = False
        new_state = None
        if request.data:
            request_data = json.loads(request.data)
            old_health = old_version.get('State', {}).get('Health')
            new_health = request_data.get('State', {}).get('Health', old_health)
            if old_health != new_health:
                health_changed_to = new_health
            old_status = old_version.get('State', {}).get('Status')
            new_status = request_data.get('State', {}).get('Status', old_status)
            if old_status != new_status:
                state_changed = True
                new_state = new_status
        send_event(
            "ResourceChanged",
            "ResourceEvent.1.4.2ResourceChanged",
            "One or more resource properties have changed.",
            "OK",
            redfish_path
        )
        if health_changed_to == "OK":
            send_event(
                "ResourceStatusChangedOK",
                "ResourceEvent.1.4.2.ResourceStatusChangedOK",
                f"The health of resource '{redfish_path}' has changed to OK.",
                "OK",
                redfish_path
            )
        if health_changed_to == "Critical":
            send_event(
                "ResourceStatusChangedCritical",
                "ResourceEvent.1.4.2.ResourceStatusChangedCritical",
                f"The health of resource '{redfish_path}' has changed to Critical.",
                "Critical",
                redfish_path
            )
        if health_changed_to == "Warning":
            send_event(
                "ResourceStatusChangedWarning",
                "ResourceEvent.1.4.2.ResourceStatusChangedCritical",
                f"The health of resource '{redfish_path}' has changed to Warning.",
                "Warning",
                redfish_path
            )
        if state_changed:
            send_event(
                "ResourceStateChanged",
                "ResourceEvent.1.4.2.ResourceStateChanged",
                f"The state of resource '{redfish_path}' has changed to {new_state}.",
                "OK",
                redfish_path
            )
        logging.info('Drive6 put called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'ResourceBlocks/{0}/Drives/{1}', 'index.json').format(ResourceBlockId, DriveId)
            redfish_path = create_path('/redfish/v1/', 'ResourceBlocks/{0}/Drives/{1}', 'index.json').format(ResourceBlockId, DriveId)
            put_object(path)
            return self.get(ResourceBlockId, DriveId)
        else:
            return msg, code

    # HTTP PATCH
    def patch(self, ResourceBlockId, DriveId):
        # Read old version and compare with new data for event logic
        old_version = None
        try:
            with open(path, 'r') as data_json:
                old_version = json.load(data_json)
        except Exception:
            old_version = {}
        health_changed_to = None
        state_changed = False
        new_state = None
        if request.data:
            request_data = json.loads(request.data)
            old_health = old_version.get('State', {}).get('Health')
            new_health = request_data.get('State', {}).get('Health', old_health)
            if old_health != new_health:
                health_changed_to = new_health
            old_status = old_version.get('State', {}).get('Status')
            new_status = request_data.get('State', {}).get('Status', old_status)
            if old_status != new_status:
                state_changed = True
                new_state = new_status
        send_event(
            "ResourceChanged",
            "ResourceEvent.1.4.2ResourceChanged",
            "One or more resource properties have changed.",
            "OK",
            redfish_path
        )
        if health_changed_to == "OK":
            send_event(
                "ResourceStatusChangedOK",
                "ResourceEvent.1.4.2.ResourceStatusChangedOK",
                f"The health of resource '{redfish_path}' has changed to OK.",
                "OK",
                redfish_path
            )
        if health_changed_to == "Critical":
            send_event(
                "ResourceStatusChangedCritical",
                "ResourceEvent.1.4.2.ResourceStatusChangedCritical",
                f"The health of resource '{redfish_path}' has changed to Critical.",
                "Critical",
                redfish_path
            )
        if health_changed_to == "Warning":
            send_event(
                "ResourceStatusChangedWarning",
                "ResourceEvent.1.4.2.ResourceStatusChangedCritical",
                f"The health of resource '{redfish_path}' has changed to Warning.",
                "Warning",
                redfish_path
            )
        if state_changed:
            send_event(
                "ResourceStateChanged",
                "ResourceEvent.1.4.2.ResourceStateChanged",
                f"The state of resource '{redfish_path}' has changed to {new_state}.",
                "OK",
                redfish_path
            )
        logging.info('Drive6 patch called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'ResourceBlocks/{0}/Drives/{1}', 'index.json').format(ResourceBlockId, DriveId)
            redfish_path = create_path('/redfish/v1/', 'ResourceBlocks/{0}/Drives/{1}', 'index.json').format(ResourceBlockId, DriveId)
            patch_object(path)
            return self.get(ResourceBlockId, DriveId)
        else:
            return msg, code

    # HTTP DELETE
    def delete(self, ResourceBlockId, DriveId):
        logging.info('Drive6 delete called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'ResourceBlocks/{0}/Drives/{1}').format(ResourceBlockId, DriveId)
            redfish_path = create_path('/redfish/v1/', 'ResourceBlocks/{0}/Drives/{1}').format(ResourceBlockId, DriveId)
            base_path = create_path(self.root, 'ResourceBlocks/{0}/Drives').format(ResourceBlockId)
            send_event(
                "ResourceRemoved",
                "ResourceEvent.1.4.2.ResourceRemoved",
                "The resource was removed successfully.",
                "OK",
                redfish_path
            )
            return delete_object(path, base_path)
        else:
            return msg, code

