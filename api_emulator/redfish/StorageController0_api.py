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

# Resource implementation for - /redfish/v1/Storage/{StorageId}/Controllers/{ControllerId}
# Program name - StorageController0_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import check_authentication, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, create_collection, send_event
from .templates.StorageController0 import get_StorageController0_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# StorageController0 Collection API
class StorageController0CollectionAPI(Resource):
    def __init__(self, **kwargs):
        logging.info('StorageController0 Collection init called')
        self.root = PATHS['Root']
        self.auth = kwargs['auth']

    # HTTP GET
    def get(self, StorageId):
        logging.info('StorageController0 Collection get called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = os.path.join(self.root, 'Storage/{0}/Controllers', 'index.json').format(StorageId)
            return get_json_data(path)
        else:
            return msg, code

    # HTTP POST Collection
    def post(self, StorageId):
        logging.info('StorageController0 Collection post called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            if request.data:
                config = json.loads(request.data)
                if "@odata.type" in config:
                    if "Collection" in config["@odata.type"]:
                        return "Invalid data in POST body", 400

            if StorageId in members:
                resp = 404
                return resp
            path = create_path(self.root, 'Storage/{0}/Controllers').format(StorageId)
            parent_path = os.path.dirname(path)
            if not os.path.exists(path):
                os.mkdir(path)
                create_collection (path, 'StorageController', parent_path)

            res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
            if request.data:
                config = json.loads(request.data)
                if "@odata.id" in config:
                    return StorageController0API.post(self, StorageId, os.path.basename(config['@odata.id']))
                else:
                    return StorageController0API.post(self, StorageId, str(res))
            else:
                return StorageController0API.post(self, StorageId, str(res))
        else:
            return msg, code

# StorageController0 API
class StorageController0API(Resource):
    def __init__(self, **kwargs):
        logging.info('StorageController0 init called')
        self.root = PATHS['Root']
        self.auth = kwargs['auth']

    # HTTP GET
    def get(self, StorageId, ControllerId):
        logging.info('StorageController0 get called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'Storage/{0}/Controllers/{1}', 'index.json').format(StorageId, ControllerId)
            return get_json_data (path)
        else:
            return msg, code

    # HTTP POST
    def post(self, StorageId, ControllerId):
        logging.info('StorageController0 post called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'Storage/{0}/Controllers/{1}').format(StorageId, ControllerId)
            collection_path = os.path.join(self.root, 'Storage/{0}/Controllers', 'index.json').format(StorageId)

            # Check if collection exists:
            if not os.path.exists(collection_path):
                StorageController0CollectionAPI.post(self, StorageId)

            if ControllerId in members:
                resp = 404
                return resp
            try:
                global config
                wildcards = {'StorageId':StorageId, 'ControllerId':ControllerId, 'rb':g.rest_base}
                config = get_StorageController0_instance(wildcards)
                config = create_and_patch_object(config, members, member_ids, path, collection_path)
                resp = config, 200
                resource_odata_id = config.get('@odata.id', f"/redfish/v1/Storage/{StorageId}/Controllers/{ControllerId}")
                send_event(
                    "ResourceCreated",
                    "ResourceEvent.1.4.2.ResourceCreated",
                    "The resource was created successfully.",
                    "OK",
                    path,
                    config
                )
            except Exception:
                traceback.print_exc()
                resp = INTERNAL_ERROR
            logging.info('StorageController0API POST exit')
            return resp
        else:
            return msg, code

    # HTTP PUT
    def put(self, StorageId, ControllerId):
        logging.info('StorageController0 put called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'Storage/{0}/Controllers/{1}', 'index.json').format(StorageId, ControllerId)
            try:
                with open(path, 'r') as f:
                    old_data = json.load(f)
            except Exception:
                old_data = {}
            put_object(path)
            new_data = get_json_data(path)
            resource_odata_id = new_data.get('@odata.id', f"/redfish/v1/Storage/{StorageId}/Controllers/{ControllerId}")
            send_event(
                "ResourceChanged",
                "ResourceEvent.1.0.ResourceChanged",
                "One or more resource properties have changed.",
                "OK",
                resource_odata_id
            )
            old_health = old_data.get('Status', {}).get('Health') if old_data else None
            new_health = new_data.get('Status', {}).get('Health') if new_data else None
            if new_health and new_health != old_health:
                if new_health == "OK":
                    send_event(
                        "ResourceStatusChangedOK",
                        "ResourceEvent.1.0.ResourceStatusChangedOK",
                        f"The health of resource '{resource_odata_id}' has changed to {new_health}.",
                        "OK",
                        resource_odata_id,
                        extra={"ResourceName": resource_odata_id, "NewHealth": new_health}
                    )
                elif new_health == "Warning":
                    send_event(
                        "ResourceStatusChangedWarning",
                        "ResourceEvent.1.0.ResourceStatusChangedWarning",
                        f"The health of resource '{resource_odata_id}' has changed to {new_health}.",
                        "Warning",
                        resource_odata_id,
                        extra={"ResourceName": resource_odata_id, "NewHealth": new_health}
                    )
                elif new_health == "Critical":
                    send_event(
                        "ResourceStatusChangedCritical",
                        "ResourceEvent.1.0.ResourceStatusChangedCritical",
                        f"The health of resource '{resource_odata_id}' has changed to {new_health}.",
                        "Critical",
                        resource_odata_id,
                        extra={"ResourceName": resource_odata_id, "NewHealth": new_health}
                    )
            return self.get(StorageId, ControllerId)
        else:
            return msg, code

    # HTTP PATCH
    def patch(self, StorageId, ControllerId):
        logging.info('StorageController0 patch called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'Storage/{0}/Controllers/{1}', 'index.json').format(StorageId, ControllerId)
            try:
                with open(path, 'r') as f:
                    old_data = json.load(f)
            except Exception:
                old_data = {}
            patch_object(path)
            new_data = get_json_data(path)
            resource_odata_id = new_data.get('@odata.id', f"/redfish/v1/Storage/{StorageId}/Controllers/{ControllerId}")
            send_event(
                "ResourceChanged",
                "ResourceEvent.1.0.ResourceChanged",
                "One or more resource properties have changed.",
                "OK",
                resource_odata_id
            )
            old_health = old_data.get('Status', {}).get('Health') if old_data else None
            new_health = new_data.get('Status', {}).get('Health') if new_data else None
            if new_health and new_health != old_health:
                if new_health == "OK":
                    send_event(
                        "ResourceStatusChangedOK",
                        "ResourceEvent.1.0.ResourceStatusChangedOK",
                        f"The health of resource '{resource_odata_id}' has changed to {new_health}.",
                        "OK",
                        resource_odata_id,
                        extra={"ResourceName": resource_odata_id, "NewHealth": new_health}
                    )
                elif new_health == "Warning":
                    send_event(
                        "ResourceStatusChangedWarning",
                        "ResourceEvent.1.0.ResourceStatusChangedWarning",
                        f"The health of resource '{resource_odata_id}' has changed to {new_health}.",
                        "Warning",
                        resource_odata_id,
                        extra={"ResourceName": resource_odata_id, "NewHealth": new_health}
                    )
                elif new_health == "Critical":
                    send_event(
                        "ResourceStatusChangedCritical",
                        "ResourceEvent.1.0.ResourceStatusChangedCritical",
                        f"The health of resource '{resource_odata_id}' has changed to {new_health}.",
                        "Critical",
                        resource_odata_id,
                        extra={"ResourceName": resource_odata_id, "NewHealth": new_health}
                    )
            return self.get(StorageId, ControllerId)
        else:
            return msg, code

    # HTTP DELETE
    def delete(self, StorageId, ControllerId):
        logging.info('StorageController0 delete called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'Storage/{0}/Controllers/{1}').format(StorageId, ControllerId)
            base_path = create_path(self.root, 'Storage/{0}/Controllers').format(StorageId)
            resp = delete_object(path, base_path)
            resource_odata_id = f"/redfish/v1/Storage/{StorageId}/Controllers/{ControllerId}"
            send_event(
                "ResourceRemoved",
                "ResourceEvent.1.0.ResourceRemoved",
                "The resource was removed successfully.",
                "OK",
                resource_odata_id
            )
            return resp
        else:
            return msg, code

