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

# Resource implementation for - /redfish/v1/ResourceBlocks/{ResourceBlockId}/Processors/{ProcessorId}/AccelerationFunctions/{AccelerationFunctionId}
# Program name - AccelerationFunction3_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.AccelerationFunction3 import get_AccelerationFunction3_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# AccelerationFunction3 Collection API
class AccelerationFunction3CollectionAPI(Resource):
	def __init__(self):
		logging.info('AccelerationFunction3 Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ResourceBlockId, ProcessorId):
		logging.info('AccelerationFunction3 Collection get called')
		path = os.path.join(self.root, 'ResourceBlocks/{0}/Processors/{1}/AccelerationFunctions', 'index.json').format(ResourceBlockId, ProcessorId)
		return get_json_data (path)

	# HTTP POST Collection
	def post(self, ResourceBlockId, ProcessorId):
		logging.info('AccelerationFunction3 Collection post called')

		if ProcessorId in members:
			resp = 404
			return resp
		path = create_path(self.root, 'ResourceBlocks/{0}/Processors/{1}/AccelerationFunctions').format(ResourceBlockId, ProcessorId)
		if not os.path.exists(path):
			os.mkdir(path)
			create_collection (path, 'AccelerationFunction')

		res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
		if request.data:
			config = json.loads(request.data)
			if "@odata.id" in config:
				return AccelerationFunction3API.post(self, os.path.basename(config['@odata.id']))
			else:
				return AccelerationFunction3API.post(self, str(res))
		else:
			return AccelerationFunction3API.post(self, str(res))

	# HTTP PUT Collection
	def put(self, ResourceBlockId, ProcessorId):
		logging.info('AccelerationFunction3 Collection put called')

		path = os.path.join(self.root, 'ResourceBlocks/{0}/Processors/{1}/AccelerationFunctions', 'index.json').format(ResourceBlockId, ProcessorId)
		put_object (path)
		return self.get(ResourceBlockId)

# AccelerationFunction3 API
class AccelerationFunction3API(Resource):
	def __init__(self):
		logging.info('AccelerationFunction3 init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ResourceBlockId, ProcessorId, AccelerationFunctionId):
		logging.info('AccelerationFunction3 get called')
		path = create_path(self.root, 'ResourceBlocks/{0}/Processors/{1}/AccelerationFunctions/{2}', 'index.json').format(ResourceBlockId, ProcessorId, AccelerationFunctionId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, ResourceBlockId, ProcessorId, AccelerationFunctionId):
		logging.info('AccelerationFunction3 post called')
		path = create_path(self.root, 'ResourceBlocks/{0}/Processors/{1}/AccelerationFunctions/{2}').format(ResourceBlockId, ProcessorId, AccelerationFunctionId)
		collection_path = os.path.join(self.root, 'ResourceBlocks/{0}/Processors/{1}/AccelerationFunctions', 'index.json').format(ResourceBlockId, ProcessorId)

		# Check if collection exists:
		if not os.path.exists(collection_path):
			AccelerationFunction3CollectionAPI.post(self, ResourceBlockId, ProcessorId)

		if AccelerationFunctionId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'ResourceBlockId':ResourceBlockId, 'ProcessorId':ProcessorId, 'AccelerationFunctionId':AccelerationFunctionId, 'rb':g.rest_base}
			config=get_AccelerationFunction3_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('AccelerationFunction3API POST exit')
		return resp

	# HTTP PUT
	def put(self, ResourceBlockId, ProcessorId, AccelerationFunctionId):
		logging.info('AccelerationFunction3 put called')
		path = os.path.join(self.root, 'ResourceBlocks/{0}/Processors/{1}/AccelerationFunctions/{2}', 'index.json').format(ResourceBlockId, ProcessorId, AccelerationFunctionId)
		put_object(path)
		return self.get(ResourceBlockId, ProcessorId, AccelerationFunctionId)

	# HTTP PATCH
	def patch(self, ResourceBlockId, ProcessorId, AccelerationFunctionId):
		logging.info('AccelerationFunction3 patch called')
		path = os.path.join(self.root, 'ResourceBlocks/{0}/Processors/{1}/AccelerationFunctions/{2}', 'index.json').format(ResourceBlockId, ProcessorId, AccelerationFunctionId)
		patch_object(path)
		return self.get(ResourceBlockId, ProcessorId, AccelerationFunctionId)

	# HTTP DELETE
	def delete(self, ResourceBlockId, ProcessorId, AccelerationFunctionId):
		logging.info('AccelerationFunction3 delete called')
		path = create_path(self.root, 'ResourceBlocks/{0}/Processors/{1}/AccelerationFunctions/{2}').format(ResourceBlockId, ProcessorId, AccelerationFunctionId)
		base_path = create_path(self.root, 'ResourceBlocks/{0}/Processors/{1}/AccelerationFunctions').format(ResourceBlockId, ProcessorId)
		return delete_object(path, base_path)

