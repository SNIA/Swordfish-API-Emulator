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

# Resource implementation for - /redfish/v1/ResourceBlocks/{ResourceBlockId}/Systems/{ComputerSystemId}/Storage/{StorageId}
# Program name - Storage5_api.py

import g
import json, os
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.Storage5 import get_Storage5_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# Storage5 Collection API
class Storage5CollectionAPI(Resource):
	def __init__(self):
		logging.info('Storage5 Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ResourceBlockId, ComputerSystemId):
		logging.info('Storage5 Collection get called')
		path = os.path.join(self.root, 'ResourceBlocks/{0}/Systems/{1}/Storage', 'index.json').format(ResourceBlockId, ComputerSystemId)
		return get_json_data (path)

	# HTTP POST Collection
	def post(self, ResourceBlockId, ComputerSystemId):
		logging.info('Storage5 Collection post called')

		if ComputerSystemId in members:
			resp = 404
			return resp
		path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/Storage').format(ResourceBlockId, ComputerSystemId)
		return create_collection (path, 'Storage')

	# HTTP PUT Collection
	def put(self, ResourceBlockId, ComputerSystemId):
		path = os.path.join(self.root, 'ResourceBlocks/{0}/Systems/{1}/Storage', 'index.json').format(ResourceBlockId, ComputerSystemId)
		put_object (path)
		return self.get(ResourceBlockId)

# Storage5 API
class Storage5API(Resource):
	def __init__(self):
		logging.info('Storage5 init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ResourceBlockId, ComputerSystemId, StorageId):
		logging.info('Storage5 get called')
		path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/Storage/{2}', 'index.json').format(ResourceBlockId, ComputerSystemId, StorageId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, ResourceBlockId, ComputerSystemId, StorageId):
		logging.info('Storage5 post called')
		path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/Storage/{2}').format(ResourceBlockId, ComputerSystemId, StorageId)
		collection_path = os.path.join(self.root, 'ResourceBlocks/{0}/Systems/{1}/Storage', 'index.json').format(ResourceBlockId, ComputerSystemId)

		# Check if collection exists:
		if not os.path.exists(collection_path):
			Storage5CollectionAPI.post(self, ResourceBlockId, ComputerSystemId)

		if StorageId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'ResourceBlockId':ResourceBlockId, 'ComputerSystemId':ComputerSystemId, 'StorageId':StorageId, 'rb':g.rest_base}
			config=get_Storage5_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('Storage5API POST exit')
		return resp

	# HTTP PUT
	def put(self, ResourceBlockId, ComputerSystemId, StorageId):
		logging.info('Storage5 put called')
		path = os.path.join(self.root, 'ResourceBlocks/{0}/Systems/{1}/Storage/{2}', 'index.json').format(ResourceBlockId, ComputerSystemId, StorageId)
		put_object(path)
		return self.get(ResourceBlockId, ComputerSystemId, StorageId)

	# HTTP PATCH
	def patch(self, ResourceBlockId, ComputerSystemId, StorageId):
		logging.info('Storage5 patch called')
		path = os.path.join(self.root, 'ResourceBlocks/{0}/Systems/{1}/Storage/{2}', 'index.json').format(ResourceBlockId, ComputerSystemId, StorageId)
		patch_object(path)
		return self.get(ResourceBlockId, ComputerSystemId, StorageId)

	# HTTP DELETE
	def delete(self, ResourceBlockId, ComputerSystemId, StorageId):
		logging.info('Storage5 delete called')
		path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/Storage/{2}').format(ResourceBlockId, ComputerSystemId, StorageId)
		base_path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/Storage').format(ResourceBlockId, ComputerSystemId)
		return delete_object(path, base_path)
