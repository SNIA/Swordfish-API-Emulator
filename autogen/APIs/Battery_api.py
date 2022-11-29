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

# Resource implementation for - /redfish/v1/Chassis/{ChassisId}/PowerSubsystem/Batteries/{BatteryId}
# Program name - Battery_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.Battery import get_Battery_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# Battery Collection API
class BatteryCollectionAPI(Resource):
	def __init__(self):
		logging.info('Battery Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ChassisId):
		logging.info('Battery Collection get called')
		path = os.path.join(self.root, 'Chassis/{0}/PowerSubsystem/Batteries', 'index.json').format(ChassisId)
		return get_json_data (path)

	# HTTP POST Collection
	def post(self, ChassisId):
		logging.info('Battery Collection post called')

		if ChassisId in members:
			resp = 404
			return resp
		path = create_path(self.root, 'Chassis/{0}/PowerSubsystem/Batteries').format(ChassisId)
		if not os.path.exists(path):
			os.mkdir(path)
			create_collection (path, 'Battery')

		res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
		if request.data:
			config = json.loads(request.data)
			if "@odata.id" in config:
				return BatteryAPI.post(self, ChassisId, os.path.basename(config['@odata.id']))
			else:
				return BatteryAPI.post(self, ChassisId, str(res))
		else:
			return BatteryAPI.post(self, ChassisId, str(res))

	# HTTP PUT Collection
	def put(self, ChassisId):
		logging.info('Battery Collection put called')

		path = os.path.join(self.root, 'Chassis/{0}/PowerSubsystem/Batteries', 'index.json').format(ChassisId)
		put_object (path)
		return self.get(ChassisId)

# Battery API
class BatteryAPI(Resource):
	def __init__(self):
		logging.info('Battery init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ChassisId, BatteryId):
		logging.info('Battery get called')
		path = create_path(self.root, 'Chassis/{0}/PowerSubsystem/Batteries/{1}', 'index.json').format(ChassisId, BatteryId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, ChassisId, BatteryId):
		logging.info('Battery post called')
		path = create_path(self.root, 'Chassis/{0}/PowerSubsystem/Batteries/{1}').format(ChassisId, BatteryId)
		collection_path = os.path.join(self.root, 'Chassis/{0}/PowerSubsystem/Batteries', 'index.json').format(ChassisId)

		# Check if collection exists:
		if not os.path.exists(collection_path):
			BatteryCollectionAPI.post(self, ChassisId)

		if BatteryId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'ChassisId':ChassisId, 'BatteryId':BatteryId, 'rb':g.rest_base}
			config=get_Battery_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('BatteryAPI POST exit')
		return resp

	# HTTP PUT
	def put(self, ChassisId, BatteryId):
		logging.info('Battery put called')
		path = create_path(self.root, 'Chassis/{0}/PowerSubsystem/Batteries/{1}', 'index.json').format(ChassisId, BatteryId)
		put_object(path)
		return self.get(ChassisId, BatteryId)

	# HTTP PATCH
	def patch(self, ChassisId, BatteryId):
		logging.info('Battery patch called')
		path = create_path(self.root, 'Chassis/{0}/PowerSubsystem/Batteries/{1}', 'index.json').format(ChassisId, BatteryId)
		patch_object(path)
		return self.get(ChassisId, BatteryId)

	# HTTP DELETE
	def delete(self, ChassisId, BatteryId):
		logging.info('Battery delete called')
		path = create_path(self.root, 'Chassis/{0}/PowerSubsystem/Batteries/{1}').format(ChassisId, BatteryId)
		base_path = create_path(self.root, 'Chassis/{0}/PowerSubsystem/Batteries').format(ChassisId)
		return delete_object(path, base_path)

