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

# storagesubsystems_api.py
import json, os
import traceback
import logging
import g
import shutil

import urllib3

from flask import jsonify, request
from flask.ext.restful import Resource
from api_emulator.utils import update_collections_json
from .constants import *
from .templates.storagesubsystems import get_StorageSubsystems_instance

members =[]
member_ids = []
foo = False
config = {}
INTERNAL_ERROR = 500




def create_path(*args):
    trimmed = [str(arg).strip('/') for arg in args]
    return os.path.join(*trimmed)


# StorageSubsystemsAPI API
class StorageSubsystemsAPI(Resource):
    def __init__(self, **kwargs):
        logging.info('StorageSubsystemsAPI init called')
        self.root = PATHS['Root']
        self.storage_services = PATHS['StorageServices']['path']
        self.storage_subsystems = PATHS['StorageServices']['storage_subsystems']

    
    # HTTP GET
    def get(self, storage_service):
        path = os.path.join(self.root, self.storage_services, storage_service, self.storage_subsystems, 'index.json')
        try:
            storage_subsystems_json = open(path)
            data = json.load(storage_subsystems_json)
            print (data)
        except Exception as e:
            traceback.print_exc()
            raise Exception("Unable read file because of following error::{}".format(e))
        return jsonify(data)
        print (data)

    def put(self, storage_service):
        path = os.path.join(self.root, self.storage_services, storage_service,
                                       self.storage_subsystems, 'index.json')

        try:
            # Read json from file.
            with open(path, 'r') as storage_subsystems_json:
                data = json.load(storage_subsystems_json)
                storage_subsystems_json.close()

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

    



class CreateStorageSubsystems(Resource):
    def __init__(self):
        self.root = PATHS['Root']
        self.storage_services = PATHS['StorageServices']['path']
        self.storage_subsystems = PATHS['StorageServices']['storage_subsystems']

    def put(self,storage_service):
        logging.info('CreateStorageSubsystems put started.')
        global config
        try:
            
            path = create_path(self.root, self.storage_services, storage_service, self.storage_subsystems)
            if not os.path.exists(path):
                os.mkdir(path)
            else: 
                print ("ihuh")
            wildcards = {'s_id':storage_service,'rb': g.rest_base}
                
            config=get_StorageSubsystems_instance(wildcards)
            
            with open(os.path.join(path, "index.json"), "w") as fd:
                fd.write(json.dumps(config, indent=4, sort_keys=True))

            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        logging.info('CreateStorageSubsystems put exit.')
        return resp