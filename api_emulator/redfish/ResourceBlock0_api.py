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

# Resource implementation for - /redfish/v1/CompositionService/ResourceBlocks/{ResourceBlockId}
# Program name - ResourceBlock0_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.ResourceBlock0 import get_ResourceBlock0_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# ResourceBlock0 Collection API
class ResourceBlock0CollectionAPI(Resource):
	def __init__(self):
		logging.info('ResourceBlock0 Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self):
		logging.info('ResourceBlock0 Collection get called')
		path = os.path.join(self.root, 'CompositionService/ResourceBlocks', 'index.json')
		return get_json_data (path)

	# HTTP POST Collection
	def post(self):
		logging.info('ResourceBlock0 Collection post called')

		path = create_path(self.root, 'CompositionService/ResourceBlocks')
		if not os.path.exists(path):
			os.mkdir(path)
			create_collection (path, 'ResourceBlock')

		res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
		if request.data:
			config = json.loads(request.data)
			if "@odata.id" in config:
				return ResourceBlock0API.post(self, os.path.basename(config['@odata.id']))
			else:
				return ResourceBlock0API.post(self, str(res))
		else:
			return ResourceBlock0API.post(self, str(res))

	# HTTP PUT Collection
	def put(self):
		logging.info('ResourceBlock0 Collection put called')

		path = os.path.join(self.root, 'CompositionService/ResourceBlocks', 'index.json')
		put_object (path)
		return self.get(self.root)

# ResourceBlock0 API
class ResourceBlock0API(Resource):
	def __init__(self):
		logging.info('ResourceBlock0 init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ResourceBlockId):
		logging.info('ResourceBlock0 get called')
		path = create_path(self.root, 'CompositionService/ResourceBlocks/{0}', 'index.json').format(ResourceBlockId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, ResourceBlockId):
		logging.info('ResourceBlock0 post called')
		path = create_path(self.root, 'CompositionService/ResourceBlocks/{0}').format(ResourceBlockId)
		collection_path = os.path.join(self.root, 'CompositionService/ResourceBlocks', 'index.json')

		# Check if collection exists:
		if not os.path.exists(collection_path):
			ResourceBlock0CollectionAPI.post(self)

		if ResourceBlockId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'ResourceBlockId':ResourceBlockId, 'rb':g.rest_base}
			config=get_ResourceBlock0_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('ResourceBlock0API POST exit')
		return resp

	# HTTP PUT
	def put(self, ResourceBlockId):
		logging.info('ResourceBlock0 put called')
		path = os.path.join(self.root, 'CompositionService/ResourceBlocks/{0}', 'index.json').format(ResourceBlockId)
		put_object(path)
		return self.get(ResourceBlockId)

	# HTTP PATCH
	def patch(self, ResourceBlockId):
		logging.info('ResourceBlock0 patch called')
		path = os.path.join(self.root, 'CompositionService/ResourceBlocks/{0}', 'index.json').format(ResourceBlockId)
		patch_object(path)
		return self.get(ResourceBlockId)

	# HTTP DELETE
	def delete(self, ResourceBlockId):
		logging.info('ResourceBlock0 delete called')
		path = create_path(self.root, 'CompositionService/ResourceBlocks/{0}').format(ResourceBlockId)
		base_path = create_path(self.root, 'CompositionService/ResourceBlocks')
		return delete_object(path, base_path)

