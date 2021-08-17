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

# c_memory_api.py

import json, os
import traceback
import logging
import shutil

import g
import urllib3

from flask import jsonify, request
from flask_restful import Resource
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .constants import *
from .templates.networkadapters import get_NetworkAdapters_instance

members =[]
member_ids = []
config = {}
INTERNAL_ERROR = 500

# NetworkAdaptersAPI API
class NetworkAdaptersAPI(Resource):
    def __init__(self, **kwargs):
        logging.info('NetworkAdaptersAPI init called')
        self.root = PATHS['Root']
        self.chassis = PATHS['Chassis']['path']
        self.network_adapters = PATHS['Chassis']['network_adapter']

    # HTTP GET
    def get(self, chassis, network_adapter):
        path = create_path(self.root, self.chassis, chassis, self.network_adapters, network_adapter, 'index.json')
        return get_json_data (path)

    # HTTP POST
    # - Create the resource (since URI variables are available)
    # - Update the members and members.id lists
    # - Attach the APIs of subordinate resources (do this only once)
    # - Finally, create an instance of the subordiante resources
    def post(self, chassis, network_adapter):
        logging.info('NetworkAdaptersAPI POST called')
        path = create_path(self.root, self.chassis, chassis, self.network_adapters, network_adapter)
        collection_path = os.path.join(self.root, self.chassis, chassis, self.network_adapters, 'index.json')

        # Check if collection exists:
        if not os.path.exists(collection_path):
            NetworkAdaptersCollectionAPI.post (self, chassis)

        if network_adapter in members:
            resp = 404
            return resp
        try:
            global config
            wildcards = {'c_id':chassis, 'n_id': network_adapter,  'rb': g.rest_base}
            config=get_NetworkAdapters_instance(wildcards)
            config = create_and_patch_object (config, members, member_ids, path, collection_path)

            # Create sub-collections:
            resp = config, 200

        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        logging.info('NetworkAdaptersAPI POST exit')
        return resp

	# HTTP PATCH
    def patch(self, chassis, network_adapter):
        path = os.path.join(self.root, self.chassis, chassis, self.network_adapters, network_adapter, 'index.json')
        patch_object(path)
        return self.get(chassis, network_adapter)

    # HTTP PUT
    def put(self, chassis, network_adapter):
        path = os.path.join(self.root, self.chassis, chassis, self.network_adapters, network_adapter, 'index.json')
        put_object(path)
        return self.get(chassis, network_adapter)

    # HTTP DELETE
    def delete(self, chassis, network_adapter):
        #Set path to object, then call delete_object:
        path = create_path(self.root, self.chassis, chassis, self.network_adapters, network_adapter)
        base_path = create_path(self.root, self.chassis, chassis, self.network_adapters)
        return delete_object(path, base_path)


# NetworkAdapters Collection API
class NetworkAdaptersCollectionAPI(Resource):

    def __init__(self):
        self.root = PATHS['Root']
        self.chassis = PATHS['Chassis']['path']
        self.network_adapters = PATHS['Chassis']['network_adapter']

    def get(self, chassis):
        path = os.path.join(self.root, self.chassis, chassis, self.network_adapters, 'index.json')
        return get_json_data (path)

    def verify(self, config):
        # TODO: Implement a method to verify that the POST body is valid
        return True,{}

    # HTTP POST Collection
    def post(self, chassis):
        self.root = PATHS['Root']
        self.chassis = PATHS['Chassis']['path']
        self.network_adapters = PATHS['Chassis']['network_adapter']

        logging.info('NetworkAdaptersCollectionAPI POST called')

        if chassis in members:
            resp = 404
            return resp

        path = create_path(self.root, self.chassis, chassis, self.network_adapters)
        return create_collection (path, 'NetworkAdapter')

    # HTTP PUT
    def put(self, chassis):
        path = os.path.join(self.root, self.chassis, chassis, self.network_adapters, 'index.json')
        put_object(path)
        return self.get(chassis)

    # HTTP DELETE
    def delete(self, chassis):
        #Set path to object, then call delete_object:
        path = create_path(self.root, self.chassis, chassis, self.network_adapters)
        base_path = create_path(self.root, self.chassis, chassis)
        return delete_collection(path, base_path)
