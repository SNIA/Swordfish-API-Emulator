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

# Resource implementation for - /redfish/v1/ResourceBlocks/{ResourceBlockId}/Processors/{ProcessorId}/Ports/{PortId}
# Program name - Port21_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import check_authentication, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, create_collection, send_event
from .templates.Port21 import get_Port21_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# Port21 Collection API
class Port21CollectionAPI(Resource):
    def __init__(self, **kwargs):
        logging.info('Port21 Collection init called')
        self.root = PATHS['Root']
        self.auth = kwargs['auth']

    # HTTP GET
    def get(self, ResourceBlockId, ProcessorId):
        logging.info('Port21 Collection get called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'ResourceBlocks/{0}/Processors/{1}/Ports', 'index.json').format(ResourceBlockId, ProcessorId)
            return get_json_data(path)
        else:
            return msg, code

    # HTTP POST Collection
    def post(self, ResourceBlockId, ProcessorId):
        logging.info('Port21 Collection post called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            if request.data:
                config = json.loads(request.data)
                if "@odata.type" in config:
                    if "Collection" in config["@odata.type"]:
                        return "Invalid data in POST body", 400

            if ProcessorId in members:
                resp = 404
                return resp
            path = create_path(self.root, 'ResourceBlocks/{0}/Processors/{1}/Ports').format(ResourceBlockId, ProcessorId)
            redfish_path = create_path('/redfish/v1/', 'ResourceBlocks/{0}/Processors/{1}/Ports').format(ResourceBlockId, ProcessorId)
            parent_path = os.path.dirname(path)
            if not os.path.exists(path):
                os.mkdir(path)
                create_collection (path, 'Port', parent_path)

            res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
            if request.data:
                config = json.loads(request.data)
                if "@odata.id" in config:
                    return Port21API.post(self, ResourceBlockId, ProcessorId, os.path.basename(config['@odata.id']))
                else:
                    return Port21API.post(self, ResourceBlockId, ProcessorId, str(res))
            else:
                return Port21API.post(self, ResourceBlockId, ProcessorId, str(res))
        else:
            return msg, code

# Port21 API
class Port21API(Resource):
    def __init__(self, **kwargs):
        logging.info('Port21 init called')
        self.root = PATHS['Root']
        self.auth = kwargs['auth']

    # HTTP GET
    def get(self, ResourceBlockId, ProcessorId, PortId):
        logging.info('Port21 get called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'ResourceBlocks/{0}/Processors/{1}/Ports/{2}', 'index.json').format(ResourceBlockId, ProcessorId, PortId)
            return get_json_data (path)
        else:
            return msg, code

    # HTTP POST
    # - Create the resource (since URI variables are available)
    # - Update the members and members.id lists
    # - Attach the APIs of subordinate resources (do this only once)
    # - Finally, create an instance of the subordinate resources
    def post(self, ResourceBlockId, ProcessorId, PortId):
        logging.info('Port21 post called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'ResourceBlocks/{0}/Processors/{1}/Ports/{2}').format(ResourceBlockId, ProcessorId, PortId)
            redfish_path = create_path('/redfish/v1/', 'ResourceBlocks/{0}/Processors/{1}/Ports/{2}').format(ResourceBlockId, ProcessorId, PortId)
            collection_path = create_path(self.root, 'ResourceBlocks/{0}/Processors/{1}/Ports', 'index.json').format(ResourceBlockId, ProcessorId)

            # Check if collection exists:
            if not os.path.exists(collection_path):
                Port21CollectionAPI.post(self, ResourceBlockId, ProcessorId)

            if PortId in members:
                resp = 404
                return resp
            try:
                global config
                wildcards = {'ResourceBlockId':ResourceBlockId, 'ProcessorId':ProcessorId, 'PortId':PortId, 'rb':g.rest_base}
                config=get_Port21_instance(wildcards)
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
            logging.info('Port21API POST exit')
            return resp
        else:
            return msg, code

    # HTTP PUT
    def put(self, ResourceBlockId, ProcessorId, PortId):
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
        logging.info('Port21 put called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'ResourceBlocks/{0}/Processors/{1}/Ports/{2}', 'index.json').format(ResourceBlockId, ProcessorId, PortId)
            redfish_path = create_path('/redfish/v1/', 'ResourceBlocks/{0}/Processors/{1}/Ports/{2}', 'index.json').format(ResourceBlockId, ProcessorId, PortId)
            put_object(path)
            return self.get(ResourceBlockId, ProcessorId, PortId)
        else:
            return msg, code

    # HTTP PATCH
    def patch(self, ResourceBlockId, ProcessorId, PortId):
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
        logging.info('Port21 patch called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'ResourceBlocks/{0}/Processors/{1}/Ports/{2}', 'index.json').format(ResourceBlockId, ProcessorId, PortId)
            redfish_path = create_path('/redfish/v1/', 'ResourceBlocks/{0}/Processors/{1}/Ports/{2}', 'index.json').format(ResourceBlockId, ProcessorId, PortId)
            patch_object(path)
            return self.get(ResourceBlockId, ProcessorId, PortId)
        else:
            return msg, code

    # HTTP DELETE
    def delete(self, ResourceBlockId, ProcessorId, PortId):
        logging.info('Port21 delete called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'ResourceBlocks/{0}/Processors/{1}/Ports/{2}').format(ResourceBlockId, ProcessorId, PortId)
            redfish_path = create_path('/redfish/v1/', 'ResourceBlocks/{0}/Processors/{1}/Ports/{2}').format(ResourceBlockId, ProcessorId, PortId)
            base_path = create_path(self.root, 'ResourceBlocks/{0}/Processors/{1}/Ports').format(ResourceBlockId, ProcessorId)
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

