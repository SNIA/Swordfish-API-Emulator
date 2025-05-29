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

# Resource implementation for - /redfish/v1/Storage/{StorageId}/ConsistencyGroups/{ConsistencyGroupId}
# Program name - ConsistencyGroup0_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import check_authentication, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, create_collection, send_event
from .templates.ConsistencyGroup0 import get_ConsistencyGroup0_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# ConsistencyGroup0 Collection API
class ConsistencyGroup0CollectionAPI(Resource):
    def __init__(self, **kwargs):
        logging.info('ConsistencyGroup0 Collection init called')
        self.root = PATHS['Root']
        self.auth = kwargs['auth']

    # HTTP GET
    def get(self, StorageId):
        logging.info('ConsistencyGroup0 Collection get called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = os.path.join(self.root, 'Storage/{0}/ConsistencyGroups', 'index.json').format(StorageId)
            return get_json_data(path)
        else:
            return msg, code

    # HTTP POST Collection
    def post(self, StorageId):
        logging.info('ConsistencyGroup0 Collection post called')
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
            path = create_path(self.root, 'Storage/{0}/ConsistencyGroups').format(StorageId)
            parent_path = os.path.dirname(path)
            if not os.path.exists(path):
                os.mkdir(path)
                create_collection (path, 'ConsistencyGroup', parent_path)

            res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
            if request.data:
                config = json.loads(request.data)
                if "@odata.id" in config:
                    return ConsistencyGroup0API.post(self, StorageId, os.path.basename(config['@odata.id']))
                else:
                    return ConsistencyGroup0API.post(self, StorageId, str(res))
            else:
                return ConsistencyGroup0API.post(self, StorageId, str(res))
        else:
            return msg, code

# ConsistencyGroup0 API
class ConsistencyGroup0API(Resource):
    def __init__(self, **kwargs):
        logging.info('ConsistencyGroup0 init called')
        self.root = PATHS['Root']
        self.auth = kwargs['auth']

    # HTTP GET
    def get(self, StorageId, ConsistencyGroupId):
        logging.info('ConsistencyGroup0 get called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'Storage/{0}/ConsistencyGroups/{1}', 'index.json').format(StorageId, ConsistencyGroupId)
            return get_json_data (path)
        else:
            return msg, code

    # HTTP POST
    def post(self, StorageId, ConsistencyGroupId):
        logging.info('ConsistencyGroup0 post called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'Storage/{0}/ConsistencyGroups/{1}').format(StorageId, ConsistencyGroupId)
            collection_path = os.path.join(self.root, 'Storage/{0}/ConsistencyGroups', 'index.json').format(StorageId)
            if not os.path.exists(collection_path):
                ConsistencyGroup0CollectionAPI.post(self, StorageId)
            if ConsistencyGroupId in members:
                resp = 404
                return resp
            try:
                global config
                wildcards = {'StorageId':StorageId, 'ConsistencyGroupId':ConsistencyGroupId, 'rb':g.rest_base}
                config=get_ConsistencyGroup0_instance(wildcards)
                config = create_and_patch_object (config, members, member_ids, path, collection_path)
                resp = config, 200
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
            logging.info('ConsistencyGroup0API POST exit')
            return resp
        else:
            return msg, code

    # HTTP PUT
    def put(self, StorageId, ConsistencyGroupId):
        logging.info('ConsistencyGroup0 put called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = os.path.join(self.root, 'Storage/{0}/ConsistencyGroups/{1}', 'index.json').format(StorageId, ConsistencyGroupId)
            old_data = get_json_data(path)
            put_object(path)
            new_data = get_json_data(path)
            send_event(
                "ResourceChanged",
                "ResourceChanged",
                f"ConsistencyGroup {ConsistencyGroupId} changed",
                "OK",
                path,
                new_data
            )
            if old_data.get('Status') != new_data.get('Status'):
                send_event(
                    "ResourceStatusChanged",
                    "ResourceStatusChanged",
                    f"ConsistencyGroup {ConsistencyGroupId} status changed",
                    "OK",
                    path,
                    new_data
                )
            return self.get(StorageId, ConsistencyGroupId)
        else:
            return msg, code

    # HTTP PATCH
    def patch(self, StorageId, ConsistencyGroupId):
        logging.info('ConsistencyGroup0 patch called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = os.path.join(self.root, 'Storage/{0}/ConsistencyGroups/{1}', 'index.json').format(StorageId, ConsistencyGroupId)
            old_data = get_json_data(path)
            patch_object(path)
            new_data = get_json_data(path)
            send_event(
                "ResourceChanged",
                "ResourceChanged",
                f"ConsistencyGroup {ConsistencyGroupId} changed",
                "OK",
                path,
                new_data
            )
            if old_data.get('Status') != new_data.get('Status'):
                send_event(
                    "ResourceStatusChanged",
                    "ResourceStatusChanged",
                    f"ConsistencyGroup {ConsistencyGroupId} status changed",
                    "OK",
                    path,
                    new_data
                )
            return self.get(StorageId, ConsistencyGroupId)
        else:
            return msg, code

    # HTTP DELETE
    def delete(self, StorageId, ConsistencyGroupId):
        logging.info('ConsistencyGroup0 delete called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'Storage/{0}/ConsistencyGroups/{1}').format(StorageId, ConsistencyGroupId)
            base_path = create_path(self.root, 'Storage/{0}/ConsistencyGroups').format(StorageId)
            obj = get_json_data(path)
            send_event(
                "ResourceRemoved",
                "ResourceRemoved",
                f"ConsistencyGroup {ConsistencyGroupId} removed",
                "OK",
                path,
                obj
            )
            delete_object(path, base_path)
            return '', 204
        else:
            return msg, code

