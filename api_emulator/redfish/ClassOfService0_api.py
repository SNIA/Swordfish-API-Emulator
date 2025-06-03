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

# Resource implementation for - /redfish/v1/StorageServices/{StorageServiceId}/ClassesOfService/{ClassOfServiceId}
# Program name - ClassOfService0_api.py

import g
import json, os
import traceback
import logging, random, requests, string, jwt

from flask import Flask, request, session
from flask_restful import Resource
from .constants import *
from api_emulator.utils import check_authentication, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection, send_event

config = {}

members = []
member_ids = []
INTERNAL_ERROR = 500

# ClassOfService0 Collection API
class ClassOfService0CollectionAPI(Resource):
    def __init__(self, **kwargs):
        logging.info('ClassOfService0 Collection init called')
        self.root = PATHS['Root']
        self.auth = kwargs['auth']

    # HTTP GET
    def get(self, StorageServiceId):
        logging.info('ClassOfService0 Collection get called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'StorageServices/{0}/ClassesOfService', 'index.json').format(StorageServiceId)
            return get_json_data(path)
        else:
            return msg, code

    # HTTP POST
    def post(self, StorageServiceId):
        logging.info('ClassOfService0 Collection post called')
        return 'POST is not a supported command for ClassOfService0CollectionAPI', 405

    # HTTP PUT
    def put(self, StorageServiceId):
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
        logging.info('ClassOfService0 Collection put called')
        return 'PUT is not a supported command for ClassOfService0CollectionAPI', 405

    # HTTP PATCH
    def patch(self, StorageServiceId):
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
        logging.info('ClassOfService0 Collection patch called')
        return 'PATCH is not a supported command for ClassOfService0CollectionAPI', 405

    # HTTP DELETE
    def delete(self, StorageServiceId):
        logging.info('ClassOfService0 Collection delete called')
        return 'DELETE is not a supported command for ClassOfService0CollectionAPI', 405


# ClassOfService0 API
class ClassOfService0API(Resource):
    def __init__(self, **kwargs):
        logging.info('ClassOfService0 init called')
        self.root = PATHS['Root']
        self.auth = kwargs['auth']

    # HTTP GET
    def get(self, StorageServiceId, ClassOfServiceId):
        logging.info('ClassOfService0 get called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'StorageServices/{0}/ClassesOfService/{1}', 'index.json').format(StorageServiceId, ClassOfServiceId)
            return get_json_data (path)
        else:
            return msg, code

    # HTTP POST
    def post(self, StorageServiceId, ClassOfServiceId):
        logging.info('ClassOfService0 post called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'StorageServices/{0}/ClassesOfService/{1}').format(StorageServiceId, ClassOfServiceId)
            redfish_path = create_path('/redfish/v1/', 'StorageServices/{0}/ClassesOfService/{1}').format(StorageServiceId, ClassOfServiceId)
            collection_path = create_path(self.root, 'StorageServices/{0}/ClassesOfService', 'index.json').format(StorageServiceId)
            if not os.path.exists(collection_path):
                # Not calling collection POST since not supported
                pass
            if ClassOfServiceId in members:
                resp = 404
                return resp
            try:
                global config
                wildcards = {'StorageServiceId':StorageServiceId, 'ClassOfServiceId':ClassOfServiceId, 'rb':g.rest_base}
                config=get_json_data(path) if os.path.exists(path) else {}
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
            logging.info('ClassOfService0API POST exit')
            return resp
        else:
            return msg, code

    # HTTP PUT
    def put(self, StorageServiceId, ClassOfServiceId):
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
        logging.info('ClassOfService0 put called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'StorageServices/{0}/ClassesOfService/{1}', 'index.json').format(StorageServiceId, ClassOfServiceId)
            redfish_path = create_path('/redfish/v1/', 'StorageServices/{0}/ClassesOfService/{1}', 'index.json').format(StorageServiceId, ClassOfServiceId)
            old_data = get_json_data(path)
            put_object(path)
            new_data = get_json_data(path)
            if old_data.get('Status') != new_data.get('Status'):
            return self.get(ClassOfServiceId)
        else:
            return msg, code

    # HTTP PATCH
    def patch(self, StorageServiceId, ClassOfServiceId):
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
        logging.info('ClassOfService0 patch called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'StorageServices/{0}/ClassesOfService/{1}', 'index.json').format(StorageServiceId, ClassOfServiceId)
            redfish_path = create_path('/redfish/v1/', 'StorageServices/{0}/ClassesOfService/{1}', 'index.json').format(StorageServiceId, ClassOfServiceId)
            old_data = get_json_data(path)
            patch_object(path)
            new_data = get_json_data(path)
            if old_data.get('Status') != new_data.get('Status'):
            return self.get(ClassOfServiceId)
        else:
            return msg, code

    # HTTP DELETE
    def delete(self, StorageServiceId, ClassOfServiceId):
        logging.info('ClassOfService0 delete called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'StorageServices/{0}/ClassesOfService/{1}').format(StorageServiceId, ClassOfServiceId)
            redfish_path = create_path('/redfish/v1/', 'StorageServices/{0}/ClassesOfService/{1}').format(StorageServiceId, ClassOfServiceId)
            base_path = create_path(self.root, 'StorageServices/{0}/ClassesOfService').format(StorageServiceId)
            obj = get_json_data(path)
            send_event(
                "ResourceRemoved",
                "ResourceEvent.1.4.2.ResourceRemoved",
                "The resource was removed successfully.",
                "OK",
                redfish_path
            )
            delete_object(path, base_path)
            return '', 204
        else:
            return msg, code


