#
# Copyright (c) 2017-2024, The Storage Networking Industry Association.
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

# Resource implementation for - /redfish/v1/Systems/{ComputerSystemId}/SecureBoot/SecureBootDatabases/{DatabaseId}/Certificates/{CertificateId}
# Program name - Certificate16_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import check_authentication, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, create_collection, send_event, send_event
from .templates.Certificate16 import get_Certificate16_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# Certificate16 Collection API
class Certificate16CollectionAPI(Resource):
	def __init__(self, **kwargs):
		logging.info('Certificate16 Collection init called')
		self.root = PATHS['Root']
		self.auth = kwargs['auth']

	# HTTP GET
	def get(self, ComputerSystemId, DatabaseId):
		logging.info('Certificate16 Collection get called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = os.path.join(self.root, 'Systems/{0}/SecureBoot/SecureBootDatabases/{1}/Certificates', 'index.json').format(ComputerSystemId, DatabaseId)
			return get_json_data(path)
		else:
			return msg, code

	# HTTP POST Collection
	def post(self, ComputerSystemId, DatabaseId):
		logging.info('Certificate16 Collection post called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			if request.data:
				config = json.loads(request.data)
				if "@odata.type" in config:
					if "Collection" in config["@odata.type"]:
						return "Invalid data in POST body", 400

			if DatabaseId in members:
				resp = 404
				return resp
			path = create_path(self.root, 'Systems/{0}/SecureBoot/SecureBootDatabases/{1}/Certificates').format(ComputerSystemId, DatabaseId)
			parent_path = os.path.dirname(path)
			if not os.path.exists(path):
				os.mkdir(path)
				create_collection (path, 'Certificate', parent_path)

			res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
			if request.data:
				config = json.loads(request.data)
				if "@odata.id" in config:
					return Certificate16API.post(self, ComputerSystemId, DatabaseId, os.path.basename(config['@odata.id']))
				else:
					return Certificate16API.post(self, ComputerSystemId, DatabaseId, str(res))
			else:
				return Certificate16API.post(self, ComputerSystemId, DatabaseId, str(res))
		else:
			return msg, code

# Certificate16 API
class Certificate16API(Resource):
	def __init__(self, **kwargs):
		logging.info('Certificate16 init called')
		self.root = PATHS['Root']
		self.auth = kwargs['auth']

	# HTTP GET
	def get(self, ComputerSystemId, DatabaseId, CertificateId):
		logging.info('Certificate16 get called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = create_path(self.root, 'Systems/{0}/SecureBoot/SecureBootDatabases/{1}/Certificates/{2}', 'index.json').format(ComputerSystemId, DatabaseId, CertificateId)
			return get_json_data (path)
		else:
			return msg, code

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, ComputerSystemId, DatabaseId, CertificateId):
		logging.info('Certificate16 post called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = create_path(self.root, 'Systems/{0}/SecureBoot/SecureBootDatabases/{1}/Certificates/{2}').format(ComputerSystemId, DatabaseId, CertificateId)
			collection_path = os.path.join(self.root, 'Systems/{0}/SecureBoot/SecureBootDatabases/{1}/Certificates', 'index.json').format(ComputerSystemId, DatabaseId)

			# Check if collection exists:
			if not os.path.exists(collection_path):
				Certificate16CollectionAPI.post(self, ComputerSystemId, DatabaseId)

			if CertificateId in members:
				resp = 404
				return resp
			try:
				global config
				wildcards = {'ComputerSystemId':ComputerSystemId, 'DatabaseId':DatabaseId, 'CertificateId':CertificateId, 'rb':g.rest_base}
				config=get_Certificate16_instance(wildcards)
				config = create_and_patch_object (config, members, member_ids, path, collection_path)
				resp = config, 200

			except Exception:
				traceback.print_exc()
				resp = INTERNAL_ERROR
			logging.info('Certificate16API POST exit')
			return resp
		else:
			return msg, code

	# HTTP PUT
	def put(self, ComputerSystemId, DatabaseId, CertificateId):
		logging.info('Certificate16 put called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = os.path.join(self.root, 'Systems/{0}/SecureBoot/SecureBootDatabases/{1}/Certificates/{2}', 'index.json').format(ComputerSystemId, DatabaseId, CertificateId)
			put_object(path)
			return self.get(ComputerSystemId, DatabaseId, CertificateId)
		else:
			return msg, code

	# HTTP PATCH
	def patch(self, ComputerSystemId, DatabaseId, CertificateId):
		logging.info('Certificate16 patch called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = os.path.join(self.root, 'Systems/{0}/SecureBoot/SecureBootDatabases/{1}/Certificates/{2}', 'index.json').format(ComputerSystemId, DatabaseId, CertificateId)
			patch_object(path)
			return self.get(ComputerSystemId, DatabaseId, CertificateId)
		else:
			return msg, code

	# HTTP DELETE
	def delete(self, ComputerSystemId, DatabaseId, CertificateId):
		logging.info('Certificate16 delete called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = create_path(self.root, 'Systems/{0}/SecureBoot/SecureBootDatabases/{1}/Certificates/{2}').format(ComputerSystemId, DatabaseId, CertificateId)
			base_path = create_path(self.root, 'Systems/{0}/SecureBoot/SecureBootDatabases/{1}/Certificates').format(ComputerSystemId, DatabaseId)
			return delete_object(path, base_path)
		else:
			return msg, code

