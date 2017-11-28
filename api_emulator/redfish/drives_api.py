# Copyright Notice:
# Copyright 2017 Storage Networking Industry Association (SNIA), USA. All rights reserved.
# License: BSD 3-Clause License. For full SNIA copyright terms, please see http://www.snia.org/about/corporate_info/copyright

# drives_api.py
import json, os
import traceback
import logging
import shutil

import g
import urllib2

from flask import jsonify, request
from flask.ext.restful import Resource
from api_emulator.utils import update_collections_json
from constants import *
from .templates.drives import get_Drives_instance

members =[]
member_ids = []
foo = False
config = {}
INTERNAL_ERROR = 500



def create_path(*args):
    trimmed = [str(arg).strip('/') for arg in args]
    return os.path.join(*trimmed)


# DrivesAPI API
class DrivesAPI(Resource):
    def __init__(self, **kwargs):
        logging.info('DrivesAPI init called')
        self.root = PATHS['Root']
        self.storage_services = PATHS['StorageServices']['path']
        self.drives = PATHS['StorageServices']['drives']

    # HTTP GET
    def get(self, storage_service, drives):
        path = create_path(self.root, self.storage_services, storage_service, self.drives, drives, 'index.json')
        try:
            drives_json = open(path)
            data = json.load(drives_json)
        except Exception as e:
            traceback.print_exc()
            raise Exception("Unable read file because of following error::{}".format(e))
        return jsonify(data)

    # HTTP POST
    # - Create the resource (since URI variables are available)
    # - Update the members and members.id lists
    # - Attach the APIs of subordinate resources (do this only once)
    # - Finally, create an instance of the subordiante resources
    def post(self, storage_service, drives):
        logging.info('DrivesAPI PUT called')
        try:
            global config
            global foo

            wildcards = {'s_id':storage_service, 'd_id': drives, 'rb': g.rest_base}
            config=get_Drives_instance(wildcards)

            members.append(config)
            member_ids.append({'@odata.id': config['@odata.id']})

            # Create instances of subordinate resources, then call put operation
            # not implemented yet

            path = create_path(self.root, self.storage_services, storage_service, self.drives, drives)
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                # This will execute when POST is called for more than one time for a resource
                return config, 500
            with open(os.path.join(path, "index.json"), "w") as fd:
                fd.write(json.dumps(config, indent=4, sort_keys=True))

            # update the collection json file with new added resource
            collection_path = os.path.join(self.root, self.storage_services, storage_service, self.drives, 'index.json')
            update_collections_json(path=collection_path, link=config['@odata.id'])
            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        logging.info('DrivesAPI put exit')
        return resp

    # HTTP PATCH
    def patch(self, ident):
        logging.info('DrivesAPI patch called')
        raw_dict = request.get_json(force=True)
        logging.info(raw_dict)
        try:
            # Find the entry with the correct value for Id
            for cfg in members:
                if (ident == cfg["Id"]):
                    break
            config = cfg
            logging.info(config)
            for key, value in raw_dict.items():
                logging.info('Update ' + key + ' to ' + value)
                config[key] = value
            logging.info(config)
            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        return resp


    # HTTP DELETE
    def delete(self,storage_service, drives):
        
        path = os.path.join(self.root, self.storage_services, storage_service, self.drives, drives, 'index.json')
        print path            
        
        try:
            with open(path,"r") as pdata:
                pdata = json.load(pdata)
                
            data = json.loads(request.data)
            jdata = data["@odata.id"].split('/')
            for element in pdata: 
                if element == jdata[len(jdata)-1]:
                    pdata.pop(element)
                    break                     
            
            path1 = os.path.join(self.root, self.storage_services, storage_service, self.drives, drives, jdata[len(jdata)-1])
            
            shutil.rmtree(path1)           
           
            with open(path,"w") as jdata:                
                
                json.dump(pdata,jdata)

        except Exception as e:
            return {"error": "Unable read file because of following error::{}".format(e)}, 500

        return jsonify(pdata)


# Drives Collection API
class DrivesCollectionAPI(Resource):

    def __init__(self):
        self.root = PATHS['Root']
        self.storage_services = PATHS['StorageServices']['path']
        self.drives = PATHS['StorageServices']['drives']

    def get(self, storage_service):
        path = os.path.join(self.root, self.storage_services, storage_service, self.drives, 'index.json')
        try:
            drives_json = open(path)
            data = json.load(drives_json)
        except Exception as e:
            traceback.print_exc()
            return {"error": "Unable read file because of following error::{}".format(e)}, 500

        return jsonify(data)

    def put(self):
        pass

    def delete(self, storage_service):
        
        path = os.path.join(self.root, self.storage_services, storage_service, self.drives, 'index.json')
                    
        
        try:
            with open(path,"r") as pdata:
                pdata = json.load(pdata)
                
            data = json.loads(request.data)
            jdata = data["@odata.id"].split('/')
            path1 = os.path.join(self.root, self.storage_services, storage_service, self.drives, jdata[len(jdata)-1])
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

class CreateDrives (Resource):
    def __init__(self):
        self.root = PATHS['Root']
        self.storage_services = PATHS['StorageServices']['path']
        self.drives = PATHS['StorageServices']['drives']

    # Attach APIs for subordinate resource(s). Attach the APIs for a resource collection and its singletons
    def put(self,storage_service):
        logging.info('CreateDrives put started.')
        try:
            path = create_path(self.root, self.storage_services, storage_service, self.drives)
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                logging.info('The given path : {} already Exist.'.format(path))
            config={
                      "@Redfish.Copyright": "Copyright 2015-2017 SNIA. All rights reserved.",
                      "@odata.context": "/redfish/v1/$metadata#Drives.Drives",                      
                      "@odata.type": "#DriveCollection.v1_0_0.DriveCollection",
                      "Name": "Drives",
                      "Members@odata.count": 1,
                      "Members": [
                      ]
                    }
            with open(os.path.join(path, "index.json"), "w") as fd:
                fd.write(json.dumps(config, indent=4, sort_keys=True))

            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        logging.info('CreateDrives put exit.')
        return resp