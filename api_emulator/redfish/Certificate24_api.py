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

# Resource implementation for - /redfish/v1/ResourceBlocks/{ResourceBlockId}/Memory/{MemoryId}/Certificates/{CertificateId}
# Program name - Certificate24_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.Certificate24 import get_Certificate24_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# Certificate24 Collection API
class Certificate24CollectionAPI(Resource):
	def __init__(self):
		logging.info('Certificate24 Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ResourceBlockId, MemoryId):
		logging.info('Certificate24 Collection get called')
		path = os.path.join(self.root, 'ResourceBlocks/{0}/Memory/{1}/Certificates', 'index.json').format(ResourceBlockId, MemoryId)
		return get_json_data (path)

	# HTTP POST Collection
	def post(self, ResourceBlockId, MemoryId):
		logging.info('Certificate24 Collection post called')

		if MemoryId in members:
			resp = 404
			return resp
		path = create_path(self.root, 'ResourceBlocks/{0}/Memory/{1}/Certificates').format(ResourceBlockId, MemoryId)
		if not os.path.exists(path):
			os.mkdir(path)
			create_collection (path, 'Certificate')

		res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
		if request.data:
			config = json.loads(request.data)
			if "@odata.id" in config:
				return Certificate24API.post(self, ResourceBlockId, MemoryId, os.path.basename(config['@odata.id']))
			else:
				return Certificate24API.post(self, ResourceBlockId, MemoryId, str(res))
		else:
			return Certificate24API.post(self, ResourceBlockId, MemoryId, str(res))

	# HTTP PUT Collection
	def put(self, ResourceBlockId, MemoryId):
		logging.info('Certificate24 Collection put called')

		path = os.path.join(self.root, 'ResourceBlocks/{0}/Memory/{1}/Certificates', 'index.json').format(ResourceBlockId, MemoryId)
		put_object (path)
		return self.get(ResourceBlockId)

# Certificate24 API
class Certificate24API(Resource):
	def __init__(self):
		logging.info('Certificate24 init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ResourceBlockId, MemoryId, CertificateId):
		logging.info('Certificate24 get called')
		path = create_path(self.root, 'ResourceBlocks/{0}/Memory/{1}/Certificates/{2}', 'index.json').format(ResourceBlockId, MemoryId, CertificateId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, ResourceBlockId, MemoryId, CertificateId):
		logging.info('Certificate24 post called')
		path = create_path(self.root, 'ResourceBlocks/{0}/Memory/{1}/Certificates/{2}').format(ResourceBlockId, MemoryId, CertificateId)
		collection_path = os.path.join(self.root, 'ResourceBlocks/{0}/Memory/{1}/Certificates', 'index.json').format(ResourceBlockId, MemoryId)

		# Check if collection exists:
		if not os.path.exists(collection_path):
			Certificate24CollectionAPI.post(self, ResourceBlockId, MemoryId)

		if CertificateId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'ResourceBlockId':ResourceBlockId, 'MemoryId':MemoryId, 'CertificateId':CertificateId, 'rb':g.rest_base}
			config=get_Certificate24_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('Certificate24API POST exit')
		return resp

	# HTTP PUT
	def put(self, ResourceBlockId, MemoryId, CertificateId):
		logging.info('Certificate24 put called')
		path = os.path.join(self.root, 'ResourceBlocks/{0}/Memory/{1}/Certificates/{2}', 'index.json').format(ResourceBlockId, MemoryId, CertificateId)
		put_object(path)
		return self.get(ResourceBlockId, MemoryId, CertificateId)

	# HTTP PATCH
	def patch(self, ResourceBlockId, MemoryId, CertificateId):
		logging.info('Certificate24 patch called')
		path = os.path.join(self.root, 'ResourceBlocks/{0}/Memory/{1}/Certificates/{2}', 'index.json').format(ResourceBlockId, MemoryId, CertificateId)
		patch_object(path)
		return self.get(ResourceBlockId, MemoryId, CertificateId)

	# HTTP DELETE
	def delete(self, ResourceBlockId, MemoryId, CertificateId):
		logging.info('Certificate24 delete called')
		path = create_path(self.root, 'ResourceBlocks/{0}/Memory/{1}/Certificates/{2}').format(ResourceBlockId, MemoryId, CertificateId)
		base_path = create_path(self.root, 'ResourceBlocks/{0}/Memory/{1}/Certificates').format(ResourceBlockId, MemoryId)
		return delete_object(path, base_path)

