# Copyright Notice:
# Copyright 2017 Storage Networking Industry Association (SNIA), USA. All rights reserved.
# License: BSD 3-Clause License. For full SNIA copyright terms, please see http://www.snia.org/about/corporate_info/copyright

# filesystems_api.py

import json, os
import traceback
import logging
import g
import urllib2
import shutil


from flask import jsonify, request
from flask.ext.restful import Resource
from api_emulator.utils import update_collections_json
from constants import *
from .templates.filesystems import get_FileSystems_instance

members =[]
member_ids = []
foo = False
config = {}
INTERNAL_ERROR = 500



def create_path(*args):
    trimmed = [str(arg).strip('/') for arg in args]
    return os.path.join(*trimmed)


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
        try:
            file_systems_json = open(path)
            data = json.load(file_systems_json)
        except Exception as e:
            traceback.print_exc()
            raise Exception("Unable read file because of following error::{}".format(e))
        return jsonify(data)

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

    def put(self, storage_service, file_systems):
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
        print "rklnr"
        path = os.path.join(self.root, self.storage_services, storage_service, self.file_systems, file_systems, 'index.json')
        print path            
        
        try:
            print "nod"
            with open(path,"r") as pdata:
                pdata = json.load(pdata)
                
            data = json.loads(request.data)
            jdata = data["@odata.id"].split('/')
            for element in pdata: 
                if element == jdata[len(jdata)-1]:
                    pdata.pop(element)
                    
            
            path1 = os.path.join(self.root, self.storage_services, storage_service, self.file_systems, file_systems, jdata[len(jdata)-1])
            
            shutil.rmtree(path1)
            
           

            with open(path,"w") as jdata:                
                
                json.dump(pdata,jdata)

        except Exception as e:
            return {"error": "Unable read file because of following error::{}".format(e)}, 500

        return jsonify(pdata)

# FileSystems Collection API
class FileSystemsCollectionAPI(Resource):

    def __init__(self):
        self.root = PATHS['Root']
        self.storage_services = PATHS['StorageServices']['path']
        self.file_systems = PATHS['StorageServices']['file_systems']

    def get(self, storage_service):
        path = os.path.join(self.root, self.storage_services, storage_service, self.file_systems, 'index.json')
        try:
            file_systems_json = open(path)
            data = json.load(file_systems_json)
        except Exception as e:
            traceback.print_exc()
            return {"error": "Unable read file because of following error::{}".format(e)}, 500

        return jsonify(data)

    def put(self):
        pass

    def delete(self, storage_service):
        
        path = os.path.join(self.root, self.storage_services, storage_service, self.file_systems, 'index.json')
                    
        
        try:
            with open(path,"r") as pdata:
                pdata = json.load(pdata)
                
            data = json.loads(request.data)
            jdata = data["@odata.id"].split('/')
            path1 = os.path.join(self.root, self.storage_services, storage_service, self.file_systems, jdata[len(jdata)-1])
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

class FileSystemsChildAPI(Resource):

    def __init__(self):
        self.root = PATHS['Root']
        self.storage_services = PATHS['StorageServices']['path']
        self.file_systems = PATHS['StorageServices']['file_systems']

    def get(self, storage_service, file_systems, values):
        path = os.path.join(self.root, self.storage_services, storage_service,
                                       self.file_systems, file_systems, values, 'index.json')

        try:
            file_systems_json = open(path)
            data = json.load(file_systems_json)
        except Exception as e:
            traceback.print_exc()
            return {"error": "Unable read file because of following error::{}".format(e)}, 500

        return jsonify(data)

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
                      "@Redfish.Copyright": "Copyright 2015-2017 SNIA. All rights reserved.",
                      "@odata.context": "/redfish/v1/$metadata#FileSystems.FileSystems",
                      "@odata.id": "/redfish/v1/StorageServices/$metadata#/FileSystems",
                      "@odata.type": "#FileSystemsCollection.1.0.0.FileSystemsCollection",
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