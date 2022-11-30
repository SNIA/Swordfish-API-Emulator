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

# Resource implementation for - /redfish/v1/Storage/{StorageId}/StoragePools/{StoragePoolId}/CapacitySources/{CapacitySourceId}/ProvidingVolumes/{VolumeId}
# Program name - Volume7_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.Volume7 import get_Volume7_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# Volume7 Collection API
class Volume7CollectionAPI(Resource):
	def __init__(self):
		logging.info('Volume7 Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, StorageId, StoragePoolId, CapacitySourceId):
		logging.info('Volume7 Collection get called')
		path = os.path.join(self.root, 'Storage/{0}/StoragePools/{1}/CapacitySources/{2}/ProvidingVolumes', 'index.json').format(StorageId, StoragePoolId, CapacitySourceId)
		return get_json_data (path)

	# HTTP POST Collection
	def post(self, StorageId, StoragePoolId, CapacitySourceId):
		logging.info('Volume7 Collection post called')

		if request.data:
			config = json.loads(request.data)
			if "@odata.type" in config:
				if "Collection" in config["@odata.type"]:
					return "Invalid data in POST body", 400

		if CapacitySourceId in members:
			resp = 404
			return resp
		path = create_path(self.root, 'Storage/{0}/StoragePools/{1}/CapacitySources/{2}/ProvidingVolumes').format(StorageId, StoragePoolId, CapacitySourceId)
		parent_path = os.path.dirname(path)
		if not os.path.exists(path):
			os.mkdir(path)
			create_collection (path, 'Volume', parent_path)

		res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
		if request.data:
			config = json.loads(request.data)
			if "@odata.id" in config:
				return Volume7API.post(self, StorageId, StoragePoolId, CapacitySourceId, os.path.basename(config['@odata.id']))
			else:
				return Volume7API.post(self, StorageId, StoragePoolId, CapacitySourceId, str(res))
		else:
			return Volume7API.post(self, StorageId, StoragePoolId, CapacitySourceId, str(res))

	# HTTP PUT Collection
	def put(self, StorageId, StoragePoolId, CapacitySourceId):
		logging.info('Volume7 Collection put called')

		path = os.path.join(self.root, 'Storage/{0}/StoragePools/{1}/CapacitySources/{2}/ProvidingVolumes', 'index.json').format(StorageId, StoragePoolId, CapacitySourceId)
		put_object (path)
		return self.get(StorageId)

# Volume7 API
class Volume7API(Resource):
	def __init__(self):
		logging.info('Volume7 init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, StorageId, StoragePoolId, CapacitySourceId, VolumeId):
		logging.info('Volume7 get called')
		path = create_path(self.root, 'Storage/{0}/StoragePools/{1}/CapacitySources/{2}/ProvidingVolumes/{3}', 'index.json').format(StorageId, StoragePoolId, CapacitySourceId, VolumeId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, StorageId, StoragePoolId, CapacitySourceId, VolumeId):
		logging.info('Volume7 post called')
		path = create_path(self.root, 'Storage/{0}/StoragePools/{1}/CapacitySources/{2}/ProvidingVolumes/{3}').format(StorageId, StoragePoolId, CapacitySourceId, VolumeId)
		collection_path = os.path.join(self.root, 'Storage/{0}/StoragePools/{1}/CapacitySources/{2}/ProvidingVolumes', 'index.json').format(StorageId, StoragePoolId, CapacitySourceId)

		# Check if collection exists:
		if not os.path.exists(collection_path):
			Volume7CollectionAPI.post(self, StorageId, StoragePoolId, CapacitySourceId)

		if VolumeId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'StorageId':StorageId, 'StoragePoolId':StoragePoolId, 'CapacitySourceId':CapacitySourceId, 'VolumeId':VolumeId, 'rb':g.rest_base}
			config=get_Volume7_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('Volume7API POST exit')
		return resp

	# HTTP PUT
	def put(self, StorageId, StoragePoolId, CapacitySourceId, VolumeId):
		logging.info('Volume7 put called')
		path = os.path.join(self.root, 'Storage/{0}/StoragePools/{1}/CapacitySources/{2}/ProvidingVolumes/{3}', 'index.json').format(StorageId, StoragePoolId, CapacitySourceId, VolumeId)
		put_object(path)
		return self.get(StorageId, StoragePoolId, CapacitySourceId, VolumeId)

	# HTTP PATCH
	def patch(self, StorageId, StoragePoolId, CapacitySourceId, VolumeId):
		logging.info('Volume7 patch called')
		path = os.path.join(self.root, 'Storage/{0}/StoragePools/{1}/CapacitySources/{2}/ProvidingVolumes/{3}', 'index.json').format(StorageId, StoragePoolId, CapacitySourceId, VolumeId)
		patch_object(path)
		return self.get(StorageId, StoragePoolId, CapacitySourceId, VolumeId)

	# HTTP DELETE
	def delete(self, StorageId, StoragePoolId, CapacitySourceId, VolumeId):
		logging.info('Volume7 delete called')
		path = create_path(self.root, 'Storage/{0}/StoragePools/{1}/CapacitySources/{2}/ProvidingVolumes/{3}').format(StorageId, StoragePoolId, CapacitySourceId, VolumeId)
		base_path = create_path(self.root, 'Storage/{0}/StoragePools/{1}/CapacitySources/{2}/ProvidingVolumes').format(StorageId, StoragePoolId, CapacitySourceId)
		return delete_object(path, base_path)

