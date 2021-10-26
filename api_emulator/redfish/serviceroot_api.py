#
# Copyright (c) 2017-2021, The ServiceRoot Networking Industry Association.
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
# Neither the name of The ServiceRoot Networking Industry Association (SNIA) nor
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
# serviceroot_api.py


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
from .templates.ServiceRoot import get_ServiceRoot_instance

members =[]
member_ids = []
config = {}
INTERNAL_ERROR = 500

# ServiceRootAPI
class ServiceRootAPI(Resource):
    def __init__(self, **kwargs):
        logging.info('ServiceRootAPI init called')
        self.root = PATHS['Root']

    # HTTP GET
    def get(self):
        path = create_path('Resources/', 'index.json')
        return get_json_data (path)

    # HTTP POST
    # - Create the resource (since URI variables are available)
    # - Update the members and members.id lists
    # - Attach the APIs of subordinate resources (do this only once)
    # - Finally, create an instance of the subordinate resources
    def post(self):
        logging.info('ServiceRootAPI POST called')
        path = create_path(self.root)
        collection_path = os.path.join(self.root, 'index.json')
        # Check if collection exists:
        if not os.path.exists(collection_path):
            ServiceRootCollectionAPI.post (self)

        if serviceroot in members:
            resp = 404
            return resp
        try:
            global config
            wildcards = {'rb': g.rest_base}
            config=get_ServiceRoot_instance(wildcards)

            config = create_and_patch_object (config, members, member_ids, path, collection_path)

            #Add default placeholder collections to instance.
            ## TBD

            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        logging.info('ServiceRootAPI POST exit')
        return resp

    # HTTP PUT
    def put(self):
        path = create_path(self.root, 'index.json')
        put_object(path)
        return self.get()

	# HTTP PATCH
    def patch(self):
        #Set path to object, then call patch_object:
        path = create_path(self.root, 'index.json')
        patch_object(path)
        return self.get()
