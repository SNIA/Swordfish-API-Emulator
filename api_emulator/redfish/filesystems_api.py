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

# filesystems_api.py

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
from .templates.filesystems import get_FileSystems_instance

members =[]
member_ids = []
foo = False
config = {}
INTERNAL_ERROR = 500

# FileSystemsAPI API
class FileSystemsAPI(Resource):
    def __init__(self, **kwargs):
        logging.info('FileSystemsAPI init called')
        self.root = PATHS['Root']
        self.storage_services = PATHS['StorageServices']['path']
        self.file_systems = PATHS['StorageServices']['file_systems']

    # HTTP GET
    def get(self, storage_service, file_systems):
        path = create_path(self.root, self.storage_services, storage_service, self.file_systems, file_systems, 'index.json')
        return get_json_data (path)

    # HTTP POST
    # - Create the resource (since URI variables are available)
    # - Update the members and members.id lists
    # - Attach the APIs of subordinate resources (do this only once)
    # - Finally, create an instance of the subordiante resources
    def post(self, storage_service, file_systems):
        logging.info('FileSystemsAPI PUT called')
        try:
            global config
            global foo

            wildcards = {'s_id':storage_service, 'fss_id': file_systems, 'rb': g.rest_base}
            config=get_FileSystems_instance(wildcards)

            members.append(config)
            member_ids.append({'@odata.id': config['@odata.id']})

            # Create instances of subordinate resources, then call put operation
            # not implemented yet

            path = create_path(self.root, self.storage_services, storage_service, self.file_systems, file_systems)
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                # This will execute when POST is called for more than one time for a resource
                return config, 500
            with open(os.path.join(path, "index.json"), "w") as fd:
                fd.write(json.dumps(config, indent=4, sort_keys=True))

            # update the collection json file with new added resource
            collection_path = os.path.join(self.root, self.storage_services, storage_service, self.file_systems, 'index.json')
            update_collections_json(path=collection_path, link=config['@odata.id'])
            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        logging.info('FileSystemsAPI put exit')
        return resp
	# HTTP PATCH
    def patch(self, storage_service, file_systems):
        path = os.path.join(self.root, self.storage_services, storage_service,
                                       self.file_systems, file_systems, 'index.json')
        try:
            # Read json from file.
            with open(path, 'r') as file_systems_json:
                data = json.load(file_systems_json)
                file_systems_json.close()

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

        json_data = self.get(storage_service, file_systems)
        return json_data


    # HTTP DELETE
    def delete(self,storage_service, file_systems):
        print ("rklnr")
        path = os.path.join(self.root, self.storage_services, storage_service, self.file_systems, file_systems).replace("\\","/")
        delPath = path.replace('Resources','/redfish/v1')
        path2 = os.path.join(self.root, self.storage_services, storage_service, self.file_systems, 'index.json').replace("\\","/")

        try:
            with open(path2,"r") as sdata:
                sdata = json.load(sdata)

            data = {
            "@odata.id":delPath
            }
            resp = 200
            jdata = data["@odata.id"].split('/')

            path1 = os.path.join(self.root, self.storage_services, storage_service, self.file_systems, jdata[len(jdata)-1])

            shutil.rmtree(path1)
            sdata['Members'].remove(data)
            sdata['Members@odata.count'] = int(sdata['Members@odata.count']) - 1

            with open(path2,"w") as jdata:

                json.dump(sdata,jdata)

        except Exception as e:
            return {"error": "Unable read file because of following error::{}".format(e)}, 500

        return jsonify(resp)

# FileSystems Collection API
class FileSystemsCollectionAPI(Resource):

    def __init__(self):
        self.root = PATHS['Root']
        self.storage_services = PATHS['StorageServices']['path']
        self.file_systems = PATHS['StorageServices']['file_systems']

    def get(self, storage_service):
        path = os.path.join(self.root, self.storage_services, storage_service, self.file_systems, 'index.json')
        return get_json_data (path)

    def verify(self, config):
        # TODO: Implement a method to verify that the POST body is valid
        return True,{}

    # HTTP POST
    # POST should allow adding multiple instances to a collection.
    # For now, this only adds one instance.
    # TODO: 'id' should be obtained from the request data.
    def post(self, storage_service):
        logging.info('FileSystemsCollectionAPI POST called')
        try:
            config = request.get_json(force=True)
            ok, msg = self.verify(config)
            if ok:
                # Save the new singleton
                singleton_name = os.path.basename(config['@odata.id'])
                path = os.path.join(self.root, self.storage_services, storage_service, self.file_systems, singleton_name)
                if not os.path.exists(path):
                    os.mkdir(path)
                with open(os.path.join(path, "index.json"), "w") as fd:
                    fd.write(json.dumps(config, indent=4, sort_keys=True))
                # Update the collection
                collection_path = os.path.join(self.root, self.storage_services, storage_service, self.file_systems, 'index.json')
                update_collections_json(collection_path, config['@odata.id'])
                # Return a copy of the new singleton with a Created response
                resp = config, 201
            else:
                resp = msg, 400
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        return resp


class CreateFileSystems (Resource):
    def __init__(self):
        self.root = PATHS['Root']
        self.storage_services = PATHS['StorageServices']['path']
        self.file_systems = PATHS['StorageServices']['file_systems']

    # Attach APIs for subordinate resource(s). Attach the APIs for a resource collection and its singletons
    def put(self,storage_service):
        logging.info('CreateFileSystems put started.')
        try:
            path = create_path(self.root, self.storage_services, storage_service, self.file_systems)
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                logging.info('The given path : {} already Exist.'.format(path))
            config={
                      "@Redfish.Copyright": "Copyright 2015-2021 SNIA. All rights reserved.",
                      "@odata.id": "/redfish/v1/StorageServices/$metadata#/FileSystems",
                      "@odata.type": "#FileSystemsCollection.FileSystemsCollection",
                      "Name": "FileSystems Collection",
                      "Members@odata.count": 0,
                      "Members": [
                      ],
                      "Permissions": [
                                {"Read": "True"},
                                {"Write": "True"}]
                    }
            with open(os.path.join(path, "index.json"), "w") as fd:
                fd.write(json.dumps(config, indent=4, sort_keys=True))

            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        logging.info('CreateFileSystems put exit.')
        return resp
