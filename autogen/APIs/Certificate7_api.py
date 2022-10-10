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

# Resource implementation for - /redfish/v1/Managers/{ManagerId}/RemoteAccountService/ExternalAccountProviders/{ExternalAccountProviderId}/Certificates/{CertificateId}
# Program name - Certificate7_api.py

import g
import json, os
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.Certificate7 import get_Certificate7_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# Certificate7 Collection API
class Certificate7CollectionAPI(Resource):
	def __init__(self):
		logging.info('Certificate7 Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ManagerId, ExternalAccountProviderId):
		logging.info('Certificate7 Collection get called')
		path = os.path.join(self.root, 'Managers/{0}/RemoteAccountService/ExternalAccountProviders/{1}/Certificates', 'index.json').format(ManagerId, ExternalAccountProviderId)
		return get_json_data (path)

	# HTTP POST Collection
	def post(self, ManagerId, ExternalAccountProviderId):
		logging.info('Certificate7 Collection post called')

		if ExternalAccountProviderId in members:
			resp = 404
			return resp
		path = create_path(self.root, 'Managers/{0}/RemoteAccountService/ExternalAccountProviders/{1}/Certificates').format(ManagerId, ExternalAccountProviderId)
		return create_collection (path, 'Certificate')

	# HTTP PUT Collection
	def put(self, ManagerId, ExternalAccountProviderId):
		logging.info('Certificate7 Collection put called')

		path = os.path.join(self.root, 'Managers/{0}/RemoteAccountService/ExternalAccountProviders/{1}/Certificates', 'index.json').format(ManagerId, ExternalAccountProviderId)
		put_object (path)
		return self.get(ManagerId)

# Certificate7 API
class Certificate7API(Resource):
	def __init__(self):
		logging.info('Certificate7 init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ManagerId, ExternalAccountProviderId, CertificateId):
		logging.info('Certificate7 get called')
		path = create_path(self.root, 'Managers/{0}/RemoteAccountService/ExternalAccountProviders/{1}/Certificates/{2}', 'index.json').format(ManagerId, ExternalAccountProviderId, CertificateId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, ManagerId, ExternalAccountProviderId, CertificateId):
		logging.info('Certificate7 post called')
		path = create_path(self.root, 'Managers/{0}/RemoteAccountService/ExternalAccountProviders/{1}/Certificates/{2}').format(ManagerId, ExternalAccountProviderId, CertificateId)
		collection_path = os.path.join(self.root, 'Managers/{0}/RemoteAccountService/ExternalAccountProviders/{1}/Certificates', 'index.json').format(ManagerId, ExternalAccountProviderId)

		# Check if collection exists:
		if not os.path.exists(collection_path):
			Certificate7CollectionAPI.post(self, ManagerId, ExternalAccountProviderId)

		if CertificateId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'ManagerId':ManagerId, 'ExternalAccountProviderId':ExternalAccountProviderId, 'CertificateId':CertificateId, 'rb':g.rest_base}
			config=get_Certificate7_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('Certificate7API POST exit')
		return resp

	# HTTP PUT
	def put(self, ManagerId, ExternalAccountProviderId, CertificateId):
		logging.info('Certificate7 put called')
		path = os.path.join(self.root, 'Managers/{0}/RemoteAccountService/ExternalAccountProviders/{1}/Certificates/{2}', 'index.json').format(ManagerId, ExternalAccountProviderId, CertificateId)
		put_object(path)
		return self.get(ManagerId, ExternalAccountProviderId, CertificateId)

	# HTTP PATCH
	def patch(self, ManagerId, ExternalAccountProviderId, CertificateId):
		logging.info('Certificate7 patch called')
		path = os.path.join(self.root, 'Managers/{0}/RemoteAccountService/ExternalAccountProviders/{1}/Certificates/{2}', 'index.json').format(ManagerId, ExternalAccountProviderId, CertificateId)
		patch_object(path)
		return self.get(ManagerId, ExternalAccountProviderId, CertificateId)

	# HTTP DELETE
	def delete(self, ManagerId, ExternalAccountProviderId, CertificateId):
		logging.info('Certificate7 delete called')
		path = create_path(self.root, 'Managers/{0}/RemoteAccountService/ExternalAccountProviders/{1}/Certificates/{2}').format(ManagerId, ExternalAccountProviderId, CertificateId)
		base_path = create_path(self.root, 'Managers/{0}/RemoteAccountService/ExternalAccountProviders/{1}/Certificates').format(ManagerId, ExternalAccountProviderId)
		return delete_object(path, base_path)

