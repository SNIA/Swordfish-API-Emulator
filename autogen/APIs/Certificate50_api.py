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

# Resource implementation for - /redfish/v1/ResourceBlocks/{ResourceBlockId}/Storage/{StorageId}/Drives/{DriveId}/Certificates/{CertificateId}
# Program name - Certificate50_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.Certificate50 import get_Certificate50_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# Certificate50 Collection API
class Certificate50CollectionAPI(Resource):
	def __init__(self):
		logging.info('Certificate50 Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ResourceBlockId, StorageId, DriveId):
		logging.info('Certificate50 Collection get called')
		path = os.path.join(self.root, 'ResourceBlocks/{0}/Storage/{1}/Drives/{2}/Certificates', 'index.json').format(ResourceBlockId, StorageId, DriveId)
		return get_json_data (path)

	# HTTP POST Collection
	def post(self, ResourceBlockId, StorageId, DriveId):
		logging.info('Certificate50 Collection post called')

		if DriveId in members:
			resp = 404
			return resp
		path = create_path(self.root, 'ResourceBlocks/{0}/Storage/{1}/Drives/{2}/Certificates').format(ResourceBlockId, StorageId, DriveId)
		if not os.path.exists(path):
			os.mkdir(path)
			create_collection (path, 'Certificate')

		res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
		if request.data:
			config = json.loads(request.data)
			if "@odata.id" in config:
				return Certificate50API.post(self, os.path.basename(config['@odata.id']))
			else:
				return Certificate50API.post(self, str(res))
		else:
			return Certificate50API.post(self, str(res))

	# HTTP PUT Collection
	def put(self, ResourceBlockId, StorageId, DriveId):
		logging.info('Certificate50 Collection put called')

		path = os.path.join(self.root, 'ResourceBlocks/{0}/Storage/{1}/Drives/{2}/Certificates', 'index.json').format(ResourceBlockId, StorageId, DriveId)
		put_object (path)
		return self.get(ResourceBlockId)

# Certificate50 API
class Certificate50API(Resource):
	def __init__(self):
		logging.info('Certificate50 init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ResourceBlockId, StorageId, DriveId, CertificateId):
		logging.info('Certificate50 get called')
		path = create_path(self.root, 'ResourceBlocks/{0}/Storage/{1}/Drives/{2}/Certificates/{3}', 'index.json').format(ResourceBlockId, StorageId, DriveId, CertificateId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, ResourceBlockId, StorageId, DriveId, CertificateId):
		logging.info('Certificate50 post called')
		path = create_path(self.root, 'ResourceBlocks/{0}/Storage/{1}/Drives/{2}/Certificates/{3}').format(ResourceBlockId, StorageId, DriveId, CertificateId)
		collection_path = os.path.join(self.root, 'ResourceBlocks/{0}/Storage/{1}/Drives/{2}/Certificates', 'index.json').format(ResourceBlockId, StorageId, DriveId)

		# Check if collection exists:
		if not os.path.exists(collection_path):
			Certificate50CollectionAPI.post(self, ResourceBlockId, StorageId, DriveId)

		if CertificateId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'ResourceBlockId':ResourceBlockId, 'StorageId':StorageId, 'DriveId':DriveId, 'CertificateId':CertificateId, 'rb':g.rest_base}
			config=get_Certificate50_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('Certificate50API POST exit')
		return resp

	# HTTP PUT
	def put(self, ResourceBlockId, StorageId, DriveId, CertificateId):
		logging.info('Certificate50 put called')
		path = os.path.join(self.root, 'ResourceBlocks/{0}/Storage/{1}/Drives/{2}/Certificates/{3}', 'index.json').format(ResourceBlockId, StorageId, DriveId, CertificateId)
		put_object(path)
		return self.get(ResourceBlockId, StorageId, DriveId, CertificateId)

	# HTTP PATCH
	def patch(self, ResourceBlockId, StorageId, DriveId, CertificateId):
		logging.info('Certificate50 patch called')
		path = os.path.join(self.root, 'ResourceBlocks/{0}/Storage/{1}/Drives/{2}/Certificates/{3}', 'index.json').format(ResourceBlockId, StorageId, DriveId, CertificateId)
		patch_object(path)
		return self.get(ResourceBlockId, StorageId, DriveId, CertificateId)

	# HTTP DELETE
	def delete(self, ResourceBlockId, StorageId, DriveId, CertificateId):
		logging.info('Certificate50 delete called')
		path = create_path(self.root, 'ResourceBlocks/{0}/Storage/{1}/Drives/{2}/Certificates/{3}').format(ResourceBlockId, StorageId, DriveId, CertificateId)
		base_path = create_path(self.root, 'ResourceBlocks/{0}/Storage/{1}/Drives/{2}/Certificates').format(ResourceBlockId, StorageId, DriveId)
		return delete_object(path, base_path)

