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

# Resource implementation for - /redfish/v1/Systems/{ComputerSystemId}/MemoryDomains/{MemoryDomainId}/MemoryChunks/{MemoryChunksId}
# Program name - MemoryChunks0_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.MemoryChunks0 import get_MemoryChunks0_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# MemoryChunks0 Collection API
class MemoryChunks0CollectionAPI(Resource):
	def __init__(self):
		logging.info('MemoryChunks0 Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ComputerSystemId, MemoryDomainId):
		logging.info('MemoryChunks0 Collection get called')
		path = os.path.join(self.root, 'Systems/{0}/MemoryDomains/{1}/MemoryChunks', 'index.json').format(ComputerSystemId, MemoryDomainId)
		return get_json_data (path)

	# HTTP POST Collection
	def post(self, ComputerSystemId, MemoryDomainId):
		logging.info('MemoryChunks0 Collection post called')

		if MemoryDomainId in members:
			resp = 404
			return resp
		path = create_path(self.root, 'Systems/{0}/MemoryDomains/{1}/MemoryChunks').format(ComputerSystemId, MemoryDomainId)
		if not os.path.exists(path):
			os.mkdir(path)
			create_collection (path, 'MemoryChunks')

		res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
		if request.data:
			config = json.loads(request.data)
			if "@odata.id" in config:
				return MemoryChunks0API.post(self, ComputerSystemId, MemoryDomainId, os.path.basename(config['@odata.id']))
			else:
				return MemoryChunks0API.post(self, ComputerSystemId, MemoryDomainId, str(res))
		else:
			return MemoryChunks0API.post(self, ComputerSystemId, MemoryDomainId, str(res))

	# HTTP PUT Collection
	def put(self, ComputerSystemId, MemoryDomainId):
		logging.info('MemoryChunks0 Collection put called')

		path = os.path.join(self.root, 'Systems/{0}/MemoryDomains/{1}/MemoryChunks', 'index.json').format(ComputerSystemId, MemoryDomainId)
		put_object (path)
		return self.get(ComputerSystemId)

# MemoryChunks0 API
class MemoryChunks0API(Resource):
	def __init__(self):
		logging.info('MemoryChunks0 init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ComputerSystemId, MemoryDomainId, MemoryChunksId):
		logging.info('MemoryChunks0 get called')
		path = create_path(self.root, 'Systems/{0}/MemoryDomains/{1}/MemoryChunks/{2}', 'index.json').format(ComputerSystemId, MemoryDomainId, MemoryChunksId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, ComputerSystemId, MemoryDomainId, MemoryChunksId):
		logging.info('MemoryChunks0 post called')
		path = create_path(self.root, 'Systems/{0}/MemoryDomains/{1}/MemoryChunks/{2}').format(ComputerSystemId, MemoryDomainId, MemoryChunksId)
		collection_path = os.path.join(self.root, 'Systems/{0}/MemoryDomains/{1}/MemoryChunks', 'index.json').format(ComputerSystemId, MemoryDomainId)

		# Check if collection exists:
		if not os.path.exists(collection_path):
			MemoryChunks0CollectionAPI.post(self, ComputerSystemId, MemoryDomainId)

		if MemoryChunksId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'ComputerSystemId':ComputerSystemId, 'MemoryDomainId':MemoryDomainId, 'MemoryChunksId':MemoryChunksId, 'rb':g.rest_base}
			config=get_MemoryChunks0_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('MemoryChunks0API POST exit')
		return resp

	# HTTP PUT
	def put(self, ComputerSystemId, MemoryDomainId, MemoryChunksId):
		logging.info('MemoryChunks0 put called')
		path = os.path.join(self.root, 'Systems/{0}/MemoryDomains/{1}/MemoryChunks/{2}', 'index.json').format(ComputerSystemId, MemoryDomainId, MemoryChunksId)
		put_object(path)
		return self.get(ComputerSystemId, MemoryDomainId, MemoryChunksId)

	# HTTP PATCH
	def patch(self, ComputerSystemId, MemoryDomainId, MemoryChunksId):
		logging.info('MemoryChunks0 patch called')
		path = os.path.join(self.root, 'Systems/{0}/MemoryDomains/{1}/MemoryChunks/{2}', 'index.json').format(ComputerSystemId, MemoryDomainId, MemoryChunksId)
		patch_object(path)
		return self.get(ComputerSystemId, MemoryDomainId, MemoryChunksId)

	# HTTP DELETE
	def delete(self, ComputerSystemId, MemoryDomainId, MemoryChunksId):
		logging.info('MemoryChunks0 delete called')
		path = create_path(self.root, 'Systems/{0}/MemoryDomains/{1}/MemoryChunks/{2}').format(ComputerSystemId, MemoryDomainId, MemoryChunksId)
		base_path = create_path(self.root, 'Systems/{0}/MemoryDomains/{1}/MemoryChunks').format(ComputerSystemId, MemoryDomainId)
		return delete_object(path, base_path)

