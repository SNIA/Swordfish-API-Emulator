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
#f_endpointgroups_api.py

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
from .templates.endpointgroups import get_EndpointGroups_instance

members =[]
member_ids = []
config = {}
INTERNAL_ERROR = 500

# FabricsEndpointGroupsAPI API
class FabricsEndpointGroupsAPI(Resource):
    def __init__(self, **kwargs):
        logging.info('FabricsEndpointGroupsAPI init called')
        self.root = PATHS['Root']
        self.fabrics = PATHS['Fabrics']['path']
        self.f_endpointgroups = PATHS['Fabrics']['f_endpointgroup']

    # HTTP GET
    def get(self, fabric, f_endpointgroup):
        path = create_path(self.root, self.fabrics, fabric, self.f_endpointgroups, f_endpointgroup, 'index.json')
        return get_json_data (path)

    # HTTP POST
    # - Create the resource (since URI variables are available)
    # - Update the members and members.id lists
    # - Attach the APIs of subordinate resources (do this only once)
    # - Finally, create an instance of the subordiante resources
    def post(self, fabric, f_endpointgroup):
        logging.info('FabricsEndpointGroupsAPI POST called')
        path = create_path(self.root, self.fabrics, fabric, self.f_endpointgroups, f_endpointgroup)
        collection_path = os.path.join(self.root, self.fabrics, fabric, self.f_endpointgroups, 'index.json')

        # Check if collection exists:
        if not os.path.exists(collection_path):
            FabricsEndpointGroupsCollectionAPI.post (self, fabric)

        if f_endpointgroup in members:
            resp = 404
            return resp
        try:
            global config
            wildcards = {'f_id':fabric, 'eg_id': f_endpointgroup, 'rb': g.rest_base}
            config=get_EndpointGroups_instance(wildcards)
            config = create_and_patch_object (config, members, member_ids, path, collection_path)
            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        logging.info('FabricsEndpointGroupsAPI POST exit')
        return resp

	# HTTP PATCH
    def patch(self, fabric, f_endpointgroup):
        path = os.path.join(self.root, self.fabrics, fabric, self.f_endpointgroups, f_endpointgroup, 'index.json')
        patch_object(path)
        return self.get(fabric, f_endpointgroup)

    # HTTP PUT
    def put(self, fabric, f_endpointgroup):
        path = os.path.join(self.root, self.fabrics, fabric, self.f_endpointgroups, f_endpointgroup, 'index.json')
        put_object(path)
        return self.get(fabric, f_endpointgroup)

    # HTTP DELETE
    def delete(self, fabric, f_endpointgroup):
        #Set path to object, then call delete_object:
        path = create_path(self.root, self.fabrics, fabric, self.f_endpointgroups, f_endpointgroup)
        base_path = create_path(self.root, self.fabrics, fabric, self.f_endpointgroups)
        return delete_object(path, base_path)


# Fabrics EndpointGroups Collection API
class FabricsEndpointGroupsCollectionAPI(Resource):

    def __init__(self):
        self.root = PATHS['Root']
        self.fabrics = PATHS['Fabrics']['path']
        self.f_endpointgroups = PATHS['Fabrics']['f_endpointgroup']

    def get(self, fabric):
        path = os.path.join(self.root, self.fabrics, fabric, self.f_endpointgroups, 'index.json')
        return get_json_data (path)

    def verify(self, config):
        # TODO: Implement a method to verify that the POST body is valid
        return True,{}

    # HTTP POST Collection
    def post(self, fabric):
        self.root = PATHS['Root']
        self.fabrics = PATHS['Fabrics']['path']
        self.f_endpointgroups = PATHS['Fabrics']['f_endpointgroup']

        logging.info('FabricsEndpointGroupsCollectionAPI POST called')

        if fabric in members:
            resp = 404
            return resp

        path = create_path(self.root, self.fabrics, fabric, self.f_endpointgroups)
        return create_collection (path, 'EndpointGroup')

    # HTTP PUT
    def put(self, fabric):
        path = os.path.join(self.root, self.fabrics, fabric, self.f_endpointgroups, 'index.json')
        put_object(path)
        return self.get(fabric)

    # HTTP DELETE
    def delete(self, fabric):
        #Set path to object, then call delete_object:
        path = create_path(self.root, self.fabrics, fabric, self.f_endpointgroups)
        base_path = create_path(self.root, self.fabrics, fabric)
        return delete_collection(path, base_path)
