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

#fa_ports_api.py

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
from .templates.fabric_adapter_port import get_FabricAdapterPorts_instance

members =[]
member_ids = []
config = {}
INTERNAL_ERROR = 500

# FabricAdapterPorts API
class FabricAdapterPortsAPI(Resource):
    def __init__(self, **kwargs):
        logging.info('FabricAdapterPortsAPI init called')
        self.root = PATHS['Root']
        self.systems = PATHS['Systems']['path']
        self.fabric_adapters = PATHS['Systems']['fabric_adapters']
        self.fabric_adapter_ports = PATHS['Systems']['fabric_adapter_ports']

    # HTTP GET
    def get(self, system, fabric_adapter, fabric_adapter_port):
        path = create_path(self.root, self.systems, system, self.fabric_adapters, fabric_adapter, self.fabric_adapter_ports, fabric_adapter_port, 'index.json')
        return get_json_data (path)

    # HTTP POST
    # - Create the resource (since URI variables are available)
    # - Update the members and members.id lists
    # - Attach the APIs of subordinate resources (do this only once)
    # - Finally, create an instance of the subordiante resources
    def post(self, system, fabric_adapter, fabric_adapter_port):
        logging.info('FabricAdapterPortsAPI PUT called')
        path = create_path(self.root, self.systems, system, self.fabric_adapters, fabric_adapter, self.fabric_adapter_ports, fabric_adapter_port)
        collection_path = os.path.join(self.root, self.systems, system, self.fabric_adapters, fabric_adapter, self.fabric_adapter_ports, 'index.json')

        # Check if collection exists:
        if not os.path.exists(collection_path):
            FabricAdapterPortsCollectionAPI.post (self, system, fabric_adapter)

        if fabric_adapter in members:
            resp = 404
            return resp
        try:
            global config
            wildcards = {'s_id': system, 'fa_id': fabric_adapter, 'fap_id': fabric_adapter_port, 'rb': g.rest_base}
            config=get_FabricAdapterPorts_instance(wildcards)
            config = create_and_patch_object (config, members, member_ids, path, collection_path)

            #Add default placeholder collections to instance.
            FabricAdapterPortsCollectionAPI.post (self, system, fabric_adapter)
            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        logging.info('FabricAdapterPortsAPI put exit')
        return resp

	# HTTP PATCH
    def patch(self, system, fabric_adapter, fabric_adapter_port):
        path = os.path.join(self.root, self.systems, system, self.fabric_adapters, fabric_adapter, self.fabric_adapter_ports, fabric_adapter_port, 'index.json')
        patch_object(path)
        return self.get(system, fabric_adapter)

	# HTTP PUT
    def put(self, system, fabric_adapter, fabric_adapter_port):
        path = os.path.join(self.root, self.systems, system, self.fabric_adapters, fabric_adapter, self.fabric_adapter_ports, fabric_adapter_port, 'index.json')
        put_object(path)
        return self.get(system, fabric_adapter)

    # HTTP DELETE
    def delete(self, system, fabric_adapter, fabric_adapter_port):
        path = create_path(self.root, self.systems, system, self.fabric_adapters, fabric_adapter, self.fabric_adapter_ports, fabric_adapter_port)
        base_path = create_path(self.root, self.systems, system, self.fabric_adapters, fabric_adapter, self.fabric_adapter_ports)
        return delete_object(path, base_path)


# FabricAdapterPorts Collection API
class FabricAdapterPortsCollectionAPI(Resource):

    def __init__(self):
        self.root = PATHS['Root']
        self.systems = PATHS['Systems']['path']
        self.fabric_adapters = PATHS['Systems']['fabric_adapters']
        self.fabric_adapter_ports = PATHS['Systems']['fabric_adapter_ports']

    def get(self, system, fabric_adapter):
        path = os.path.join(self.root, self.systems, system, self.fabric_adapters, fabric_adapter, self.fabric_adapter_ports, 'index.json')
        return get_json_data (path)

    def verify(self, config):
        # TODO: Implement a method to verify that the POST body is valid
        return True,{}

    # HTTP POST
    # POST should allow adding multiple instances to a collection.
    # For now, this only adds one instance.
    # TODO: 'id' should be obtained from the request data.
    def post(self, system, fabric_adapter):
        logging.info('FabricAdapterPortsCollectionAPI POST called')
        self.root = PATHS['Root']
        self.systems = PATHS['Systems']['path']
        self.fabric_adapters = PATHS['Systems']['fabric_adapters']
        self.fabric_adapter_ports = PATHS['Systems']['fabric_adapter_ports']

        if fabric_adapter in members:
            resp = 404
            return resp
        path = create_path(self.root, self.systems, system, self.fabric_adapters, fabric_adapter, self.fabric_adapter_ports)
        return create_collection (path, 'Port')

    # HTTP PUT
    def put(self, system, fabric_adapter):
        path = os.path.join(self.root, self.systems, system, self.fabric_adapters, fabric_adapter, self.fabric_adapter_ports, 'index.json')
        put_object(path)
        return self.get(system)

    # HTTP DELETE
    def delete(self, system, fabric_adapter):
        #Set path to object, then call delete_object:
        path = create_path(self.root, self.systems, system, self.fabric_adapters, fabric_adapter, self.fabric_adapter_ports)
        base_path = create_path(self.root, self.systems, system, self.fabric_adapters, fabric_adapter)
        return delete_collection(path, base_path)

class CreateFabricAdapterPorts (Resource):
    def __init__(self):
        self.root = PATHS['Root']
        self.systems = PATHS['Systems']['path']
        self.fabric_adapters = PATHS['Systems']['fabric_adapters']
        self.fabric_adapter_ports = PATHS['Systems']['fabric_adapter_ports']

    # Attach APIs for subordinate resource(s). Attach the APIs for a resource collection and its singletons
    def put(self,system, fabric_adapter):
        logging.info('CreateFabricAdapterPorts put started.')
        try:
            path = create_path(self.root, self.systems, system, self.fabric_adapters, fabric_adapter, self.fabric_adapter_ports)
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                logging.info('The given path : {} already exists.'.format(path))
            config={

                      "@Redfish.Copyright": "Copyright 2015-2021 SNIA. All rights reserved.",
                      "@odata.id": "/redfish/v1/Systems/{system}/FabricAdapters/{fabric_adapter}/Ports",
                      "@odata.type": "#PortCollection.PortCollection",
                      "Name": "Port Collection",
                      "Members@odata.count": 0,
                      "Members": [
                      ]
                    }
            with open(os.path.join(path, "index.json"), "w") as fd:
                fd.write(json.dumps(config, indent=4, sort_keys=True))

            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        logging.info('CreateFabricAdapterPorts put exit.')
        return resp
