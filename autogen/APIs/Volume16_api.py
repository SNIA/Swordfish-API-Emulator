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

# Resource implementation for - /redfish/v1/StorageServices/{StorageServiceId}/StoragePools/{StoragePoolId}/AllocatedVolumes/{VolumeId}
# Program name - Volume16_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.Volume16 import get_Volume16_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# Volume16 Collection API
class Volume16CollectionAPI(Resource):
	def __init__(self):
		logging.info('Volume16 Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, StorageServiceId, StoragePoolId):
		logging.info('Volume16 Collection get called')
		path = os.path.join(self.root, 'StorageServices/{0}/StoragePools/{1}/AllocatedVolumes', 'index.json').format(StorageServiceId, StoragePoolId)
		return get_json_data (path)

	# HTTP POST Collection
	def post(self, StorageServiceId, StoragePoolId):
		logging.info('Volume16 Collection post called')

		if StoragePoolId in members:
			resp = 404
			return resp
		path = create_path(self.root, 'StorageServices/{0}/StoragePools/{1}/AllocatedVolumes').format(StorageServiceId, StoragePoolId)
		if not os.path.exists(path):
			os.mkdir(path)
			create_collection (path, 'Volume')

		res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
		if request.data:
			config = json.loads(request.data)
			if "@odata.id" in config:
				return Volume16API.post(self, os.path.basename(config['@odata.id']))
			else:
				return Volume16API.post(self, str(res))
		else:
			return Volume16API.post(self, str(res))

	# HTTP PUT Collection
	def put(self, StorageServiceId, StoragePoolId):
		logging.info('Volume16 Collection put called')

		path = os.path.join(self.root, 'StorageServices/{0}/StoragePools/{1}/AllocatedVolumes', 'index.json').format(StorageServiceId, StoragePoolId)
		put_object (path)
		return self.get(StorageServiceId)

# Volume16 API
class Volume16API(Resource):
	def __init__(self):
		logging.info('Volume16 init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, StorageServiceId, StoragePoolId, VolumeId):
		logging.info('Volume16 get called')
		path = create_path(self.root, 'StorageServices/{0}/StoragePools/{1}/AllocatedVolumes/{2}', 'index.json').format(StorageServiceId, StoragePoolId, VolumeId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, StorageServiceId, StoragePoolId, VolumeId):
		logging.info('Volume16 post called')
		path = create_path(self.root, 'StorageServices/{0}/StoragePools/{1}/AllocatedVolumes/{2}').format(StorageServiceId, StoragePoolId, VolumeId)
		collection_path = os.path.join(self.root, 'StorageServices/{0}/StoragePools/{1}/AllocatedVolumes', 'index.json').format(StorageServiceId, StoragePoolId)

		# Check if collection exists:
		if not os.path.exists(collection_path):
			Volume16CollectionAPI.post(self, StorageServiceId, StoragePoolId)

		if VolumeId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'StorageServiceId':StorageServiceId, 'StoragePoolId':StoragePoolId, 'VolumeId':VolumeId, 'rb':g.rest_base}
			config=get_Volume16_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('Volume16API POST exit')
		return resp

	# HTTP PUT
	def put(self, StorageServiceId, StoragePoolId, VolumeId):
		logging.info('Volume16 put called')
		path = os.path.join(self.root, 'StorageServices/{0}/StoragePools/{1}/AllocatedVolumes/{2}', 'index.json').format(StorageServiceId, StoragePoolId, VolumeId)
		put_object(path)
		return self.get(StorageServiceId, StoragePoolId, VolumeId)

	# HTTP PATCH
	def patch(self, StorageServiceId, StoragePoolId, VolumeId):
		logging.info('Volume16 patch called')
		path = os.path.join(self.root, 'StorageServices/{0}/StoragePools/{1}/AllocatedVolumes/{2}', 'index.json').format(StorageServiceId, StoragePoolId, VolumeId)
		patch_object(path)
		return self.get(StorageServiceId, StoragePoolId, VolumeId)

	# HTTP DELETE
	def delete(self, StorageServiceId, StoragePoolId, VolumeId):
		logging.info('Volume16 delete called')
		path = create_path(self.root, 'StorageServices/{0}/StoragePools/{1}/AllocatedVolumes/{2}').format(StorageServiceId, StoragePoolId, VolumeId)
		base_path = create_path(self.root, 'StorageServices/{0}/StoragePools/{1}/AllocatedVolumes').format(StorageServiceId, StoragePoolId)
		return delete_object(path, base_path)

