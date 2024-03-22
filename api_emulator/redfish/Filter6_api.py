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

# Resource implementation for - /redfish/v1/ThermalEquipment/ImmersionUnits/{CoolingUnitId}/Pumps/{PumpId}/Filters/{FilterId}
# Program name - Filter6_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import check_authentication, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, create_collection
from .templates.Filter6 import get_Filter6_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# Filter6 Collection API
class Filter6CollectionAPI(Resource):
	def __init__(self, **kwargs):
		logging.info('Filter6 Collection init called')
		self.root = PATHS['Root']
		self.auth = kwargs['auth']

	# HTTP GET
	def get(self, CoolingUnitId, PumpId):
		logging.info('Filter6 Collection get called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = os.path.join(self.root, 'ThermalEquipment/ImmersionUnits/{0}/Pumps/{1}/Filters', 'index.json').format(CoolingUnitId, PumpId)
			return get_json_data(path)
		else:
			return msg, code

	# HTTP POST Collection
	def post(self, CoolingUnitId, PumpId):
		logging.info('Filter6 Collection post called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			if request.data:
				config = json.loads(request.data)
				if "@odata.type" in config:
					if "Collection" in config["@odata.type"]:
						return "Invalid data in POST body", 400

			if PumpId in members:
				resp = 404
				return resp
			path = create_path(self.root, 'ThermalEquipment/ImmersionUnits/{0}/Pumps/{1}/Filters').format(CoolingUnitId, PumpId)
			parent_path = os.path.dirname(path)
			if not os.path.exists(path):
				os.mkdir(path)
				create_collection (path, 'Filter', parent_path)

			res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
			if request.data:
				config = json.loads(request.data)
				if "@odata.id" in config:
					return Filter6API.post(self, CoolingUnitId, PumpId, os.path.basename(config['@odata.id']))
				else:
					return Filter6API.post(self, CoolingUnitId, PumpId, str(res))
			else:
				return Filter6API.post(self, CoolingUnitId, PumpId, str(res))
		else:
			return msg, code

# Filter6 API
class Filter6API(Resource):
	def __init__(self, **kwargs):
		logging.info('Filter6 init called')
		self.root = PATHS['Root']
		self.auth = kwargs['auth']

	# HTTP GET
	def get(self, CoolingUnitId, PumpId, FilterId):
		logging.info('Filter6 get called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = create_path(self.root, 'ThermalEquipment/ImmersionUnits/{0}/Pumps/{1}/Filters/{2}', 'index.json').format(CoolingUnitId, PumpId, FilterId)
			return get_json_data (path)
		else:
			return msg, code

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, CoolingUnitId, PumpId, FilterId):
		logging.info('Filter6 post called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = create_path(self.root, 'ThermalEquipment/ImmersionUnits/{0}/Pumps/{1}/Filters/{2}').format(CoolingUnitId, PumpId, FilterId)
			collection_path = os.path.join(self.root, 'ThermalEquipment/ImmersionUnits/{0}/Pumps/{1}/Filters', 'index.json').format(CoolingUnitId, PumpId)

			# Check if collection exists:
			if not os.path.exists(collection_path):
				Filter6CollectionAPI.post(self, CoolingUnitId, PumpId)

			if FilterId in members:
				resp = 404
				return resp
			try:
				global config
				wildcards = {'CoolingUnitId':CoolingUnitId, 'PumpId':PumpId, 'FilterId':FilterId, 'rb':g.rest_base}
				config=get_Filter6_instance(wildcards)
				config = create_and_patch_object (config, members, member_ids, path, collection_path)
				resp = config, 200

			except Exception:
				traceback.print_exc()
				resp = INTERNAL_ERROR
			logging.info('Filter6API POST exit')
			return resp
		else:
			return msg, code

	# HTTP PUT
	def put(self, CoolingUnitId, PumpId, FilterId):
		logging.info('Filter6 put called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = os.path.join(self.root, 'ThermalEquipment/ImmersionUnits/{0}/Pumps/{1}/Filters/{2}', 'index.json').format(CoolingUnitId, PumpId, FilterId)
			put_object(path)
			return self.get(CoolingUnitId, PumpId, FilterId)
		else:
			return msg, code

	# HTTP PATCH
	def patch(self, CoolingUnitId, PumpId, FilterId):
		logging.info('Filter6 patch called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = os.path.join(self.root, 'ThermalEquipment/ImmersionUnits/{0}/Pumps/{1}/Filters/{2}', 'index.json').format(CoolingUnitId, PumpId, FilterId)
			patch_object(path)
			return self.get(CoolingUnitId, PumpId, FilterId)
		else:
			return msg, code

	# HTTP DELETE
	def delete(self, CoolingUnitId, PumpId, FilterId):
		logging.info('Filter6 delete called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = create_path(self.root, 'ThermalEquipment/ImmersionUnits/{0}/Pumps/{1}/Filters/{2}').format(CoolingUnitId, PumpId, FilterId)
			base_path = create_path(self.root, 'ThermalEquipment/ImmersionUnits/{0}/Pumps/{1}/Filters').format(CoolingUnitId, PumpId)
			return delete_object(path, base_path)
		else:
			return msg, code

