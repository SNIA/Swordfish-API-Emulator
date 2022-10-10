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

# Resource implementation for - /redfish/v1/ResourceBlocks/{ResourceBlockId}/Systems/{ComputerSystemId}/Memory/{MemoryId}/Certificates/{CertificateId}
# Program name - Certificate25_api.py

import g
import json, os
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.Certificate25 import get_Certificate25_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# Certificate25 Collection API
class Certificate25CollectionAPI(Resource):
	def __init__(self):
		logging.info('Certificate25 Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ResourceBlockId, ComputerSystemId, MemoryId):
		logging.info('Certificate25 Collection get called')
		path = os.path.join(self.root, 'ResourceBlocks/{0}/Systems/{1}/Memory/{2}/Certificates', 'index.json').format(ResourceBlockId, ComputerSystemId, MemoryId)
		return get_json_data (path)

	# HTTP POST Collection
	def post(self, ResourceBlockId, ComputerSystemId, MemoryId):
		logging.info('Certificate25 Collection post called')

		if MemoryId in members:
			resp = 404
			return resp
		path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/Memory/{2}/Certificates').format(ResourceBlockId, ComputerSystemId, MemoryId)
		return create_collection (path, 'Certificate')

	# HTTP PUT Collection
	def put(self, ResourceBlockId, ComputerSystemId, MemoryId):
		logging.info('Certificate25 Collection put called')

		path = os.path.join(self.root, 'ResourceBlocks/{0}/Systems/{1}/Memory/{2}/Certificates', 'index.json').format(ResourceBlockId, ComputerSystemId, MemoryId)
		put_object (path)
		return self.get(ResourceBlockId)

# Certificate25 API
class Certificate25API(Resource):
	def __init__(self):
		logging.info('Certificate25 init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ResourceBlockId, ComputerSystemId, MemoryId, CertificateId):
		logging.info('Certificate25 get called')
		path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/Memory/{2}/Certificates/{3}', 'index.json').format(ResourceBlockId, ComputerSystemId, MemoryId, CertificateId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, ResourceBlockId, ComputerSystemId, MemoryId, CertificateId):
		logging.info('Certificate25 post called')
		path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/Memory/{2}/Certificates/{3}').format(ResourceBlockId, ComputerSystemId, MemoryId, CertificateId)
		collection_path = os.path.join(self.root, 'ResourceBlocks/{0}/Systems/{1}/Memory/{2}/Certificates', 'index.json').format(ResourceBlockId, ComputerSystemId, MemoryId)

		# Check if collection exists:
		if not os.path.exists(collection_path):
			Certificate25CollectionAPI.post(self, ResourceBlockId, ComputerSystemId, MemoryId)

		if CertificateId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'ResourceBlockId':ResourceBlockId, 'ComputerSystemId':ComputerSystemId, 'MemoryId':MemoryId, 'CertificateId':CertificateId, 'rb':g.rest_base}
			config=get_Certificate25_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('Certificate25API POST exit')
		return resp

	# HTTP PUT
	def put(self, ResourceBlockId, ComputerSystemId, MemoryId, CertificateId):
		logging.info('Certificate25 put called')
		path = os.path.join(self.root, 'ResourceBlocks/{0}/Systems/{1}/Memory/{2}/Certificates/{3}', 'index.json').format(ResourceBlockId, ComputerSystemId, MemoryId, CertificateId)
		put_object(path)
		return self.get(ResourceBlockId, ComputerSystemId, MemoryId, CertificateId)

	# HTTP PATCH
	def patch(self, ResourceBlockId, ComputerSystemId, MemoryId, CertificateId):
		logging.info('Certificate25 patch called')
		path = os.path.join(self.root, 'ResourceBlocks/{0}/Systems/{1}/Memory/{2}/Certificates/{3}', 'index.json').format(ResourceBlockId, ComputerSystemId, MemoryId, CertificateId)
		patch_object(path)
		return self.get(ResourceBlockId, ComputerSystemId, MemoryId, CertificateId)

	# HTTP DELETE
	def delete(self, ResourceBlockId, ComputerSystemId, MemoryId, CertificateId):
		logging.info('Certificate25 delete called')
		path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/Memory/{2}/Certificates/{3}').format(ResourceBlockId, ComputerSystemId, MemoryId, CertificateId)
		base_path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/Memory/{2}/Certificates').format(ResourceBlockId, ComputerSystemId, MemoryId)
		return delete_object(path, base_path)

