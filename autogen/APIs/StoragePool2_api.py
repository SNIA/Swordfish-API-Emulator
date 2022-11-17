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

# Resource implementation for - /redfish/v1/StorageServices/{StorageServiceId}/StoragePools/{StoragePoolId}/CapacitySources/{CapacitySourceId}/ProvidingPools/{ProvidingPoolId}
# Program name - StoragePool2_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.StoragePool2 import get_StoragePool2_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# StoragePool2 Collection API
class StoragePool2CollectionAPI(Resource):
	def __init__(self):
		logging.info('StoragePool2 Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, StorageServiceId, StoragePoolId, CapacitySourceId):
		logging.info('StoragePool2 Collection get called')
		path = os.path.join(self.root, 'StorageServices/{0}/StoragePools/{1}/CapacitySources/{2}/ProvidingPools', 'index.json').format(StorageServiceId, StoragePoolId, CapacitySourceId)
		return get_json_data (path)

	# HTTP POST Collection
	def post(self, StorageServiceId, StoragePoolId, CapacitySourceId):
		logging.info('StoragePool2 Collection post called')

		if CapacitySourceId in members:
			resp = 404
			return resp
		path = create_path(self.root, 'StorageServices/{0}/StoragePools/{1}/CapacitySources/{2}/ProvidingPools').format(StorageServiceId, StoragePoolId, CapacitySourceId)
		if not os.path.exists(path):
			os.mkdir(path)
			create_collection (path, 'StoragePool')

		res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
		if request.data:
			config = json.loads(request.data)
			if "@odata.id" in config:
				return StoragePool2API.post(self, os.path.basename(config['@odata.id']))
			else:
				return StoragePool2API.post(self, str(res))
		else:
			return StoragePool2API.post(self, str(res))

	# HTTP PUT Collection
	def put(self, StorageServiceId, StoragePoolId, CapacitySourceId):
		logging.info('StoragePool2 Collection put called')

		path = os.path.join(self.root, 'StorageServices/{0}/StoragePools/{1}/CapacitySources/{2}/ProvidingPools', 'index.json').format(StorageServiceId, StoragePoolId, CapacitySourceId)
		put_object (path)
		return self.get(StorageServiceId)

# StoragePool2 API
class StoragePool2API(Resource):
	def __init__(self):
		logging.info('StoragePool2 init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, StorageServiceId, StoragePoolId, CapacitySourceId, ProvidingPoolId):
		logging.info('StoragePool2 get called')
		path = create_path(self.root, 'StorageServices/{0}/StoragePools/{1}/CapacitySources/{2}/ProvidingPools/{3}', 'index.json').format(StorageServiceId, StoragePoolId, CapacitySourceId, ProvidingPoolId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, StorageServiceId, StoragePoolId, CapacitySourceId, ProvidingPoolId):
		logging.info('StoragePool2 post called')
		path = create_path(self.root, 'StorageServices/{0}/StoragePools/{1}/CapacitySources/{2}/ProvidingPools/{3}').format(StorageServiceId, StoragePoolId, CapacitySourceId, ProvidingPoolId)
		collection_path = os.path.join(self.root, 'StorageServices/{0}/StoragePools/{1}/CapacitySources/{2}/ProvidingPools', 'index.json').format(StorageServiceId, StoragePoolId, CapacitySourceId)

		# Check if collection exists:
		if not os.path.exists(collection_path):
			StoragePool2CollectionAPI.post(self, StorageServiceId, StoragePoolId, CapacitySourceId)

		if ProvidingPoolId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'StorageServiceId':StorageServiceId, 'StoragePoolId':StoragePoolId, 'CapacitySourceId':CapacitySourceId, 'ProvidingPoolId':ProvidingPoolId, 'rb':g.rest_base}
			config=get_StoragePool2_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('StoragePool2API POST exit')
		return resp

	# HTTP PUT
	def put(self, StorageServiceId, StoragePoolId, CapacitySourceId, ProvidingPoolId):
		logging.info('StoragePool2 put called')
		path = os.path.join(self.root, 'StorageServices/{0}/StoragePools/{1}/CapacitySources/{2}/ProvidingPools/{3}', 'index.json').format(StorageServiceId, StoragePoolId, CapacitySourceId, ProvidingPoolId)
		put_object(path)
		return self.get(StorageServiceId, StoragePoolId, CapacitySourceId, ProvidingPoolId)

	# HTTP PATCH
	def patch(self, StorageServiceId, StoragePoolId, CapacitySourceId, ProvidingPoolId):
		logging.info('StoragePool2 patch called')
		path = os.path.join(self.root, 'StorageServices/{0}/StoragePools/{1}/CapacitySources/{2}/ProvidingPools/{3}', 'index.json').format(StorageServiceId, StoragePoolId, CapacitySourceId, ProvidingPoolId)
		patch_object(path)
		return self.get(StorageServiceId, StoragePoolId, CapacitySourceId, ProvidingPoolId)

	# HTTP DELETE
	def delete(self, StorageServiceId, StoragePoolId, CapacitySourceId, ProvidingPoolId):
		logging.info('StoragePool2 delete called')
		path = create_path(self.root, 'StorageServices/{0}/StoragePools/{1}/CapacitySources/{2}/ProvidingPools/{3}').format(StorageServiceId, StoragePoolId, CapacitySourceId, ProvidingPoolId)
		base_path = create_path(self.root, 'StorageServices/{0}/StoragePools/{1}/CapacitySources/{2}/ProvidingPools').format(StorageServiceId, StoragePoolId, CapacitySourceId)
		return delete_object(path, base_path)
