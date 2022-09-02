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

# Resource implementation for - /redfish/v1/Systems/{ComputerSystemId}/Processors/{ProcessorId}/Ports/{PortId}
# Program name - Port6_api.py

import g
import json, os
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.Port6 import get_Port6_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# Port6 Collection API
class Port6CollectionAPI(Resource):
	def __init__(self):
		logging.info('Port6 Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ComputerSystemId, ProcessorId):
		logging.info('Port6 Collection get called')
		path = os.path.join(self.root, 'Systems/{0}/Processors/{1}/Ports', 'index.json').format(ComputerSystemId, ProcessorId)
		return get_json_data (path)

	# HTTP POST Collection
	def post(self, ComputerSystemId, ProcessorId):
		logging.info('Port6 Collection post called')

		if ProcessorId in members:
			resp = 404
			return resp
		path = create_path(self.root, 'Systems/{0}/Processors/{1}/Ports').format(ComputerSystemId, ProcessorId)
		return create_collection (path, 'Port')

	# HTTP PUT Collection
	def put(self, ComputerSystemId, ProcessorId):
		path = os.path.join(self.root, 'Systems/{0}/Processors/{1}/Ports', 'index.json').format(ComputerSystemId, ProcessorId)
		put_object (path)
		return self.get(ComputerSystemId)

# Port6 API
class Port6API(Resource):
	def __init__(self):
		logging.info('Port6 init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ComputerSystemId, ProcessorId, PortId):
		logging.info('Port6 get called')
		path = create_path(self.root, 'Systems/{0}/Processors/{1}/Ports/{2}', 'index.json').format(ComputerSystemId, ProcessorId, PortId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, ComputerSystemId, ProcessorId, PortId):
		logging.info('Port6 post called')
		path = create_path(self.root, 'Systems/{0}/Processors/{1}/Ports/{2}').format(ComputerSystemId, ProcessorId, PortId)
		collection_path = os.path.join(self.root, 'Systems/{0}/Processors/{1}/Ports', 'index.json').format(ComputerSystemId, ProcessorId)

		# Check if collection exists:
		if not os.path.exists(collection_path):
			Port6CollectionAPI.post(self, ComputerSystemId, ProcessorId)

		if PortId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'ComputerSystemId':ComputerSystemId, 'ProcessorId':ProcessorId, 'PortId':PortId, 'rb':g.rest_base}
			config=get_Port6_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('Port6API POST exit')
		return resp

	# HTTP PUT
	def put(self, ComputerSystemId, ProcessorId, PortId):
		logging.info('Port6 put called')
		path = os.path.join(self.root, 'Systems/{0}/Processors/{1}/Ports/{2}', 'index.json').format(ComputerSystemId, ProcessorId, PortId)
		put_object(path)
		return self.get(ComputerSystemId, ProcessorId, PortId)

	# HTTP PATCH
	def patch(self, ComputerSystemId, ProcessorId, PortId):
		logging.info('Port6 patch called')
		path = os.path.join(self.root, 'Systems/{0}/Processors/{1}/Ports/{2}', 'index.json').format(ComputerSystemId, ProcessorId, PortId)
		patch_object(path)
		return self.get(ComputerSystemId, ProcessorId, PortId)

	# HTTP DELETE
	def delete(self, ComputerSystemId, ProcessorId, PortId):
		logging.info('Port6 delete called')
		path = create_path(self.root, 'Systems/{0}/Processors/{1}/Ports/{2}').format(ComputerSystemId, ProcessorId, PortId)
		base_path = create_path(self.root, 'Systems/{0}/Processors/{1}/Ports').format(ComputerSystemId, ProcessorId)
		return delete_object(path, base_path)

