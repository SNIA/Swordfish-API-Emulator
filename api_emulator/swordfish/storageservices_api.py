#
# Copyright (c) 2017-2018, The Storage Networking Industry Association.
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

# StorageServices_api.py
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
from .volumes_api import CreateVolume
from .templates.StorageServices import get_StorageServices_instance
from .storagepools_api import StoragePoolsAPI, CreateStoragePools
from .filesystems_api import FileSystemsAPI, CreateFileSystems
from .drives_api import DrivesAPI, CreateDrives
from .endpoints_api import EndpointsAPI, CreateEndpoints
from .endpointgroups_api import EndpointGroupsAPI, CreateEndpointGroups
from .classesofservice_api import ClassesOfServiceAPI, CreateClassesOfService, ClassesOfServiceCollectionAPI
from .dataprotectionloscapabilities_api import DataProtectionLoSCapabilitiesAPI, CreateDataProtectionLoSCapabilities
from .storagegroups_api import StorageGroupsAPI, CreateStorageGroups
from .storagesubsystems_api import StorageSubsystemsAPI, CreateStorageSubsystems
from .datasecurityloscapabilities_api import DataSecurityLoSCapabilitiesAPI, CreateDataSecurityLoSCapabilities
from .datastorageloscapabilities_api import DataStorageLoSCapabilitiesAPI, CreateDataStorageLoSCapabilities
from .ioperformanceloscapabilities_api import IOPerformanceLoSCapabilitiesAPI, CreateIOPerformanceLoSCapabilities
from .ioconnectivityloscapabilities_api import IOConnectivityLoSCapabilitiesAPI, CreateIOConnectivityLoSCapabilities


# config is instantiated by CreateStorageServices()
members =[]
member_ids = []
foo = False
config = {}
INTERNAL_ERROR = 500


def create_path(*args):
    trimmed = [str(arg).strip('/') for arg in args]
    return os.path.join(*trimmed)

# StorageServices API
class StorageServicesAPI(Resource):
    def __init__(self, **kwargs):
        logging.info('StorageServicesAPI init called')
        self.root = PATHS['Root']
        self.storage_services = PATHS['StorageServices']['path']


    # HTTP GET
    def get(self, storage_service):
        path = os.path.join(self.root, self.storage_services, storage_service, 'index.json')
        try:
            storage_service_json = open(path)
            data = json.load(storage_service_json)
        except Exception as e:
            traceback.print_exc()
            raise Exception("Unable read file because of following error::{}".format(e))
        return jsonify(data)

    # HTTP POST
    # - Create the resource (since URI variables are available)
    # - Update the members and members.id lists
    # - Attach the APIs of subordinate resources (do this only once)
    # - Finally, create an instance of the subordiante resources
    def post(self,storage_service):
        logging.info('StorageServicesAPI PUT called')
        try:
            global config
            global foo

            wildcards = {'id': storage_service, 'rb': g.rest_base}

            config=get_StorageServices_instance(wildcards)


            members.append(config)
            member_ids.append({'@odata.id': config['@odata.id']})

            path = os.path.join(self.root, self.storage_services, storage_service)
            if not os.path.exists(path):
                os.mkdir(path)

            with open(os.path.join(path, "index.json"), "w") as fd:
                fd.write(json.dumps(config, indent=4, sort_keys=True))

            collection_path = os.path.join(self.root, self.storage_services, 'index.json')
            update_collections_json(path=collection_path, link=config['@odata.id'])

            # Create instances of subordinate resources, then call put operation


            cfg = CreateVolume()
            cfg.put(storage_service)
            cfg = CreateStoragePools()
            cfg.put(storage_service)
            cfg = CreateFileSystems()
            cfg.put(storage_service)
            cfg = CreateDrives()
            cfg.put(storage_service)
            cfg = CreateStorageGroups()
            cfg.put(storage_service)
            cfg = CreateDataProtectionLoSCapabilities()
            cfg.put(storage_service)
            cfg = CreateDataSecurityLoSCapabilities()
            cfg.put(storage_service)
            cfg = CreateDataStorageLoSCapabilities()
            cfg.put(storage_service)
            cfg = CreateIOPerformanceLoSCapabilities()
            cfg.put(storage_service)
            cfg = CreateIOConnectivityLoSCapabilities()
            cfg.put(storage_service)
            cfg = CreateEndpoints()
            cfg.put(storage_service)
            cfg = CreateEndpointGroups()
            cfg.put(storage_service)
            cfg = CreateClassesOfService()
            cfg.put(storage_service)
            cfg = CreateStorageSubsystems()
            cfg.put(storage_service)



            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        logging.info('StorageServicesAPI put exit')
        return resp

    # HTTP PATCH
    def patch(self, ident):
        logging.info('StorageServicesAPI patch called')
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
    def delete(self,storage_service):

        path = os.path.join(self.root, self.storage_services, storage_service, 'index.json')
        print (path)

        try:
            with open(path,"r") as pdata:
                pdata = json.load(pdata)

            data = json.loads(request.data)
            jdata = data["@odata.id"].split('/')
            for element in pdata:

                if element == jdata[len(jdata)-1]:

                    pdata.pop(element)

                    break

            path1 = os.path.join(self.root, self.storage_services, storage_service, jdata[len(jdata)-1])

            shutil.rmtree(path1)

            with open(path,"w") as jdata:

                json.dump(pdata,jdata)

        except Exception as e:
            return {"error": "Unable read file because of following error::{}".format(e)}, 500

        return jsonify(pdata)


# StorageServices Collection API
class StorageServicesCollectionAPI(Resource):

    def __init__(self):
        self.root = PATHS['Root']
        self.storage_services = PATHS['StorageServices']['path']

    def get(self):
        path = os.path.join(self.root, self.storage_services, 'index.json')
        try:
            storage_services_json = open(path)
            data = json.load(storage_services_json)
        except Exception as e:
            traceback.print_exc()
            return {"error": "Unable read file because of following error::{}".format(e)}, 500

        return jsonify(data)

    def put(self):
        pass

    def delete(self):

        path = os.path.join(self.root, self.storage_services, 'index.json')


        try:
            with open(path,"r") as pdata:
                pdata = json.load(pdata)

            data = json.loads(request.data)
            jdata = data["@odata.id"].split('/')
            path1 = os.path.join(self.root, self.storage_services, jdata[len(jdata)-1])
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

# CreateStorageServices
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
class CreateStorageServices (Resource):
    def __init__(self, **kwargs):
        logging.info('CreateStorageServices init called')
        logging.debug(kwargs)#, kwargs.keys(), 'resource_class_kwargs' in kwargs)
        if 'resource_class_kwargs' in kwargs:
            global wildcards
            wildcards = copy.deepcopy(kwargs['resource_class_kwargs'])
            logging.debug(wildcards)#, wildcards.keys())

    # Attach APIs for subordinate resource(s). Attach the APIs for a resource collection and its singletons
    def put(self,ident):
        logging.info('CreateStorageServices put called')
        try:
            global config
            global wildcards
            wildcards['id'] = ident
            config=get_StorageServices_instance(wildcards)
            members[ident]=config

            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        logging.info('StorageServices init exit')
        return resp