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

# Resource implementation for - /redfish/v1/Storage/{StorageId}/StoragePools/{StoragePoolId}/AllocatedPools/{AllocatedPoolId}
# Program name - StoragePool7_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.StoragePool7 import get_StoragePool7_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# StoragePool7 Collection API
class StoragePool7CollectionAPI(Resource):
	def __init__(self):
		logging.info('StoragePool7 Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, StorageId, StoragePoolId):
		logging.info('StoragePool7 Collection get called')
		path = os.path.join(self.root, 'Storage/{0}/StoragePools/{1}/AllocatedPools', 'index.json').format(StorageId, StoragePoolId)
		return get_json_data (path)

	# HTTP POST Collection
	def post(self, StorageId, StoragePoolId):
		logging.info('StoragePool7 Collection post called')

		if StoragePoolId in members:
			resp = 404
			return resp
		path = create_path(self.root, 'Storage/{0}/StoragePools/{1}/AllocatedPools').format(StorageId, StoragePoolId)
		if not os.path.exists(path):
			os.mkdir(path)
			create_collection (path, 'StoragePool')

		res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
		if request.data:
			config = json.loads(request.data)
			if "@odata.id" in config:
				return StoragePool7API.post(self, StorageId, StoragePoolId, os.path.basename(config['@odata.id']))
			else:
				return StoragePool7API.post(self, StorageId, StoragePoolId, str(res))
		else:
			return StoragePool7API.post(self, StorageId, StoragePoolId, str(res))

	# HTTP PUT Collection
	def put(self, StorageId, StoragePoolId):
		logging.info('StoragePool7 Collection put called')

		path = os.path.join(self.root, 'Storage/{0}/StoragePools/{1}/AllocatedPools', 'index.json').format(StorageId, StoragePoolId)
		put_object (path)
		return self.get(StorageId)

# StoragePool7 API
class StoragePool7API(Resource):
	def __init__(self):
		logging.info('StoragePool7 init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, StorageId, StoragePoolId, AllocatedPoolId):
		logging.info('StoragePool7 get called')
		path = create_path(self.root, 'Storage/{0}/StoragePools/{1}/AllocatedPools/{2}', 'index.json').format(StorageId, StoragePoolId, AllocatedPoolId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, StorageId, StoragePoolId, AllocatedPoolId):
		logging.info('StoragePool7 post called')
		path = create_path(self.root, 'Storage/{0}/StoragePools/{1}/AllocatedPools/{2}').format(StorageId, StoragePoolId, AllocatedPoolId)
		collection_path = os.path.join(self.root, 'Storage/{0}/StoragePools/{1}/AllocatedPools', 'index.json').format(StorageId, StoragePoolId)

		# Check if collection exists:
		if not os.path.exists(collection_path):
			StoragePool7CollectionAPI.post(self, StorageId, StoragePoolId)

		if AllocatedPoolId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'StorageId':StorageId, 'StoragePoolId':StoragePoolId, 'AllocatedPoolId':AllocatedPoolId, 'rb':g.rest_base}
			config=get_StoragePool7_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('StoragePool7API POST exit')
		return resp

	# HTTP PUT
	def put(self, StorageId, StoragePoolId, AllocatedPoolId):
		logging.info('StoragePool7 put called')
		path = os.path.join(self.root, 'Storage/{0}/StoragePools/{1}/AllocatedPools/{2}', 'index.json').format(StorageId, StoragePoolId, AllocatedPoolId)
		put_object(path)
		return self.get(StorageId, StoragePoolId, AllocatedPoolId)

	# HTTP PATCH
	def patch(self, StorageId, StoragePoolId, AllocatedPoolId):
		logging.info('StoragePool7 patch called')
		path = os.path.join(self.root, 'Storage/{0}/StoragePools/{1}/AllocatedPools/{2}', 'index.json').format(StorageId, StoragePoolId, AllocatedPoolId)
		patch_object(path)
		return self.get(StorageId, StoragePoolId, AllocatedPoolId)

	# HTTP DELETE
	def delete(self, StorageId, StoragePoolId, AllocatedPoolId):
		logging.info('StoragePool7 delete called')
		path = create_path(self.root, 'Storage/{0}/StoragePools/{1}/AllocatedPools/{2}').format(StorageId, StoragePoolId, AllocatedPoolId)
		base_path = create_path(self.root, 'Storage/{0}/StoragePools/{1}/AllocatedPools').format(StorageId, StoragePoolId)
		return delete_object(path, base_path)

