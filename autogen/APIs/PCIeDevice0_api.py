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

# Resource implementation for - /redfish/v1/Chassis/{ChassisId}/PCIeDevices/{PCIeDeviceId}
# Program name - PCIeDevice0_api.py

import g
import json, os
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.PCIeDevice0 import get_PCIeDevice0_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# PCIeDevice0 Collection API
class PCIeDevice0CollectionAPI(Resource):
	def __init__(self):
		logging.info('PCIeDevice0 Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ChassisId):
		logging.info('PCIeDevice0 Collection get called')
		path = os.path.join(self.root, 'Chassis/{0}/PCIeDevices', 'index.json').format(ChassisId)
		return get_json_data (path)

	# HTTP POST Collection
	def post(self, ChassisId):
		logging.info('PCIeDevice0 Collection post called')

		if ChassisId in members:
			resp = 404
			return resp
		path = create_path(self.root, 'Chassis/{0}/PCIeDevices').format(ChassisId)
		return create_collection (path, 'PCIeDevice')

	# HTTP PUT Collection
	def put(self, ChassisId):
		logging.info('PCIeDevice0 Collection put called')

		path = os.path.join(self.root, 'Chassis/{0}/PCIeDevices', 'index.json').format(ChassisId)
		put_object (path)
		return self.get(ChassisId)

# PCIeDevice0 API
class PCIeDevice0API(Resource):
	def __init__(self):
		logging.info('PCIeDevice0 init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ChassisId, PCIeDeviceId):
		logging.info('PCIeDevice0 get called')
		path = create_path(self.root, 'Chassis/{0}/PCIeDevices/{1}', 'index.json').format(ChassisId, PCIeDeviceId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, ChassisId, PCIeDeviceId):
		logging.info('PCIeDevice0 post called')
		path = create_path(self.root, 'Chassis/{0}/PCIeDevices/{1}').format(ChassisId, PCIeDeviceId)
		collection_path = os.path.join(self.root, 'Chassis/{0}/PCIeDevices', 'index.json').format(ChassisId)

		# Check if collection exists:
		if not os.path.exists(collection_path):
			PCIeDevice0CollectionAPI.post(self, ChassisId)

		if PCIeDeviceId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'ChassisId':ChassisId, 'PCIeDeviceId':PCIeDeviceId, 'rb':g.rest_base}
			config=get_PCIeDevice0_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('PCIeDevice0API POST exit')
		return resp

	# HTTP PUT
	def put(self, ChassisId, PCIeDeviceId):
		logging.info('PCIeDevice0 put called')
		path = create_path(self.root, 'Chassis/{0}/PCIeDevices/{1}', 'index.json').format(ChassisId, PCIeDeviceId)
		put_object(path)
		return self.get(ChassisId, PCIeDeviceId)

	# HTTP PATCH
	def patch(self, ChassisId, PCIeDeviceId):
		logging.info('PCIeDevice0 patch called')
		path = create_path(self.root, 'Chassis/{0}/PCIeDevices/{1}', 'index.json').format(ChassisId, PCIeDeviceId)
		patch_object(path)
		return self.get(ChassisId, PCIeDeviceId)

	# HTTP DELETE
	def delete(self, ChassisId, PCIeDeviceId):
		logging.info('PCIeDevice0 delete called')
		path = create_path(self.root, 'Chassis/{0}/PCIeDevices/{1}').format(ChassisId, PCIeDeviceId)
		base_path = create_path(self.root, 'Chassis/{0}/PCIeDevices').format(ChassisId)
		return delete_object(path, base_path)

