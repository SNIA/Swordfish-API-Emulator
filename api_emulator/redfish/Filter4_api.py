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

# Resource implementation for - /redfish/v1/ThermalEquipment/ImmersionUnits/{CoolingUnitId}/Filters/{FilterId}
# Program name - Filter4_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import check_authentication, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, create_collection, send_event
from .templates.Filter4 import get_Filter4_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# Filter4 Collection API
class Filter4CollectionAPI(Resource):
    def __init__(self, **kwargs):
        logging.info('Filter4 Collection init called')
        self.root = PATHS['Root']
        self.auth = kwargs['auth']

    # HTTP GET
    def get(self, CoolingUnitId):
        logging.info('Filter4 Collection get called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'ThermalEquipment/ImmersionUnits/{0}/Filters', 'index.json').format(CoolingUnitId)
            return get_json_data(path)
        else:
            return msg, code

    # HTTP POST Collection
    def post(self, CoolingUnitId):
        logging.info('Filter4 Collection post called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            if request.data:
                config = json.loads(request.data)
                if "@odata.type" in config:
                    if "Collection" in config["@odata.type"]:
                        return "Invalid data in POST body", 400

            if CoolingUnitId in members:
                resp = 404
                return resp
            path = create_path(self.root, 'ThermalEquipment/ImmersionUnits/{0}/Filters').format(CoolingUnitId)
            redfish_path = create_path('/redfish/v1/', 'ThermalEquipment/ImmersionUnits/{0}/Filters').format(CoolingUnitId)
            parent_path = os.path.dirname(path)
            if not os.path.exists(path):
                os.mkdir(path)
                create_collection (path, 'Filter', parent_path)

            res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
            if request.data:
                config = json.loads(request.data)
                if "@odata.id" in config:
                    return Filter4API.post(self, CoolingUnitId, os.path.basename(config['@odata.id']))
                else:
                    return Filter4API.post(self, CoolingUnitId, str(res))
            else:
                return Filter4API.post(self, CoolingUnitId, str(res))
        else:
            return msg, code

# Filter4 API
class Filter4API(Resource):
    def __init__(self, **kwargs):
        logging.info('Filter4 init called')
        self.root = PATHS['Root']
        self.auth = kwargs['auth']

    # HTTP GET
    def get(self, CoolingUnitId, FilterId):
        logging.info('Filter4 get called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'ThermalEquipment/ImmersionUnits/{0}/Filters/{1}', 'index.json').format(CoolingUnitId, FilterId)
            return get_json_data (path)
        else:
            return msg, code

    # HTTP POST
    # - Create the resource (since URI variables are available)
    # - Update the members and members.id lists
    # - Attach the APIs of subordinate resources (do this only once)
    # - Finally, create an instance of the subordinate resources
    def post(self, CoolingUnitId, FilterId):
        logging.info('Filter4 post called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'ThermalEquipment/ImmersionUnits/{0}/Filters/{1}').format(CoolingUnitId, FilterId)
            redfish_path = create_path('/redfish/v1/', 'ThermalEquipment/ImmersionUnits/{0}/Filters/{1}').format(CoolingUnitId, FilterId)
            collection_path = create_path(self.root, 'ThermalEquipment/ImmersionUnits/{0}/Filters', 'index.json').format(CoolingUnitId)

            # Check if collection exists:
            if not os.path.exists(collection_path):
                Filter4CollectionAPI.post(self, CoolingUnitId)

            if FilterId in members:
                resp = 404
                return resp
            try:
                global config
                wildcards = {'CoolingUnitId':CoolingUnitId, 'FilterId':FilterId, 'rb':g.rest_base}
                config=get_Filter4_instance(wildcards)
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
            logging.info('Filter4API POST exit')
            return resp
        else:
            return msg, code

    # HTTP PUT
    def put(self, CoolingUnitId, FilterId):
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
        logging.info('Filter4 put called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'ThermalEquipment/ImmersionUnits/{0}/Filters/{1}', 'index.json').format(CoolingUnitId, FilterId)
            redfish_path = create_path('/redfish/v1/', 'ThermalEquipment/ImmersionUnits/{0}/Filters/{1}', 'index.json').format(CoolingUnitId, FilterId)
            put_object(path)
            return self.get(CoolingUnitId, FilterId)
        else:
            return msg, code

    # HTTP PATCH
    def patch(self, CoolingUnitId, FilterId):
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
        logging.info('Filter4 patch called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'ThermalEquipment/ImmersionUnits/{0}/Filters/{1}', 'index.json').format(CoolingUnitId, FilterId)
            redfish_path = create_path('/redfish/v1/', 'ThermalEquipment/ImmersionUnits/{0}/Filters/{1}', 'index.json').format(CoolingUnitId, FilterId)
            patch_object(path)
            return self.get(CoolingUnitId, FilterId)
        else:
            return msg, code

    # HTTP DELETE
    def delete(self, CoolingUnitId, FilterId):
        logging.info('Filter4 delete called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'ThermalEquipment/ImmersionUnits/{0}/Filters/{1}').format(CoolingUnitId, FilterId)
            redfish_path = create_path('/redfish/v1/', 'ThermalEquipment/ImmersionUnits/{0}/Filters/{1}').format(CoolingUnitId, FilterId)
            base_path = create_path(self.root, 'ThermalEquipment/ImmersionUnits/{0}/Filters').format(CoolingUnitId)
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

