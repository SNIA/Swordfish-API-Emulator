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

# Resource implementation for - /redfish/v1/UpdateService/ClientCertificates/{CertificateId}
# Program name - Certificate61_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.Certificate61 import get_Certificate61_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# Certificate61 Collection API
class Certificate61CollectionAPI(Resource):
	def __init__(self):
		logging.info('Certificate61 Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self):
		logging.info('Certificate61 Collection get called')
		path = os.path.join(self.root, 'UpdateService/ClientCertificates', 'index.json')
		return get_json_data (path)

	# HTTP POST Collection
	def post(self):
		logging.info('Certificate61 Collection post called')

		if request.data:
			config = json.loads(request.data)
			if "@odata.type" in config:
				if "Collection" in config["@odata.type"]:
					return "Invalid data in POST body", 400

		path = create_path(self.root, 'UpdateService/ClientCertificates')
		parent_path = os.path.dirname(path)
		if not os.path.exists(path):
			os.mkdir(path)
			create_collection (path, 'Certificate', parent_path)

		res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
		if request.data:
			config = json.loads(request.data)
			if "@odata.id" in config:
				return Certificate61API.post(self, os.path.basename(config['@odata.id']))
			else:
				return Certificate61API.post(self, str(res))
		else:
			return Certificate61API.post(self, str(res))

	# HTTP PUT Collection
	def put(self):
		logging.info('Certificate61 Collection put called')

		path = os.path.join(self.root, 'UpdateService/ClientCertificates', 'index.json')
		put_object (path)
		return self.get(self.root)

# Certificate61 API
class Certificate61API(Resource):
	def __init__(self):
		logging.info('Certificate61 init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, CertificateId):
		logging.info('Certificate61 get called')
		path = create_path(self.root, 'UpdateService/ClientCertificates/{0}', 'index.json').format(CertificateId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, CertificateId):
		logging.info('Certificate61 post called')
		path = create_path(self.root, 'UpdateService/ClientCertificates/{0}').format(CertificateId)
		collection_path = os.path.join(self.root, 'UpdateService/ClientCertificates', 'index.json')

		# Check if collection exists:
		if not os.path.exists(collection_path):
			Certificate61CollectionAPI.post(self)

		if CertificateId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'CertificateId':CertificateId, 'rb':g.rest_base}
			config=get_Certificate61_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('Certificate61API POST exit')
		return resp

	# HTTP PUT
	def put(self, CertificateId):
		logging.info('Certificate61 put called')
		path = os.path.join(self.root, 'UpdateService/ClientCertificates/{0}', 'index.json').format(CertificateId)
		put_object(path)
		return self.get(CertificateId)

	# HTTP PATCH
	def patch(self, CertificateId):
		logging.info('Certificate61 patch called')
		path = os.path.join(self.root, 'UpdateService/ClientCertificates/{0}', 'index.json').format(CertificateId)
		patch_object(path)
		return self.get(CertificateId)

	# HTTP DELETE
	def delete(self, CertificateId):
		logging.info('Certificate61 delete called')
		path = create_path(self.root, 'UpdateService/ClientCertificates/{0}').format(CertificateId)
		base_path = create_path(self.root, 'UpdateService/ClientCertificates')
		return delete_object(path, base_path)

