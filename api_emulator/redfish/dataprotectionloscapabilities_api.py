#
# Copyright (c) 2017-2021, The Storage Networking Industry Association.
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
#

#dataprotectionloscapabilities_api.py
import json, os
import traceback
import logging
import g
import urllib3

from flask import jsonify, request
from flask_restful import Resource
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .constants import *
from .templates.dataprotectionloscapabilities import get_DataProtectionLoSCapabilities_instance

members =[]
member_ids = []
foo = False
config = {}
INTERNAL_ERROR = 500


# DataProtectionLoSCapabilities API
class DataProtectionLoSCapabilitiesAPI(Resource):
    def __init__(self, **kwargs):
        logging.info('DataProtectionLoSCapabilitiesAPI init called')
        self.root = PATHS['Root']
        self.storage_services = PATHS['StorageServices']['path']
        self.data_protection_los_capabilities = PATHS['StorageServices']['data_protection_los_capabilities']

    # HTTP GET
    def get(self, storage_service):
        path = os.path.join(self.root, self.storage_services, storage_service, self.data_protection_los_capabilities, 'index.json')
        return get_json_data (path)

	# HTTP PATCH
    def patch(self, storage_service):
        path = os.path.join(self.root, self.storage_services, storage_service, self.data_protection_los_capabilities, 'index.json')

        try:
            # Read json from file.
            with open(path, 'r') as data_protection_los_capabilities_json:
                data = json.load(data_protection_los_capabilities_json)
                data_protection_los_capabilities_json.close()

            request_data = json.loads(request.data)

            if request_data:
                # Update the keys of payload in json file.
                for key, value in request_data.items():
                    if key in data and data[key]:
                        data[key] = value

            # Write the updated json to file.
            with open(path, 'w') as f:
                json.dump(data, f)
                f.close()

        except Exception as e:
            return {"error": "Unable read file because of following error::{}".format(e)}, 500

        json_data = self.get(storage_service)
        return json_data






class CreateDataProtectionLoSCapabilities (Resource):
    def __init__(self):
        self.root = PATHS['Root']
        self.storage_services = PATHS['StorageServices']['path']
        self.data_protection_los_capabilities = PATHS['StorageServices']['data_protection_los_capabilities']

    # Attach APIs for subordinate resource(s). Attach the APIs for a resource collection and its singletons
    def put(self,storage_service):
        logging.info('CreateDataProtectionLoSCapabilities put started.')
        global config
        try:

            path = create_path(self.root, self.storage_services, storage_service, self.data_protection_los_capabilities)
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                print ("ihuh")
            wildcards = {'s_id':storage_service,'rb': g.rest_base}

            config=get_DataProtectionLoSCapabilities_instance(wildcards)

            with open(os.path.join(path, "index.json"), "w") as fd:
                fd.write(json.dumps(config, indent=4, sort_keys=True))

            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        logging.info('CreateDataProtectionLoSCapabilities put exit.')
        return resp
