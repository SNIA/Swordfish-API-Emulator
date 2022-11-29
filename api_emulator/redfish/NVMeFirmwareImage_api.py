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

# Resource implementation for - /redfish/v1/NVMeDomains/{DomainId}/AvailableFirmwareImages/{FirmwareImageId}
# Program name - NVMeFirmwareImage_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.NVMeFirmwareImage import get_NVMeFirmwareImage_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# NVMeFirmwareImage Collection API
class NVMeFirmwareImageCollectionAPI(Resource):
	def __init__(self):
		logging.info('NVMeFirmwareImage Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, DomainId):
		logging.info('NVMeFirmwareImage Collection get called')
		path = os.path.join(self.root, 'NVMeDomains/{0}/AvailableFirmwareImages', 'index.json').format(DomainId)
		return get_json_data (path)

	# HTTP POST Collection
	def post(self, DomainId):
		logging.info('NVMeFirmwareImage Collection post called')

		if DomainId in members:
			resp = 404
			return resp
		path = create_path(self.root, 'NVMeDomains/{0}/AvailableFirmwareImages').format(DomainId)
		if not os.path.exists(path):
			os.mkdir(path)
			create_collection (path, 'NVMeFirmwareImage')

		res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
		if request.data:
			config = json.loads(request.data)
			if "@odata.id" in config:
				return NVMeFirmwareImageAPI.post(self, DomainId, os.path.basename(config['@odata.id']))
			else:
				return NVMeFirmwareImageAPI.post(self, DomainId, str(res))
		else:
			return NVMeFirmwareImageAPI.post(self, DomainId, str(res))

	# HTTP PUT Collection
	def put(self, DomainId):
		logging.info('NVMeFirmwareImage Collection put called')

		path = os.path.join(self.root, 'NVMeDomains/{0}/AvailableFirmwareImages', 'index.json').format(DomainId)
		put_object (path)
		return self.get(DomainId)

# NVMeFirmwareImage API
class NVMeFirmwareImageAPI(Resource):
	def __init__(self):
		logging.info('NVMeFirmwareImage init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, DomainId, FirmwareImageId):
		logging.info('NVMeFirmwareImage get called')
		path = create_path(self.root, 'NVMeDomains/{0}/AvailableFirmwareImages/{1}', 'index.json').format(DomainId, FirmwareImageId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, DomainId, FirmwareImageId):
		logging.info('NVMeFirmwareImage post called')
		path = create_path(self.root, 'NVMeDomains/{0}/AvailableFirmwareImages/{1}').format(DomainId, FirmwareImageId)
		collection_path = os.path.join(self.root, 'NVMeDomains/{0}/AvailableFirmwareImages', 'index.json').format(DomainId)

		# Check if collection exists:
		if not os.path.exists(collection_path):
			NVMeFirmwareImageCollectionAPI.post(self, DomainId)

		if FirmwareImageId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'DomainId':DomainId, 'FirmwareImageId':FirmwareImageId, 'rb':g.rest_base}
			config=get_NVMeFirmwareImage_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('NVMeFirmwareImageAPI POST exit')
		return resp

	# HTTP PUT
	def put(self, DomainId, FirmwareImageId):
		logging.info('NVMeFirmwareImage put called')
		path = create_path(self.root, 'NVMeDomains/{0}/AvailableFirmwareImages/{1}', 'index.json').format(DomainId, FirmwareImageId)
		put_object(path)
		return self.get(DomainId, FirmwareImageId)

	# HTTP PATCH
	def patch(self, DomainId, FirmwareImageId):
		logging.info('NVMeFirmwareImage patch called')
		path = create_path(self.root, 'NVMeDomains/{0}/AvailableFirmwareImages/{1}', 'index.json').format(DomainId, FirmwareImageId)
		patch_object(path)
		return self.get(DomainId, FirmwareImageId)

	# HTTP DELETE
	def delete(self, DomainId, FirmwareImageId):
		logging.info('NVMeFirmwareImage delete called')
		path = create_path(self.root, 'NVMeDomains/{0}/AvailableFirmwareImages/{1}').format(DomainId, FirmwareImageId)
		base_path = create_path(self.root, 'NVMeDomains/{0}/AvailableFirmwareImages').format(DomainId)
		return delete_object(path, base_path)

