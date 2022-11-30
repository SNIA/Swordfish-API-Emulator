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

# Resource implementation for - /redfish/v1/RegisteredClients/{RegisteredClientId}
# Program name - RegisteredClient_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.RegisteredClient import get_RegisteredClient_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# RegisteredClient Collection API
class RegisteredClientCollectionAPI(Resource):
	def __init__(self):
		logging.info('RegisteredClient Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self):
		logging.info('RegisteredClient Collection get called')
		path = os.path.join(self.root, 'RegisteredClients', 'index.json')
		return get_json_data (path)

	# HTTP POST Collection
	def post(self):
		logging.info('RegisteredClient Collection post called')

		if request.data:
			config = json.loads(request.data)
			if "@odata.type" in config:
				if "Collection" in config["@odata.type"]:
					return "Invalid data in POST body", 400

		path = create_path(self.root, 'RegisteredClients')
		parent_path = os.path.dirname(path)
		if not os.path.exists(path):
			os.mkdir(path)
			create_collection (path, 'RegisteredClient', parent_path)

		res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
		if request.data:
			config = json.loads(request.data)
			if "@odata.id" in config:
				return RegisteredClientAPI.post(self, os.path.basename(config['@odata.id']))
			else:
				return RegisteredClientAPI.post(self, str(res))
		else:
			return RegisteredClientAPI.post(self, str(res))

	# HTTP PUT Collection
	def put(self):
		logging.info('RegisteredClient Collection put called')

		path = os.path.join(self.root, 'RegisteredClients', 'index.json')
		put_object (path)
		return self.get(self.root)

# RegisteredClient API
class RegisteredClientAPI(Resource):
	def __init__(self):
		logging.info('RegisteredClient init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, RegisteredClientId):
		logging.info('RegisteredClient get called')
		path = create_path(self.root, 'RegisteredClients/{0}', 'index.json').format(RegisteredClientId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, RegisteredClientId):
		logging.info('RegisteredClient post called')
		path = create_path(self.root, 'RegisteredClients/{0}').format(RegisteredClientId)
		collection_path = os.path.join(self.root, 'RegisteredClients', 'index.json')

		# Check if collection exists:
		if not os.path.exists(collection_path):
			RegisteredClientCollectionAPI.post(self)

		if RegisteredClientId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'RegisteredClientId':RegisteredClientId, 'rb':g.rest_base}
			config=get_RegisteredClient_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('RegisteredClientAPI POST exit')
		return resp

	# HTTP PUT
	def put(self, RegisteredClientId):
		logging.info('RegisteredClient put called')
		path = os.path.join(self.root, 'RegisteredClients/{0}', 'index.json').format(RegisteredClientId)
		put_object(path)
		return self.get(RegisteredClientId)

	# HTTP PATCH
	def patch(self, RegisteredClientId):
		logging.info('RegisteredClient patch called')
		path = os.path.join(self.root, 'RegisteredClients/{0}', 'index.json').format(RegisteredClientId)
		patch_object(path)
		return self.get(RegisteredClientId)

	# HTTP DELETE
	def delete(self, RegisteredClientId):
		logging.info('RegisteredClient delete called')
		path = create_path(self.root, 'RegisteredClients/{0}').format(RegisteredClientId)
		base_path = create_path(self.root, 'RegisteredClients')
		return delete_object(path, base_path)

