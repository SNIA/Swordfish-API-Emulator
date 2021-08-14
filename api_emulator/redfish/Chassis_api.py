# Copyright Notice:
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
# Copyright 2015-2021 DMTF. All rights reserved.
# License: BSD 3-Clause License. For full text see link: https://github.com/DMTF/Redfish-Interface-Emulator/blob/master/LICENSE.md

# Chassis API File

"""
Collection API:  GET, POST, DELETE, PUT
Singleton  API:  GET, POST, PATCH, PUT, DELETE
"""

import g

import json, os
import sys, traceback
import logging
import copy

from flask import jsonify
from flask import Flask, request, make_response, render_template
from flask_restful import reqparse, Api, Resource
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection

# Resource and SubResource imports
from .templates.Chassis import get_Chassis_instance
from .thermal_api import ThermalAPI, CreateThermal
from .power_api import PowerAPI, CreatePower
from .constants import *

members = []
member_ids = []
config = {}
wildcards = {}
INTERNAL_ERROR = 500

# Chassis Singleton API
class ChassisAPI(Resource):

    # kwargs is used to pass in the wildcards values to be replaced
    # when an instance is created via get_<resource>_instance().
    #
    # The call to attach the API establishes the contents of kwargs.
    # All subsequent HTTP calls go through __init__.
    #
    # __init__ stores kwargs in wildcards, which is used to pass
    # values to the get_<resource>_instance() call.
    def __init__(self, **kwargs):
        logging.info('ChassisAPI init called')
        self.root = PATHS['Root']
        self.chassis = PATHS['Chassis']['path']

    # HTTP GET
    def get(self, ident):
        path = os.path.join(self.root, self.chassis, ident, 'index.json')
        return get_json_data (path)

    # HTTP POST
    # - Create the resource (since URI variables are available)
    # - Update the members and members.id lists
    # - Attach the APIs of subordinate resources (do this only once)
    # - Finally, create an instance of the subordinate resources
    def post(self, ident):
        logging.info('ChassisAPI POST called')
        path = create_path(self.root,  self.chassis, ident)
        collection_path = os.path.join(self.root, self.chassis, 'index.json')
        # Check if collection exists:
        if not os.path.exists(collection_path):
            ChassisCollectionAPI.post (self)

        if ident in members:
            resp = 404
            return resp
        try:
            global config

            wildcards['id'] = ident
            wildcards['linkSystem'] = ['UpdateWithPATCH']
            wildcards['linkResourceBlocks'] = ['UpdateWithPATCH']
            wildcards['linkMgr'] = 'UpdateWithPATCH'
            wildcards['rb'] = g.rest_base
            config=get_Chassis_instance(wildcards)
            config = create_and_patch_object (config, members, member_ids, path, collection_path)

            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        return resp

    # HTTP PUT
    def put(self, ident):
        path = create_path(self.root, self.chassis, ident, 'index.json')
        put_object(path)
        return self.get(ident)

    # HTTP PATCH
    def patch(self, ident):
        #Set path to object, then call patch_object:
        path = create_path(self.root, self.chassis, ident, 'index.json')
        patch_object(path)
        return self.get(ident)

    # HTTP DELETE
    def delete(self, ident):
        #Set path to object, then call delete_object:
        path = create_path(self.root, self.chassis, ident)
        base_path = create_path(self.root, self.chassis)
        return delete_object(path, base_path)


# Chassis Collection API
class ChassisCollectionAPI(Resource):

    def __init__(self):
        self.root = PATHS['Root']
        self.chassis = PATHS['Chassis']['path']

    def get(self):
        path = os.path.join(self.root, self.chassis, 'index.json')
        return get_json_data (path)

    def verify(self, config):
        # TODO: Implement a method to verify that the POST body is valid
        return True,{}

    # HTTP POST Collection
    def post(self):
        self.root = PATHS['Root']
        self.chassis = PATHS['Chassis']['path']

        path = create_path(self.root, self.chassis)
        return create_collection (path, 'Chassis')

    # HTTP PUT
    def put(self):
        path = os.path.join(self.root, self.chassis, 'index.json')
        put_object(path)
        return self.get(self.root)

    def verify(self, config):
        #TODO: Implement a method to verify that the POST body is valid
        return True,{}

    # HTTP DELETE
    def delete(self):
        #Set path to object, then call delete_object:
        path = create_path(self.root, self.chassis)
        base_path = create_path(self.root)
        return delete_collection(path, base_path)


# CreateChassis
#
# Called internally to create instances of a resource. If the
# resource has subordinate resources, those subordinate resource(s)
# are created automatically.
#
# Note: In 'init', the first time through, kwargs may not have any
# values, so we need to check. The call to 'init' stores the path
# wildcards. The wildcards are used to modify the resource template
# when subsequent calls are made to instantiate resources.
class CreateChassis(Resource):

    def __init__(self, **kwargs):
        logging.info('CreateChassis init called')
        if 'resource_class_kwargs' in kwargs:
            global wildcards
            wildcards = copy.deepcopy(kwargs['resource_class_kwargs'])
        self.root = PATHS['Root']
        self.chassis = PATHS['Chassis']['path']

    # Create instance
    def put(self, ident):
        logging.info('CreateChassis put called')
        try:
            global config
            global wildcards
            wildcards['id'] = ident
            config = get_Chassis_instance(wildcards)
            members[ident] = config
            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        logging.info('CreateChassis init exit')
        return resp
