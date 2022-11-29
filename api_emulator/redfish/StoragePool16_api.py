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

# Resource implementation for - /redfish/v1/Systems/{ComputerSystemId}/Storage/{StorageId}/Volumes/{VolumeId}/AllocatedPools/{StoragePoolId}
# Program name - StoragePool16_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.StoragePool16 import get_StoragePool16_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# StoragePool16 Collection API
class StoragePool16CollectionAPI(Resource):
	def __init__(self):
		logging.info('StoragePool16 Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ComputerSystemId, StorageId, VolumeId):
		logging.info('StoragePool16 Collection get called')
		path = os.path.join(self.root, 'Systems/{0}/Storage/{1}/Volumes/{2}/AllocatedPools', 'index.json').format(ComputerSystemId, StorageId, VolumeId)
		return get_json_data (path)

	# HTTP POST Collection
	def post(self, ComputerSystemId, StorageId, VolumeId):
		logging.info('StoragePool16 Collection post called')

		if VolumeId in members:
			resp = 404
			return resp
		path = create_path(self.root, 'Systems/{0}/Storage/{1}/Volumes/{2}/AllocatedPools').format(ComputerSystemId, StorageId, VolumeId)
		if not os.path.exists(path):
			os.mkdir(path)
			create_collection (path, 'StoragePool')

		res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
		if request.data:
			config = json.loads(request.data)
			if "@odata.id" in config:
				return StoragePool16API.post(self, ComputerSystemId, StorageId, VolumeId, os.path.basename(config['@odata.id']))
			else:
				return StoragePool16API.post(self, ComputerSystemId, StorageId, VolumeId, str(res))
		else:
			return StoragePool16API.post(self, ComputerSystemId, StorageId, VolumeId, str(res))

	# HTTP PUT Collection
	def put(self, ComputerSystemId, StorageId, VolumeId):
		logging.info('StoragePool16 Collection put called')

		path = os.path.join(self.root, 'Systems/{0}/Storage/{1}/Volumes/{2}/AllocatedPools', 'index.json').format(ComputerSystemId, StorageId, VolumeId)
		put_object (path)
		return self.get(ComputerSystemId)

# StoragePool16 API
class StoragePool16API(Resource):
	def __init__(self):
		logging.info('StoragePool16 init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ComputerSystemId, StorageId, VolumeId, StoragePoolId):
		logging.info('StoragePool16 get called')
		path = create_path(self.root, 'Systems/{0}/Storage/{1}/Volumes/{2}/AllocatedPools/{3}', 'index.json').format(ComputerSystemId, StorageId, VolumeId, StoragePoolId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, ComputerSystemId, StorageId, VolumeId, StoragePoolId):
		logging.info('StoragePool16 post called')
		path = create_path(self.root, 'Systems/{0}/Storage/{1}/Volumes/{2}/AllocatedPools/{3}').format(ComputerSystemId, StorageId, VolumeId, StoragePoolId)
		collection_path = os.path.join(self.root, 'Systems/{0}/Storage/{1}/Volumes/{2}/AllocatedPools', 'index.json').format(ComputerSystemId, StorageId, VolumeId)

		# Check if collection exists:
		if not os.path.exists(collection_path):
			StoragePool16CollectionAPI.post(self, ComputerSystemId, StorageId, VolumeId)

		if StoragePoolId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'ComputerSystemId':ComputerSystemId, 'StorageId':StorageId, 'VolumeId':VolumeId, 'StoragePoolId':StoragePoolId, 'rb':g.rest_base}
			config=get_StoragePool16_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('StoragePool16API POST exit')
		return resp

	# HTTP PUT
	def put(self, ComputerSystemId, StorageId, VolumeId, StoragePoolId):
		logging.info('StoragePool16 put called')
		path = os.path.join(self.root, 'Systems/{0}/Storage/{1}/Volumes/{2}/AllocatedPools/{3}', 'index.json').format(ComputerSystemId, StorageId, VolumeId, StoragePoolId)
		put_object(path)
		return self.get(ComputerSystemId, StorageId, VolumeId, StoragePoolId)

	# HTTP PATCH
	def patch(self, ComputerSystemId, StorageId, VolumeId, StoragePoolId):
		logging.info('StoragePool16 patch called')
		path = os.path.join(self.root, 'Systems/{0}/Storage/{1}/Volumes/{2}/AllocatedPools/{3}', 'index.json').format(ComputerSystemId, StorageId, VolumeId, StoragePoolId)
		patch_object(path)
		return self.get(ComputerSystemId, StorageId, VolumeId, StoragePoolId)

	# HTTP DELETE
	def delete(self, ComputerSystemId, StorageId, VolumeId, StoragePoolId):
		logging.info('StoragePool16 delete called')
		path = create_path(self.root, 'Systems/{0}/Storage/{1}/Volumes/{2}/AllocatedPools/{3}').format(ComputerSystemId, StorageId, VolumeId, StoragePoolId)
		base_path = create_path(self.root, 'Systems/{0}/Storage/{1}/Volumes/{2}/AllocatedPools').format(ComputerSystemId, StorageId, VolumeId)
		return delete_object(path, base_path)

