
import json, os
import shutil

import traceback
import logging
import g
import urllib2

from flask import jsonify, request
from flask.ext.restful import Resource
from api_emulator.utils import update_collections_json
from constants import *
from .templates.classesofservice import get_ClassesOfService_instance


members =[]
member_ids = []
foo = False
config = {}
INTERNAL_ERROR = 500




def create_path(*args):
    trimmed = [str(arg).strip('/') for arg in args]
    return os.path.join(*trimmed)


# ClassesOfServiceAPI 
class ClassesOfServiceAPI(Resource):
    def __init__(self, **kwargs):
        logging.info('ClassesOfServiceAPI init called')
        self.root = PATHS['Root']
        self.storage_services = PATHS['StorageServices']['path']
        self.classes_of_service = PATHS['StorageServices']['classes_of_service']

    # HTTP GET
    def get(self, storage_service, classes_of_service):
        path = create_path(self.root, self.storage_services, storage_service, self.classes_of_service, classes_of_service, 'index.json')
        try:
            classes_of_service_json = open(path)
            data = json.load(classes_of_service_json)
        except Exception as e:
            traceback.print_exc()
            raise Exception("Unable read file because of following error::{}".format(e))
        return jsonify(data)

    # HTTP POST
    # - Create the resource (since URI variables are available)
    # - Update the members and members.id lists
    # - Attach the APIs of subordinate resources (do this only once)
    # - Finally, create an instance of the subordiante resources
    def post(self, storage_service, classes_of_service):
        logging.info('ClassesOfServiceAPI PUT called')
        try:
            global config
            global foo

            wildcards = {'s_id':storage_service, 'clos_id': classes_of_service, 'rb': g.rest_base}
            config=get_ClassesOfService_instance(wildcards)

            members.append(config)
            member_ids.append({'@odata.id': config['@odata.id']})

            # Create instances of subordinate resources, then call put operation
            # not implemented yet

            path = create_path(self.root, self.storage_services, storage_service, self.classes_of_service, classes_of_service)
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                # This will execute when POST is called for more than one time for a resource
                return config, 500
            with open(os.path.join(path, "index.json"), "w") as fd:
                fd.write(json.dumps(config, indent=4, sort_keys=True))


            # update the collection json file with new added resource
            collection_path = os.path.join(self.root, self.storage_services, storage_service, self.classes_of_service, 'index.json')
            update_collections_json(path=collection_path, link=config['@odata.id'])
            
            
            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        logging.info('ClassesOfServiceAPI put exit')
        return resp
    
    def put(self, storage_service, classes_of_service):
        
        path = os.path.join(self.root, self.storage_services, storage_service, self.classes_of_service, classes_of_service, 'index.json')
        try:
            # Read json from file.
            with open(path, 'r') as classes_of_service_json:
                data = json.load(classes_of_service_json)
                classes_of_service_json.close()

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

        json_data = self.get(storage_service, classes_of_service)
        return json_data

    # HTTP DELETE
    def delete(self,storage_service):
        
        path = create_path(self.root, self.storage_services, storage_service, self.classes_of_service, classes_of_service, 'index.json')
        print path            
        
        try:
            with open(path,"r") as pdata:
                pdata = json.load(pdata)
                
            data = json.loads(request.data)
            jdata = data["@odata.id"].split('/')
            for element in pdata: 
                if element == jdata[len(jdata)-1]:
                    pdata.pop(element)
                    
            
            path1 = os.path.join(self.root, self.storage_services, storage_service,  self.classes_of_service, classes_of_service, sjdata[len(jdata)-1])
            
            shutil.rmtree(path1)
            
           

            with open(path,"w") as jdata:                
                
                json.dump(pdata,jdata)

        except Exception as e:
            return {"error": "Unable read file because of following error::{}".format(e)}, 500

        return jsonify(pdata)


# ClassesOfService Collection API
class ClassesOfServiceCollectionAPI(Resource):

    def __init__(self):
        self.root = PATHS['Root']
        self.storage_services = PATHS['StorageServices']['path']
        self.classes_of_service = PATHS['StorageServices']['classes_of_service']

    def get(self, storage_service):
        path = os.path.join(self.root, self.storage_services, storage_service, self.classes_of_service, 'index.json')
        try:
            classes_of_service_json = open(path)
            data = json.load(classes_of_service_json)
        except Exception as e:
            traceback.print_exc()
            return {"error": "Unable read file because of following error::{}".format(e)}, 500

        return jsonify(data)

    def put(self):
        pass

    def delete(self):
        
        path = os.path.join(self.root, self.storage_services, storage_service, self.classes_of_service, 'index.json')
                    
        
        try:
            with open(path,"r") as pdata:
                pdata = json.load(pdata)
                
            data = json.loads(request.data)
            jdata = data["@odata.id"].split('/')
            path1 = os.path.join(self.root, self.storage_services, storage_service, self.classes_of_service, jdata[len(jdata)-1])
            shutil.rmtree(path1)
            pdata['Members'].remove(data)
           

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

"""class ClassesOfServiceChildAPI(Resource):

    def __init__(self):
        self.root = PATHS['Root']
        self.storage_services = PATHS['StorageServices']['path']
        self.classes_of_service = PATHS['StorageServices']['classes_of_service']

    def get(self, storage_service, volumes, values):
        path = '{}{}{}/{}{}/{}/{}'.format(self.root, self.storage_services, storage_service,
                                       self.volumes, volumes, values, 'index.json')

        try:
            volumes_json = open(path)
            data = json.load(volumes_json)
        except Exception as e:
            traceback.print_exc()
            return {"error": "Unable read file because of following error::{}".format(e)}, 500

        return jsonify(data)"""

class CreateClassesOfService (Resource):
    def __init__(self):
        self.root = PATHS['Root']
        self.storage_services = PATHS['StorageServices']['path']
        self.classes_of_service = PATHS['StorageServices']['classes_of_service']

    # Attach APIs for subordinate resource(s). Attach the APIs for a resource collection and its singletons
    def put(self,storage_service):
        logging.info('CreateClassesOfService put started.')
        try:
            path = create_path(self.root, self.storage_services, storage_service, self.classes_of_service)
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                logging.info('The given path : {} already Exist.'.format(path))
            config={  
                      "@Redfish.Copyright": "Copyright 2015-2017 SNIA. All rights reserved.",
                      "@odata.context": "/redfish/v1/$metadata#ClassesOfService.ClassesOfService",
                      "@odata.id": "/redfish/v1/StorageServices/$metadata#/ClassesOfService",
                      "@odata.type": "#ClassOfServiceCollection.v1_0_0.ClassOfServiceCollection",
                      "Name": "ClassesOfService",
                      "Members@odata.count": 0,
                      "Members": [
                      ],
                      "Permissions": [
                                {"Read": "True"},
                                {"Write": "False"}]
                    }
            with open(os.path.join(path, "index.json"), "w") as fd:
                fd.write(json.dumps(config, indent=4, sort_keys=True))

            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        logging.info('CreateClassesOfService put exit.')
        return resp