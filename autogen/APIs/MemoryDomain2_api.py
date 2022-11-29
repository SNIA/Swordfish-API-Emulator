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

# Resource implementation for - /redfish/v1/CompositionService/ResourceBlocks/{ResourceBlockId}/Systems/{ComputerSystemId}/MemoryDomains/{MemoryDomainId}
# Program name - MemoryDomain2_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.MemoryDomain2 import get_MemoryDomain2_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# MemoryDomain2 Collection API
class MemoryDomain2CollectionAPI(Resource):
	def __init__(self):
		logging.info('MemoryDomain2 Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ResourceBlockId, ComputerSystemId):
		logging.info('MemoryDomain2 Collection get called')
		path = os.path.join(self.root, 'CompositionService/ResourceBlocks/{0}/Systems/{1}/MemoryDomains', 'index.json').format(ResourceBlockId, ComputerSystemId)
		return get_json_data (path)

	# HTTP POST Collection
	def post(self, ResourceBlockId, ComputerSystemId):
		logging.info('MemoryDomain2 Collection post called')

		if ComputerSystemId in members:
			resp = 404
			return resp
		path = create_path(self.root, 'CompositionService/ResourceBlocks/{0}/Systems/{1}/MemoryDomains').format(ResourceBlockId, ComputerSystemId)
		if not os.path.exists(path):
			os.mkdir(path)
			create_collection (path, 'MemoryDomain')

		res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
		if request.data:
			config = json.loads(request.data)
			if "@odata.id" in config:
				return MemoryDomain2API.post(self, ResourceBlockId, ComputerSystemId, os.path.basename(config['@odata.id']))
			else:
				return MemoryDomain2API.post(self, ResourceBlockId, ComputerSystemId, str(res))
		else:
			return MemoryDomain2API.post(self, ResourceBlockId, ComputerSystemId, str(res))

	# HTTP PUT Collection
	def put(self, ResourceBlockId, ComputerSystemId):
		logging.info('MemoryDomain2 Collection put called')

		path = os.path.join(self.root, 'CompositionService/ResourceBlocks/{0}/Systems/{1}/MemoryDomains', 'index.json').format(ResourceBlockId, ComputerSystemId)
		put_object (path)
		return self.get(ResourceBlockId)

# MemoryDomain2 API
class MemoryDomain2API(Resource):
	def __init__(self):
		logging.info('MemoryDomain2 init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ResourceBlockId, ComputerSystemId, MemoryDomainId):
		logging.info('MemoryDomain2 get called')
		path = create_path(self.root, 'CompositionService/ResourceBlocks/{0}/Systems/{1}/MemoryDomains/{2}', 'index.json').format(ResourceBlockId, ComputerSystemId, MemoryDomainId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, ResourceBlockId, ComputerSystemId, MemoryDomainId):
		logging.info('MemoryDomain2 post called')
		path = create_path(self.root, 'CompositionService/ResourceBlocks/{0}/Systems/{1}/MemoryDomains/{2}').format(ResourceBlockId, ComputerSystemId, MemoryDomainId)
		collection_path = os.path.join(self.root, 'CompositionService/ResourceBlocks/{0}/Systems/{1}/MemoryDomains', 'index.json').format(ResourceBlockId, ComputerSystemId)

		# Check if collection exists:
		if not os.path.exists(collection_path):
			MemoryDomain2CollectionAPI.post(self, ResourceBlockId, ComputerSystemId)

		if MemoryDomainId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'ResourceBlockId':ResourceBlockId, 'ComputerSystemId':ComputerSystemId, 'MemoryDomainId':MemoryDomainId, 'rb':g.rest_base}
			config=get_MemoryDomain2_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('MemoryDomain2API POST exit')
		return resp

	# HTTP PUT
	def put(self, ResourceBlockId, ComputerSystemId, MemoryDomainId):
		logging.info('MemoryDomain2 put called')
		path = os.path.join(self.root, 'CompositionService/ResourceBlocks/{0}/Systems/{1}/MemoryDomains/{2}', 'index.json').format(ResourceBlockId, ComputerSystemId, MemoryDomainId)
		put_object(path)
		return self.get(ResourceBlockId, ComputerSystemId, MemoryDomainId)

	# HTTP PATCH
	def patch(self, ResourceBlockId, ComputerSystemId, MemoryDomainId):
		logging.info('MemoryDomain2 patch called')
		path = os.path.join(self.root, 'CompositionService/ResourceBlocks/{0}/Systems/{1}/MemoryDomains/{2}', 'index.json').format(ResourceBlockId, ComputerSystemId, MemoryDomainId)
		patch_object(path)
		return self.get(ResourceBlockId, ComputerSystemId, MemoryDomainId)

	# HTTP DELETE
	def delete(self, ResourceBlockId, ComputerSystemId, MemoryDomainId):
		logging.info('MemoryDomain2 delete called')
		path = create_path(self.root, 'CompositionService/ResourceBlocks/{0}/Systems/{1}/MemoryDomains/{2}').format(ResourceBlockId, ComputerSystemId, MemoryDomainId)
		base_path = create_path(self.root, 'CompositionService/ResourceBlocks/{0}/Systems/{1}/MemoryDomains').format(ResourceBlockId, ComputerSystemId)
		return delete_object(path, base_path)

