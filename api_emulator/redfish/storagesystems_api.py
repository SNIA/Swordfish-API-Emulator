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
# StorageSystems_api.py
#
# Collection API  GET, POST
# Singleton  API  GET, PUT, PATCH, DELETE

import g, json, urllib3
import shutil

import sys, traceback
import logging
import copy
import os

from flask import request, make_response, render_template, jsonify
from flask_restful import reqparse, Api, Resource
from .constants import *
from api_emulator.utils import update_collections_json

from .templates.StorageSystems import get_StorageSystems_instance


# config is instantiated by CreateStorageSystems()
members =[]
member_ids = []
foo = False
config = {}
INTERNAL_ERROR = 500


def create_path(*args):
    trimmed = [str(arg).strip('/') for arg in args]
    return os.path.join(*trimmed)

# StorageSystems API
class StorageSystemsAPI(Resource):
    def __init__(self, **kwargs):
        logging.info('StorageSystemsAPI init called')
        self.root = PATHS['Root']
        self.storage_systems = PATHS['StorageSystems']['path']


    # HTTP GET
    def get(self, storage_systems):
        path = os.path.join(self.root, self.storage_systems, storage_systems, 'index.json')
        try:
            storage_systems_json = open(path)
            data = json.load(storage_systems_json)
        except Exception as e:
            traceback.print_exc()
            raise Exception("Unable read file because of following error::{}".format(e))
        return jsonify(data)

    # HTTP POST
    # - Create the resource (since URI variables are available)
    # - Update the members and members.id lists
    # - Attach the APIs of subordinate resources (do this only once)
    # - Finally, create an instance of the subordiante resources
    def post(self,storage_systems):
        logging.info('StorageSystemsAPI PUT called')
        try:
            global config
            global foo
            
            wildcards = {'id': storage_systems, 'rb': g.rest_base}
            
            config=get_StorageSystems_instance(wildcards)
            

            members.append(config)
            member_ids.append({'@odata.id': config['@odata.id']})
            
            path = os.path.join(self.root, self.storage_systems, storage_systems)
            if not os.path.exists(path):
                os.mkdir(path)

            with open(os.path.join(path, "index.json"), "w") as fd:
                fd.write(json.dumps(config, indent=4, sort_keys=True))

            collection_path = os.path.join(self.root, self.storage_systems, 'index.json')
            update_collections_json(path=collection_path, link=config['@odata.id'])

            # Create instances of subordinate resources, then call put operation
            
            
            
            
            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        logging.info('StorageSystemsAPI put exit')
        return resp

    # HTTP PATCH
    def patch(self, storage_systems):
        path = os.path.join(self.root, self.storage_systems, storage_systems,
                                        'index.json')
        print (path)
        try:
            # Read json from file.
            with open(path, 'r') as storage_systems_json:
                data = json.load(storage_systems_json)
                storage_systems_json.close()

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
        
        json_data = self.get(storage_systems)
        return json_data

    # HTTP DELETE
    def delete(self,storage_systems):
        
        path = os.path.join(self.root, self.storage_systems, storage_systems)
        print (path)
        delPath = path.replace('Resources','/redfish/v1')
        path2 = os.path.join(self.root, self.storage_systems, 'index.json')
        try:
            with open(path2,"r") as pdata:
                pdata = json.load(pdata)
                
            data = {
            "@odata.id":delPath
            }            
            resp = 200
            jdata = data["@odata.id"].split('/')
            
            path1 = os.path.join(self.root, self.storage_systems, jdata[len(jdata)-1])
            shutil.rmtree(path1)
            pdata['Members'].remove(data)
            pdata['Members@odata.count'] = int(pdata['Members@odata.count']) - 1
          
            with open(path2,"w") as jdata:
                json.dump(pdata,jdata)
                       

        except Exception as e:
            return {"error": "Unable read file because of following error::{}".format(e)}, 500

        return jsonify(resp)

# StorageSystems Collection API
class StorageSystemsCollectionAPI(Resource):

    def __init__(self):
        self.root = PATHS['Root']
        self.storage_systems = PATHS['StorageSystems']['path']

    def get(self):
        path = os.path.join(self.root, self.storage_systems, 'index.json')
        try:
            storage_systems_json = open(path)
            data = json.load(storage_systems_json)
        except Exception as e:
            traceback.print_exc()
            return {"error": "Unable read file because of following error::{}".format(e)}, 500

        return jsonify(data)

    def verify(self, config):
        # TODO: Implement a method to verify that the POST body is valid
        return True,{}

    # HTTP POST
    # POST should allow adding multiple instances to a collection.
    # For now, this only adds one instance.
    # TODO: 'id' should be obtained from the request data.
    def post(self):
        logging.info('StorageSystemsCollectionAPI POST called')
        try:
            config = request.get_json(force=True)
            ok, msg = self.verify(config)
            if ok:
                # Save the new singleton
                singleton_name = os.path.basename(config['@odata.id'])
                path = os.path.join(self.root, self.storage_systems, singleton_name)
                if not os.path.exists(path):
                    os.mkdir(path)
                with open(os.path.join(path, "index.json"), "w") as fd:
                    fd.write(json.dumps(config, indent=4, sort_keys=True))
                # Update the collection
                collection_path = os.path.join(self.root, self.storage_systems, 'index.json')
                update_collections_json(collection_path, config['@odata.id'])
                # Return a copy of the new singleton with a Created response
                resp = config, 201
            else:
                resp = msg, 400
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        return resp


# CreateStorageSystems
#
# Called internally to create a instances of a resource.  If the resource has subordinate resources,
# those subordinate resource(s)  should be created automatically.
#
# This routine can also be used to pre-populate emulator with resource instances.  For example, a couple of
# Chassis and a Chassis (see examples in resource_manager.py)
#
# Note: this may not the optimal way to pre-populate the emulator, since the resource_manager.py files needs
# to be editted.  A better method is just hack up a copy of usertest.py which performs a POST for each resource
# instance desired (e.g. populate.py).  Then one could have a multiple 'populate' files and the emulator doesn't
# need to change.
# 
# Note: In 'init', the first time through, kwargs may not have any values, so we need to check.
#   The call to 'init' stores the path wildcards. The wildcards are used when subsequent calls instanctiate
#   resources to modify the resource template.
#
class CreateStorageSystems (Resource):
    def __init__(self, **kwargs):
        logging.info('CreateStorageSystems init called')
        logging.debug(kwargs)#, kwargs.keys(), 'resource_class_kwargs' in kwargs)
        if 'resource_class_kwargs' in kwargs:
            global wildcards
            wildcards = copy.deepcopy(kwargs['resource_class_kwargs'])
            logging.debug(wildcards)#, wildcards.keys())

    # Attach APIs for subordinate resource(s). Attach the APIs for a resource collection and its singletons
    def put(self,ident):
        logging.info('CreateStorageSystems put called')
        try:
            global config
            global wildcards
            wildcards['id'] = ident
            config=get_StorageSystems_instance(wildcards)
            members[ident]=config

            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        logging.info('StorageSystems init exit')
        return resp
