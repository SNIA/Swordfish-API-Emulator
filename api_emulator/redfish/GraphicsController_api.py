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

# Resource implementation for - /redfish/v1/Systems/{ComputerSystemId}/GraphicsControllers/{ControllerId}
# Program name - GraphicsController_api.py

import g
import json, os
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.GraphicsController import get_GraphicsController_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# GraphicsController Collection API
class GraphicsControllerCollectionAPI(Resource):
	def __init__(self):
		logging.info('GraphicsController Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ComputerSystemId):
		logging.info('GraphicsController Collection get called')
		path = os.path.join(self.root, 'Systems/{0}/GraphicsControllers', 'index.json').format(ComputerSystemId)
		return get_json_data (path)

	# HTTP POST Collection
	def post(self, ComputerSystemId):
		logging.info('GraphicsController Collection post called')

		if ComputerSystemId in members:
			resp = 404
			return resp
		path = create_path(self.root, 'Systems/{0}/GraphicsControllers').format(ComputerSystemId)
		return create_collection (path, 'GraphicsController')

	# HTTP PUT Collection
	def put(self, ComputerSystemId):
		logging.info('GraphicsController Collection put called')

		path = os.path.join(self.root, 'Systems/{0}/GraphicsControllers', 'index.json').format(ComputerSystemId)
		put_object (path)
		return self.get(ComputerSystemId)

# GraphicsController API
class GraphicsControllerAPI(Resource):
	def __init__(self):
		logging.info('GraphicsController init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ComputerSystemId, ControllerId):
		logging.info('GraphicsController get called')
		path = create_path(self.root, 'Systems/{0}/GraphicsControllers/{1}', 'index.json').format(ComputerSystemId, ControllerId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, ComputerSystemId, ControllerId):
		logging.info('GraphicsController post called')
		path = create_path(self.root, 'Systems/{0}/GraphicsControllers/{1}').format(ComputerSystemId, ControllerId)
		collection_path = os.path.join(self.root, 'Systems/{0}/GraphicsControllers', 'index.json').format(ComputerSystemId)

		# Check if collection exists:
		if not os.path.exists(collection_path):
			GraphicsControllerCollectionAPI.post(self, ComputerSystemId)

		if ControllerId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'ComputerSystemId':ComputerSystemId, 'ControllerId':ControllerId, 'rb':g.rest_base}
			config=get_GraphicsController_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('GraphicsControllerAPI POST exit')
		return resp

	# HTTP PUT
	def put(self, ComputerSystemId, ControllerId):
		logging.info('GraphicsController put called')
		path = create_path(self.root, 'Systems/{0}/GraphicsControllers/{1}', 'index.json').format(ComputerSystemId, ControllerId)
		put_object(path)
		return self.get(ComputerSystemId, ControllerId)

	# HTTP PATCH
	def patch(self, ComputerSystemId, ControllerId):
		logging.info('GraphicsController patch called')
		path = create_path(self.root, 'Systems/{0}/GraphicsControllers/{1}', 'index.json').format(ComputerSystemId, ControllerId)
		patch_object(path)
		return self.get(ComputerSystemId, ControllerId)

	# HTTP DELETE
	def delete(self, ComputerSystemId, ControllerId):
		logging.info('GraphicsController delete called')
		path = create_path(self.root, 'Systems/{0}/GraphicsControllers/{1}').format(ComputerSystemId, ControllerId)
		base_path = create_path(self.root, 'Systems/{0}/GraphicsControllers').format(ComputerSystemId)
		return delete_object(path, base_path)

