""" 
 * Copyright (c) 2017, The Storage Networking Industry Association.
 *  
 * Redistribution and use in source and binary forms, with or without 
 * modification, are permitted provided that the following conditions are met:
 *  
 * Redistributions of source code must retain the above copyright notice, 
 * this list of conditions and the following disclaimer.
 *  
 * Redistributions in binary form must reproduce the above copyright notice, 
 * this list of conditions and the following disclaimer in the documentation 
 * and/or other materials provided with the distribution.
 *  
 * Neither the name of The Storage Networking Industry Association (SNIA) nor 
 * the names of its contributors may be used to endorse or promote products 
 * derived from this software without specific prior written permission.
 *  
 *  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
 *  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
 *  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
 *  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE 
 *  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
 *  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
 *  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS  
 *  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
 *  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
 *  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
 *  THE POSSIBILITY OF SUCH DAMAGE.
"""
#endpoints_api.py

import json, os
import shutil

import traceback
import logging
import g
import urllib3

from flask import jsonify, request
from flask.ext.restful import Resource
from api_emulator.utils import update_collections_json
from .constants import *
from .templates.endpoints import get_Endpoints_instance

members =[]
member_ids = []
foo = False
config = {}
INTERNAL_ERROR = 500



def create_path(*args):
    trimmed = [str(arg).strip('/') for arg in args]
    return os.path.join(*trimmed)


# EndpointsAPI API
class EndpointsAPI(Resource):
    def __init__(self, **kwargs):
        logging.info('EndpointsAPI init called')
        self.root = PATHS['Root']
        self.storage_services = PATHS['StorageServices']['path']
        self.endpoints = PATHS['StorageServices']['endpoints']

    # HTTP GET
    def get(self, storage_service, endpoints):
        path = create_path(self.root, self.storage_services, storage_service, self.endpoints, endpoints, 'index.json')
        try:
            endpoints_json = open(path)
            data = json.load(endpoints_json)
        except Exception as e:
            traceback.print_exc()
            raise Exception("Unable read file because of following error::{}".format(e))
        return jsonify(data)

    # HTTP POST
    # - Create the resource (since URI variables are available)
    # - Update the members and members.id lists
    # - Attach the APIs of subordinate resources (do this only once)
    # - Finally, create an instance of the subordiante resources
    def post(self, storage_service, endpoints):
        logging.info('EndpointsAPI PUT called')
        try:
            global config
            global foo

            wildcards = {'s_id':storage_service, 'ep_id': endpoints, 'rb': g.rest_base}
            config=get_Endpoints_instance(wildcards)

            members.append(config)
            member_ids.append({'@odata.id': config['@odata.id']})

            # Create instances of subordinate resources, then call put operation
            # not implemented yet

            path = create_path(self.root, self.storage_services, storage_service, self.endpoints, endpoints)
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                # This will execute when POST is called for more than one time for a resource
                return config, 500
            with open(os.path.join(path, "index.json"), "w") as fd:
                fd.write(json.dumps(config, indent=4, sort_keys=True))

            # update the collection json file with new added resource
            collection_path = os.path.join(self.root, self.storage_services, storage_service, self.endpoints, 'index.json')
            update_collections_json(path=collection_path, link=config['@odata.id'])
            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        logging.info('EndpointsAPI put exit')
        return resp

    # HTTP DELETE
    def delete(self,storage_service, endpoints):
        
        path = create_path(self.root, self.storage_services, storage_service, self.endpoints, endpoints, 'index.json')
        print (path)            
        
        try:
            with open(path,"r") as pdata:
                pdata = json.load(pdata)
                
            data = json.loads(request.data)
            jdata = data["@odata.id"].split('/')
            for element in pdata: 
                if element == jdata[len(jdata)-1]:
                    pdata.pop(element)             
        
            path1 = os.path.join(self.root, self.storage_services, storage_service, self.endpoints, endpoints, jdata[len(jdata)-1])
            shutil.rmtree(path1)
            
           

            with open(path,"w") as jdata:                
                
                json.dump(pdata,jdata)

        except Exception as e:
            return {"error": "Unable read file because of following error::{}".format(e)}, 500

        return jsonify(pdata)


# Endpoints Collection API
class EndpointsCollectionAPI(Resource):

    def __init__(self):
        self.root = PATHS['Root']
        self.storage_services = PATHS['StorageServices']['path']
        self.endpoints = PATHS['StorageServices']['endpoints']

    def get(self, storage_service):
        path = os.path.join(self.root, self.storage_services, storage_service, self.endpoints, 'index.json')
        try:
            endpoints_json = open(path)
            data = json.load(endpoints_json)
        except Exception as e:
            traceback.print_exc()
            return {"error": "Unable read file because of following error::{}".format(e)}, 500

        return jsonify(data)

    def put(self):
        pass

    def delete(self, storage_service):
        
        path = os.path.join(self.root, self.storage_services, storage_service, self.endpoints, 'index.json')                    
        
        try:
            with open(path,"r") as pdata:
                pdata = json.load(pdata)
                
            data = json.loads(request.data)
            jdata = data["@odata.id"].split('/')
            path1 = os.path.join(self.root, self.storage_services, storage_service, self.endpoints, jdata[len(jdata)-1])
            shutil.rmtree(path1)
            pdata['Members'].remove(data)
            pdata['Members@odata.count'] = int(pdata['Members@odata.count']) - 1
           

            with open(path,"w") as jdata:                
                
                json.dump(pdata,jdata)

        except Exception as e:
            return {"error": "Unable read file because of following error::{}".format(e)}, 500

        return jsonify(pdata)
    def verify(self,config):
        #TODO: implement a method to verify that the POST'ed data is valid
        return True,{}

    # The POST command should be for adding multiple instances. For now, just add one.
    def post(self):
        pass



class CreateEndpoints (Resource):
    def __init__(self):
        self.root = PATHS['Root']
        self.storage_services = PATHS['StorageServices']['path']
        self.endpoints = PATHS['StorageServices']['endpoints']

    # Attach APIs for subordinate resource(s). Attach the APIs for a resource collection and its singletons
    def put(self,storage_service):
        logging.info('CreateEndpoints put started.')
        try:
            path = create_path(self.root, self.storage_services, storage_service, self.endpoints)
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                logging.info('The given path : {} already Exist.'.format(path))
            config={
                      "@Redfish.Copyright": "Copyright 2015-2017 SNIA. All rights reserved.",
                      "@odata.context": "/redfish/v1/$metadata#Endpoints.Endpoints",
                      "@odata.id": "/redfish/v1/StorageServices/$metadata#/Endpoints",
                      "@odata.type": "#EndpointCollection.v1_0_0.EndpointCollection",
                      "Name": "Endpoints Collection",
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
        logging.info('CreateEndpoints put exit.')
        return resp