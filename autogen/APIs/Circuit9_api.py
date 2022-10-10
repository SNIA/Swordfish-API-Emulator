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

# Resource implementation for - /redfish/v1/PowerEquipment/PowerShelves/{PowerDistributionId}/Branches/{CircuitId}
# Program name - Circuit9_api.py

import g
import json, os
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.Circuit9 import get_Circuit9_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# Circuit9 Collection API
class Circuit9CollectionAPI(Resource):
	def __init__(self):
		logging.info('Circuit9 Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, PowerDistributionId):
		logging.info('Circuit9 Collection get called')
		path = os.path.join(self.root, 'PowerEquipment/PowerShelves/{0}/Branches', 'index.json').format(PowerDistributionId)
		return get_json_data (path)

	# HTTP POST Collection
	def post(self, PowerDistributionId):
		logging.info('Circuit9 Collection post called')

		if PowerDistributionId in members:
			resp = 404
			return resp
		path = create_path(self.root, 'PowerEquipment/PowerShelves/{0}/Branches').format(PowerDistributionId)
		return create_collection (path, 'Circuit')

	# HTTP PUT Collection
	def put(self, PowerDistributionId):
		logging.info('Circuit9 Collection put called')

		path = os.path.join(self.root, 'PowerEquipment/PowerShelves/{0}/Branches', 'index.json').format(PowerDistributionId)
		put_object (path)
		return self.get(PowerDistributionId)

# Circuit9 API
class Circuit9API(Resource):
	def __init__(self):
		logging.info('Circuit9 init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, PowerDistributionId, CircuitId):
		logging.info('Circuit9 get called')
		path = create_path(self.root, 'PowerEquipment/PowerShelves/{0}/Branches/{1}', 'index.json').format(PowerDistributionId, CircuitId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, PowerDistributionId, CircuitId):
		logging.info('Circuit9 post called')
		path = create_path(self.root, 'PowerEquipment/PowerShelves/{0}/Branches/{1}').format(PowerDistributionId, CircuitId)
		collection_path = os.path.join(self.root, 'PowerEquipment/PowerShelves/{0}/Branches', 'index.json').format(PowerDistributionId)

		# Check if collection exists:
		if not os.path.exists(collection_path):
			Circuit9CollectionAPI.post(self, PowerDistributionId)

		if CircuitId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'PowerDistributionId':PowerDistributionId, 'CircuitId':CircuitId, 'rb':g.rest_base}
			config=get_Circuit9_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('Circuit9API POST exit')
		return resp

	# HTTP PUT
	def put(self, PowerDistributionId, CircuitId):
		logging.info('Circuit9 put called')
		path = create_path(self.root, 'PowerEquipment/PowerShelves/{0}/Branches/{1}', 'index.json').format(PowerDistributionId, CircuitId)
		put_object(path)
		return self.get(PowerDistributionId, CircuitId)

	# HTTP PATCH
	def patch(self, PowerDistributionId, CircuitId):
		logging.info('Circuit9 patch called')
		path = create_path(self.root, 'PowerEquipment/PowerShelves/{0}/Branches/{1}', 'index.json').format(PowerDistributionId, CircuitId)
		patch_object(path)
		return self.get(PowerDistributionId, CircuitId)

	# HTTP DELETE
	def delete(self, PowerDistributionId, CircuitId):
		logging.info('Circuit9 delete called')
		path = create_path(self.root, 'PowerEquipment/PowerShelves/{0}/Branches/{1}').format(PowerDistributionId, CircuitId)
		base_path = create_path(self.root, 'PowerEquipment/PowerShelves/{0}/Branches').format(PowerDistributionId)
		return delete_object(path, base_path)

