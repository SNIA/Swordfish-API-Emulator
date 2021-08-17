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

# classesofservice_api.py

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
from .templates.classesofservice import get_ClassesOfService_instance


members =[]
member_ids = []
foo = False
config = {}
INTERNAL_ERROR = 500


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
        return get_json_data (path)

    # HTTP POST
    # - Create the resource (since URI variables are available)
    # - Update the members and members.id lists
    # - Attach the APIs of subordinate resources (do this only once)
    # - Finally, create an instance of the subordiante resources
    def post(self, storage_service, classes_of_service):
        logging.info('ClassesOfServiceAPI PUT called')
        path = create_path(self.root, self.storage_services, storage_service, self.classes_of_service, classes_of_service)
        collection_path = create_path(self.root, self.storage_services, storage_service, self.classes_of_service)

        if classes_of_service in members:
            resp = 404
            return resp
        try:
            global config

            wildcards = {'s_id':storage_service, 'clos_id': classes_of_service, 'rb': g.rest_base}
            config=get_ClassesOfService_instance(wildcards)

            config = create_and_patch_object (config, members, member_ids, path, collection_path)

            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        logging.info('ClassesOfServiceAPI put exit')
        return resp

	# HTTP PATCH
    def patch(self, storage_service, classes_of_service):

        path = os.path.join(self.root, self.storage_services, storage_service, self.classes_of_service, classes_of_service, 'index.json')
        patch_object(path)
        return self.get(fabric)


    # HTTP DELETE
    def delete(self,storage_service,classes_of_service):

        path = create_path(self.root, self.storage_services, storage_service, self.classes_of_service, classes_of_service).replace("\\","/")
        collection_path = create_path(self.root, self.storage_services, storage_service, self.classes_of_service).replace("\\","/")
        return delete_object(path, base_path)


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

    def verify(self, config):
        # TODO: Implement a method to verify that the POST body is valid
        return True,{}

    # HTTP POST
    # POST should allow adding multiple instances to a collection.
    # For now, this only adds one instance.
    # TODO: 'id' should be obtained from the request data.
    def post(self, storage_service):
        logging.info('ClassesOfServiceCollectionAPI POST called')
        try:
            config = request.get_json(force=True)
            ok, msg = self.verify(config)
            if ok:
                # Save the new singleton
                singleton_name = os.path.basename(config['@odata.id'])
                path = os.path.join(self.root, self.storage_services, storage_service, self.classes_of_service, singleton_name)
                if not os.path.exists(path):
                    os.mkdir(path)
                with open(os.path.join(path, "index.json"), "w") as fd:
                    fd.write(json.dumps(config, indent=4, sort_keys=True))
                # Update the collection
                collection_path = os.path.join(self.root, self.storage_services, storage_service, self.classes_of_service, 'index.json')
                update_collections_json(collection_path, config['@odata.id'])
                # Return a copy of the new singleton with a Created response
                resp = config, 201
            else:
                resp = msg, 400
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        return resp


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
                      "@Redfish.Copyright": "Copyright 2015-2021 SNIA. All rights reserved.",
                      "@odata.id": "/redfish/v1/StorageServices/$metadata#/ClassesOfService",
                      "@odata.type": "#ClassOfServiceCollection.ClassOfServiceCollection",
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
