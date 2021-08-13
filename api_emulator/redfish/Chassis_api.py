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
Collection API:  GET, POST
Singleton  API:  GET, POST, PATCH, DELETE
"""

import g

import json, os
import sys, traceback
import logging
import copy

from flask import jsonify
from flask import Flask, request, make_response, render_template
from flask_restful import reqparse, Api, Resource
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, patch_object, create_collection

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

    # HTTP PUT
    def put(self, ident):
        logging.info('ChassisAPI PUT called')
        return 'PUT is not a supported command for ChassisAPI', 405

    # HTTP POST
    # This is an emulator-only POST command that creates new resource
    # instances from a predefined template. The new instance is given
    # the identifier "ident", which is taken from the end of the URL.
    # PATCH commands can then be used to update the new instance.
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

    # HTTP PATCH
    def patch(self, ident):
        logging.info('ChassisAPI PATCH called')
        raw_dict = request.get_json(force=True)
        try:
            # Update specific portions of the identified object
            for key, value in raw_dict.items():
                members[ident][key] = value
            resp = members[ident], 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        return resp

    # HTTP DELETE
    def delete(self, ident):
        logging.info('ChassisAPI DELETE called')
        try:
            # Find the entry with the correct value for Id
            resp = 404
            if ident in members:
                del(members[ident])
                resp = 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        return resp


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

    # HTTP PUT
    def put(self):
        logging.info('ChassisCollectionAPI PUT called')
        return 'PUT is not a supported command for ChassisCollectionAPI', 405

    def verify(self, config):
        #TODO: Implement a method to verify that the POST body is valid
        return True,{}

    # HTTP POST
    # POST should allow adding multiple instances to a collection.
    # For now, this only adds one instance.
    # TODO: 'id' should be obtained from the request data.
    def post(self):
        path = create_path(self.root, self.chassis)
        return create_collection (path, 'Chassis')

    # HTTP PATCH
    def patch(self):
        logging.info('ChassisCollectionAPI PATCH called')
        return 'PATCH is not a supported command for ChassisCollectionAPI', 405

    # HTTP DELETE
    def delete(self):
        logging.info('ChassisCollectionAPI DELETE called')
        return 'DELETE is not a supported command for ChassisCollectionAPI', 405


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
        self.fabrics = PATHS['Fabrics']['path']

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
