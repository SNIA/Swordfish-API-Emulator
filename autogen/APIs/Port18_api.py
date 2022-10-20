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

# Resource implementation for - /redfish/v1/Storage/{StorageId}/StorageControllers/{StorageControllerId}/Ports/{PortId}
# Program name - Port18_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.Port18 import get_Port18_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# Port18 Collection API
class Port18CollectionAPI(Resource):
	def __init__(self):
		logging.info('Port18 Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, StorageId, StorageControllerId):
		logging.info('Port18 Collection get called')
		path = os.path.join(self.root, 'Storage/{0}/StorageControllers/{1}/Ports', 'index.json').format(StorageId, StorageControllerId)
		return get_json_data (path)

	# HTTP POST Collection
	def post(self, StorageId, StorageControllerId):
		logging.info('Port18 Collection post called')

		if StorageControllerId in members:
			resp = 404
			return resp
		path = create_path(self.root, 'Storage/{0}/StorageControllers/{1}/Ports').format(StorageId, StorageControllerId)
		if not os.path.exists(path):
			os.mkdir(path)
			create_collection (path, 'Port')

		res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
		if request.data:
			config = json.loads(request.data)
			if "@odata.id" in config:
				return Port18API.post(self, os.path.basename(config['@odata.id']))
			else:
				return Port18API.post(self, str(res))
		else:
			return Port18API.post(self, str(res))

	# HTTP PUT Collection
	def put(self, StorageId, StorageControllerId):
		logging.info('Port18 Collection put called')

		path = os.path.join(self.root, 'Storage/{0}/StorageControllers/{1}/Ports', 'index.json').format(StorageId, StorageControllerId)
		put_object (path)
		return self.get(StorageId)

# Port18 API
class Port18API(Resource):
	def __init__(self):
		logging.info('Port18 init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, StorageId, StorageControllerId, PortId):
		logging.info('Port18 get called')
		path = create_path(self.root, 'Storage/{0}/StorageControllers/{1}/Ports/{2}', 'index.json').format(StorageId, StorageControllerId, PortId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, StorageId, StorageControllerId, PortId):
		logging.info('Port18 post called')
		path = create_path(self.root, 'Storage/{0}/StorageControllers/{1}/Ports/{2}').format(StorageId, StorageControllerId, PortId)
		collection_path = os.path.join(self.root, 'Storage/{0}/StorageControllers/{1}/Ports', 'index.json').format(StorageId, StorageControllerId)

		# Check if collection exists:
		if not os.path.exists(collection_path):
			Port18CollectionAPI.post(self, StorageId, StorageControllerId)

		if PortId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'StorageId':StorageId, 'StorageControllerId':StorageControllerId, 'PortId':PortId, 'rb':g.rest_base}
			config=get_Port18_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('Port18API POST exit')
		return resp

	# HTTP PUT
	def put(self, StorageId, StorageControllerId, PortId):
		logging.info('Port18 put called')
		path = os.path.join(self.root, 'Storage/{0}/StorageControllers/{1}/Ports/{2}', 'index.json').format(StorageId, StorageControllerId, PortId)
		put_object(path)
		return self.get(StorageId, StorageControllerId, PortId)

	# HTTP PATCH
	def patch(self, StorageId, StorageControllerId, PortId):
		logging.info('Port18 patch called')
		path = os.path.join(self.root, 'Storage/{0}/StorageControllers/{1}/Ports/{2}', 'index.json').format(StorageId, StorageControllerId, PortId)
		patch_object(path)
		return self.get(StorageId, StorageControllerId, PortId)

	# HTTP DELETE
	def delete(self, StorageId, StorageControllerId, PortId):
		logging.info('Port18 delete called')
		path = create_path(self.root, 'Storage/{0}/StorageControllers/{1}/Ports/{2}').format(StorageId, StorageControllerId, PortId)
		base_path = create_path(self.root, 'Storage/{0}/StorageControllers/{1}/Ports').format(StorageId, StorageControllerId)
		return delete_object(path, base_path)

