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
# storage_api.py


import json, os
import traceback
import logging
import g
import urllib3
import shutil

from flask import jsonify, request
from flask_restful import Resource
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .constants import *
from .templates.Storage import get_Storage_instance

from api_emulator.redfish.storagecontrollers_api import *
from api_emulator.redfish.volumes_api import *
from api_emulator.redfish.storagepools_api import *

members =[]
member_ids = []
config = {}
INTERNAL_ERROR = 500

# StorageAPI
class StorageAPI(Resource):
    def __init__(self, **kwargs):
        logging.info('StorageAPI init called')
        self.root = PATHS['Root']
        self.storage = PATHS['Storage']['path']

    # HTTP GET
    def get(self, storage):
        path = create_path(self.root, self.storage, storage, 'index.json')
        return get_json_data (path)

    # HTTP POST
    # - Create the resource (since URI variables are available)
    # - Update the members and members.id lists
    # - Attach the APIs of subordinate resources (do this only once)
    # - Finally, create an instance of the subordinate resources
    def post(self, storage):
        logging.info('StorageAPI POST called')
        path = create_path(self.root,  self.storage, storage)
        collection_path = os.path.join(self.root, self.storage, 'index.json')
        # Check if collection exists:
        if not os.path.exists(collection_path):
            StorageCollectionAPI.post (self)

        if storage in members:
            resp = 404
            return resp
        try:
            global config
            wildcards = {'s_id':storage, 'rb': g.rest_base}
            config=get_Storage_instance(wildcards)

            config = create_and_patch_object (config, members, member_ids, path, collection_path)

            #Add default placeholder collections to instance.
            VolumesCollectionAPI.post (self, storage)
            StoragePoolsCollectionAPI.post (self, storage)
            StorageControllersCollectionAPI.post (self, storage)

            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        logging.info('StorageAPI POST exit')
        return resp

    # HTTP PUT
    def put(self, storage):
        path = create_path(self.root, self.storage, storage, 'index.json')
        put_object(path)
        return self.get(storage)

	# HTTP PATCH
    def patch(self, storage):
        #Set path to object, then call patch_object:
        path = create_path(self.root, self.storage, storage, 'index.json')
        patch_object(path)
        return self.get(storage)

    # HTTP DELETE
    def delete(self, storage):
        #Set path to object, then call delete_object:
        path = create_path(self.root, self.storage, storage)
        base_path = create_path(self.root, self.storage)
        return delete_object(path, base_path)


# Storage Collection API
class StorageCollectionAPI(Resource):

    def __init__(self):
        self.root = PATHS['Root']
        self.storage = PATHS['Storage']['path']

    def get(self):
        path = os.path.join(self.root, self.storage, 'index.json')
        return get_json_data (path)

    def verify(self, config):
        # TODO: Implement a method to verify that the POST body is valid
        return True,{}

    # HTTP POST Collection
    def post(self):
        self.root = PATHS['Root']
        self.storage = PATHS['Storage']['path']

        path = create_path(self.root, self.storage)
        return create_collection (path, 'Storage')

    # HTTP PUT
    def put(self):
        path = os.path.join(self.root, self.storage, 'index.json')
        put_object(path)
        return self.get(self.root)

    # HTTP DELETE
    def delete(self):
        #Set path to object, then call delete_object:
        path = create_path(self.root, self.storage)
        base_path = create_path(self.root)
        return delete_collection(path, base_path)

class CreateStorage (Resource):

    def __init__(self, **kwargs):
        self.root = PATHS['Root']
        self.storage = PATHS['Storage']['path']

        if 'resource_class_kwargs' in kwargs:
            global wildcards
            wildcards = copy.deepcopy(kwargs['resource_class_kwargs'])
            logging.debug(wildcards)#, wildcards.keys())

    # Attach APIs for subordinate resource(s). Attach the APIs for a resource collection and its singletons
    def put(self,storage):
        logging.info('CreateStorage put started.')
        if storage in members:
            resp = 404
            return resp
        try:
            path = create_path(self.root, self.storage)
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                logging.info('The given path : {} already exists.'.format(path))
                wildcards = {'s_id':storage, 'rb': g.rest_base}
                config=get_Storage_instance(wildcards)
            with open(os.path.join(path, "index.json"), "w") as fd:
                fd.write(json.dumps(config, indent=4, sort_keys=True))

            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        logging.info('CreateStorage put exit.')
        return resp
