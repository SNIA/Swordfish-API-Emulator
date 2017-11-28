# Copyright Notice:
# Copyright 2017 Storage Networking Industry Association (SNIA), USA. All rights reserved.
# License: BSD 3-Clause License. For full SNIA copyright terms, please see http://www.snia.org/about/corporate_info/copyright

#storagegroups_api.py

import json, os
import traceback
import shutil

import logging
import g
import urllib2

from flask import jsonify, request
from flask.ext.restful import Resource
from api_emulator.utils import update_collections_json
from constants import *
from .templates.storagegroups import get_StorageGroups_instance

members =[]
member_ids = []
foo = False
config = {}
INTERNAL_ERROR = 500


def create_path(*args):
    trimmed = [str(arg).strip('/') for arg in args]
    return os.path.join(*trimmed)


# StorageGroups API
class StorageGroupsAPI(Resource):
    def __init__(self, **kwargs):
        logging.info('StorageGroupsAPI init called')
        self.root = PATHS['Root']
        self.storage_services = PATHS['StorageServices']['path']
        self.storage_groups = PATHS['StorageServices']['storage_groups']

    # HTTP GET
    def get(self, storage_service, storage_groups):
        path = create_path(self.root, self.storage_services, storage_service, self.storage_groups, storage_groups, 'index.json')
        try:
            storage_groups_json = open(path)
            data = json.load(storage_groups_json)
        except Exception as e:
            traceback.print_exc()
            raise Exception("Unable read file because of following error::{}".format(e))
        return jsonify(data)

    # HTTP POST
    # - Create the resource (since URI variables are available)
    # - Update the members and members.id lists
    # - Attach the APIs of subordinate resources (do this only once)
    # - Finally, create an instance of the subordiante resources
    def post(self, storage_service, storage_groups):
        logging.info('StorageGroupsAPI PUT called')
        try:
            global config
            global foo

            wildcards = {'s_id':storage_service, 'sg_id': storage_groups, 'rb': g.rest_base}
            config=get_StorageGroups_instance(wildcards)

            members.append(config)
            member_ids.append({'@odata.id': config['@odata.id']})

            # Create instances of subordinate resources, then call put operation
            # not implemented yet

            path = create_path(self.root, self.storage_services, storage_service, self.storage_groups, storage_groups)
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                # This will execute when POST is called for more than one time for a resource
                return config, 500
            with open(os.path.join(path, "index.json"), "w") as fd:
                fd.write(json.dumps(config, indent=4, sort_keys=True))

            # update the collection json file with new added resource
            collection_path = os.path.join(self.root, self.storage_services, storage_service, self.storage_groups, 'index.json')
            update_collections_json(path=collection_path, link=config['@odata.id'])
            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        logging.info('StorageGroupsAPI put exit')
        return resp

    


    # HTTP DELETE
    def delete(self,storage_service, storage_groups):
        
        path = os.path.join(self.root, self.storage_services, storage_service, self.storage_groups, storage_groups, 'index.json')
        print path            
        
        try:
            with open(path,"r") as pdata:
                pdata = json.load(pdata)
                
            data = json.loads(request.data)
            jdata = data["@odata.id"].split('/')
            for element in pdata: 
                if element == jdata[len(jdata)-1]:
                    pdata.pop(element)
                    
            
            path1 = os.path.join(self.root, self.storage_services, storage_service, self.storage_groups, storage_groups, jdata[len(jdata)-1])
            
            shutil.rmtree(path1)
            
           

            with open(path,"w") as jdata:                
                
                json.dump(pdata,jdata)

        except Exception as e:
            return {"error": "Unable read file because of following error::{}".format(e)}, 500

        return jsonify(pdata)


# StorageGroups Collection API
class StorageGroupsCollectionAPI(Resource):

    def __init__(self):
        self.root = PATHS['Root']
        self.storage_services = PATHS['StorageServices']['path']
        self.storage_groups = PATHS['StorageServices']['storage_groups']

    def get(self, storage_service):
        path = os.path.join(self.root, self.storage_services, storage_service, self.storage_groups, 'index.json')
        try:
            storage_groups_json = open(path)
            data = json.load(storage_groups_json)
        except Exception as e:
            traceback.print_exc()
            return {"error": "Unable read file because of following error::{}".format(e)}, 500

        return jsonify(data)

    def put(self):
        pass

    def delete(self, storage_service):
        print "nklnklndkl"
        path = os.path.join(self.root, self.storage_services, storage_service, self.storage_groups, 'index.json')
                    
        
        try:
            with open(path,"r") as pdata:
                pdata = json.load(pdata)
                
            data = json.loads(request.data)
            jdata = data["@odata.id"].split('/')
            print data
            path1 = os.path.join(self.root, self.storage_services, storage_service, self.storage_groups, jdata[len(jdata)-1])
            shutil.rmtree(path1)
            print path1
            pdata['Members'].remove(data)
            print data
           

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

class StorageGroupsChildAPI(Resource):

    def __init__(self):
        self.root = PATHS['Root']
        self.storage_services = PATHS['StorageServices']['path']
        self.storage_groups = PATHS['StorageServices']['storage_groups']

    def get(self, storage_service, storage_groups, values):
        path = '{}{}{}/{}{}/{}/{}'.format(self.root, self.storage_services, storage_service,
                                       self.storage_groups, storage_groups, values, 'index.json')

        try:
            storage_groups_json = open(path)
            data = json.load(storage_groups_json)
        except Exception as e:
            traceback.print_exc()
            return {"error": "Unable read file because of following error::{}".format(e)}, 500

        return jsonify(data)

class CreateStorageGroups (Resource):
    def __init__(self):
        self.root = PATHS['Root']
        self.storage_services = PATHS['StorageServices']['path']
        self.storage_groups = PATHS['StorageServices']['storage_groups']

    # Attach APIs for subordinate resource(s). Attach the APIs for a resource collection and its singletons
    def put(self,storage_service):
        logging.info('CreateStorageGroups put started.')
        try:
            path = create_path(self.root, self.storage_services, storage_service, self.storage_groups)
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                logging.info('The given path : {} already Exist.'.format(path))
            config={
                     "@Redfish.Copyright": "Copyright 2015-2016 SNIA. All rights reserved.",
                      "@odata.context": "/redfish/v1/$metadata#StorageGroups.StorageGroups",
                      "@odata.id": "/redfish/v1/StorageServices/$metadata#/StorageGroups",
                      "@odata.type": "#StorageGroupsCollection.1.0.0.StorageGroupsCollection",
                      "Name": "StorageGroups Collection",
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
        logging.info('CreateStorageGroups put exit.')
        return resp