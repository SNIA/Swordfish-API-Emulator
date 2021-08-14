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

# fabric_api.py

import json, os
import shutil

import traceback
import logging
import g
import urllib3

from flask import jsonify, request
from flask_restful import Resource

from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .constants import *
from .templates.fabric import get_Fabric_instance

from api_emulator.redfish.f_switches_api import *
from api_emulator.redfish.f_switch_ports_api import *

from api_emulator.redfish.f_connections_api import *
from api_emulator.redfish.f_zones_api import *

from api_emulator.redfish.f_endpoints_api import *
from api_emulator.redfish.f_endpointgroups_api import *

members =[]
member_ids = []
config = {}
INTERNAL_ERROR = 500

# FabricAPI
class FabricAPI(Resource):
    def __init__(self, **kwargs):
        logging.info('FabricAPI init called')
        self.root = PATHS['Root']
        self.fabrics = PATHS['Fabrics']['path']

    # HTTP GET
    def get(self, fabric):
        path = create_path(self.root, self.fabrics, fabric, 'index.json')
        return get_json_data (path)

    # HTTP POST
    # - Create the resource (since URI variables are available)
    # - Update the members and members.id lists
    # - Attach the APIs of subordinate resources (do this only once)
    # - Finally, create an instance of the subordinate resources
    def post(self, fabric):
        logging.info('FabricAPI POST called')
        path = create_path(self.root,  self.fabrics, fabric)
        collection_path = os.path.join(self.root, self.fabrics, 'index.json')
        # Check if collection exists:
        if not os.path.exists(collection_path):
            FabricCollectionAPI.post (self)

        if fabric in members:
            resp = 404
            return resp
        try:
            global config
            wildcards = {'f_id':fabric, 'rb': g.rest_base}
            config=get_Fabric_instance(wildcards)

            config = create_and_patch_object (config, members, member_ids, path, collection_path)

            #Add default placeholder collections to instance.
            FabricsEndpointsCollectionAPI.post (self, fabric)
            FabricsConnectionsCollectionAPI.post (self, fabric)
            FabricsSwitchesCollectionAPI.post (self, fabric)
            FabricsZonesCollectionAPI.post (self, fabric)

            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        logging.info('FabricAPI POST exit')
        return resp

    # HTTP PUT
    def put(self, fabric):
        path = create_path(self.root, self.fabrics, fabric, 'index.json')
        put_object(path)
        return self.get(fabric)

	# HTTP PATCH
    def patch(self, fabric):
        #Set path to object, then call patch_object:
        path = create_path(self.root, self.fabrics, fabric, 'index.json')
        patch_object(path)
        return self.get(fabric)

    # HTTP DELETE
    def delete(self, fabric):
        #Set path to object, then call delete_object:
        path = create_path(self.root, self.fabrics, fabric)
        base_path = create_path(self.root, self.fabrics)
        return delete_object(path, base_path)


# Fabric Collection API
class FabricCollectionAPI(Resource):

    def __init__(self):
        self.root = PATHS['Root']
        self.fabrics = PATHS['Fabrics']['path']

    def get(self):
        path = os.path.join(self.root, self.fabrics, 'index.json')
        return get_json_data (path)

    def verify(self, config):
        # TODO: Implement a method to verify that the POST body is valid
        return True,{}

    # HTTP POST Collection
    def post(self):
        self.root = PATHS['Root']
        self.fabrics = PATHS['Fabrics']['path']

        path = create_path(self.root, self.fabrics)
        return create_collection (path, 'Fabric')

    # HTTP PUT
    def put(self):
        path = os.path.join(self.root, self.fabrics, 'index.json')
        put_object(path)
        return self.get(self.root)

    # HTTP DELETE
    def delete(self):
        #Set path to object, then call delete_object:
        path = create_path(self.root, self.fabrics)
        base_path = create_path(self.root)
        return delete_collection(path, base_path)
