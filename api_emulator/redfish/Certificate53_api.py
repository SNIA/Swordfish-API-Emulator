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

# Resource implementation for - /redfish/v1/Chassis/{ChassisId}/NetworkAdapters/{NetworkAdapterId}/Certificates/{CertificateId}
# Program name - Certificate53_api.py

import g
import json, os
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.Certificate53 import get_Certificate53_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# Certificate53 Collection API
class Certificate53CollectionAPI(Resource):
	def __init__(self):
		logging.info('Certificate53 Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ChassisId, NetworkAdapterId):
		logging.info('Certificate53 Collection get called')
		path = os.path.join(self.root, 'Chassis/{0}/NetworkAdapters/{1}/Certificates', 'index.json').format(ChassisId, NetworkAdapterId)
		return get_json_data (path)

	# HTTP POST Collection
	def post(self, ChassisId, NetworkAdapterId):
		logging.info('Certificate53 Collection post called')

		if NetworkAdapterId in members:
			resp = 404
			return resp
		path = create_path(self.root, 'Chassis/{0}/NetworkAdapters/{1}/Certificates').format(ChassisId, NetworkAdapterId)
		return create_collection (path, 'Certificate')

	# HTTP PUT Collection
	def put(self, ChassisId, NetworkAdapterId):
		logging.info('Certificate53 Collection put called')

		path = os.path.join(self.root, 'Chassis/{0}/NetworkAdapters/{1}/Certificates', 'index.json').format(ChassisId, NetworkAdapterId)
		put_object (path)
		return self.get(ChassisId)

# Certificate53 API
class Certificate53API(Resource):
	def __init__(self):
		logging.info('Certificate53 init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ChassisId, NetworkAdapterId, CertificateId):
		logging.info('Certificate53 get called')
		path = create_path(self.root, 'Chassis/{0}/NetworkAdapters/{1}/Certificates/{2}', 'index.json').format(ChassisId, NetworkAdapterId, CertificateId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, ChassisId, NetworkAdapterId, CertificateId):
		logging.info('Certificate53 post called')
		path = create_path(self.root, 'Chassis/{0}/NetworkAdapters/{1}/Certificates/{2}').format(ChassisId, NetworkAdapterId, CertificateId)
		collection_path = os.path.join(self.root, 'Chassis/{0}/NetworkAdapters/{1}/Certificates', 'index.json').format(ChassisId, NetworkAdapterId)

		# Check if collection exists:
		if not os.path.exists(collection_path):
			Certificate53CollectionAPI.post(self, ChassisId, NetworkAdapterId)

		if CertificateId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'ChassisId':ChassisId, 'NetworkAdapterId':NetworkAdapterId, 'CertificateId':CertificateId, 'rb':g.rest_base}
			config=get_Certificate53_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('Certificate53API POST exit')
		return resp

	# HTTP PUT
	def put(self, ChassisId, NetworkAdapterId, CertificateId):
		logging.info('Certificate53 put called')
		path = os.path.join(self.root, 'Chassis/{0}/NetworkAdapters/{1}/Certificates/{2}', 'index.json').format(ChassisId, NetworkAdapterId, CertificateId)
		put_object(path)
		return self.get(ChassisId, NetworkAdapterId, CertificateId)

	# HTTP PATCH
	def patch(self, ChassisId, NetworkAdapterId, CertificateId):
		logging.info('Certificate53 patch called')
		path = os.path.join(self.root, 'Chassis/{0}/NetworkAdapters/{1}/Certificates/{2}', 'index.json').format(ChassisId, NetworkAdapterId, CertificateId)
		patch_object(path)
		return self.get(ChassisId, NetworkAdapterId, CertificateId)

	# HTTP DELETE
	def delete(self, ChassisId, NetworkAdapterId, CertificateId):
		logging.info('Certificate53 delete called')
		path = create_path(self.root, 'Chassis/{0}/NetworkAdapters/{1}/Certificates/{2}').format(ChassisId, NetworkAdapterId, CertificateId)
		base_path = create_path(self.root, 'Chassis/{0}/NetworkAdapters/{1}/Certificates').format(ChassisId, NetworkAdapterId)
		return delete_object(path, base_path)

