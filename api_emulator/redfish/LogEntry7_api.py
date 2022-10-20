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

# Resource implementation for - /redfish/v1/Systems/{ComputerSystemId}/Memory/{MemoryId}/DeviceLog/Entries/{LogEntryId}
# Program name - LogEntry7_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.LogEntry7 import get_LogEntry7_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# LogEntry7 Collection API
class LogEntry7CollectionAPI(Resource):
	def __init__(self):
		logging.info('LogEntry7 Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ComputerSystemId, MemoryId):
		logging.info('LogEntry7 Collection get called')
		path = os.path.join(self.root, 'Systems/{0}/Memory/{1}/DeviceLog/Entries', 'index.json').format(ComputerSystemId, MemoryId)
		return get_json_data (path)

	# HTTP POST Collection
	def post(self, ComputerSystemId, MemoryId):
		logging.info('LogEntry7 Collection post called')

		if MemoryId in members:
			resp = 404
			return resp
		path = create_path(self.root, 'Systems/{0}/Memory/{1}/DeviceLog/Entries').format(ComputerSystemId, MemoryId)
		if not os.path.exists(path):
			os.mkdir(path)
			create_collection (path, 'LogEntry')

		res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
		if request.data:
			config = json.loads(request.data)
			if "@odata.id" in config:
				return LogEntry7API.post(self, os.path.basename(config['@odata.id']))
			else:
				return LogEntry7API.post(self, str(res))
		else:
			return LogEntry7API.post(self, str(res))

	# HTTP PUT Collection
	def put(self, ComputerSystemId, MemoryId):
		logging.info('LogEntry7 Collection put called')

		path = os.path.join(self.root, 'Systems/{0}/Memory/{1}/DeviceLog/Entries', 'index.json').format(ComputerSystemId, MemoryId)
		put_object (path)
		return self.get(ComputerSystemId)

# LogEntry7 API
class LogEntry7API(Resource):
	def __init__(self):
		logging.info('LogEntry7 init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ComputerSystemId, MemoryId, LogEntryId):
		logging.info('LogEntry7 get called')
		path = create_path(self.root, 'Systems/{0}/Memory/{1}/DeviceLog/Entries/{2}', 'index.json').format(ComputerSystemId, MemoryId, LogEntryId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, ComputerSystemId, MemoryId, LogEntryId):
		logging.info('LogEntry7 post called')
		path = create_path(self.root, 'Systems/{0}/Memory/{1}/DeviceLog/Entries/{2}').format(ComputerSystemId, MemoryId, LogEntryId)
		collection_path = os.path.join(self.root, 'Systems/{0}/Memory/{1}/DeviceLog/Entries', 'index.json').format(ComputerSystemId, MemoryId)

		# Check if collection exists:
		if not os.path.exists(collection_path):
			LogEntry7CollectionAPI.post(self, ComputerSystemId, MemoryId)

		if LogEntryId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'ComputerSystemId':ComputerSystemId, 'MemoryId':MemoryId, 'LogEntryId':LogEntryId, 'rb':g.rest_base}
			config=get_LogEntry7_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('LogEntry7API POST exit')
		return resp

	# HTTP PUT
	def put(self, ComputerSystemId, MemoryId, LogEntryId):
		logging.info('LogEntry7 put called')
		path = os.path.join(self.root, 'Systems/{0}/Memory/{1}/DeviceLog/Entries/{2}', 'index.json').format(ComputerSystemId, MemoryId, LogEntryId)
		put_object(path)
		return self.get(ComputerSystemId, MemoryId, LogEntryId)

	# HTTP PATCH
	def patch(self, ComputerSystemId, MemoryId, LogEntryId):
		logging.info('LogEntry7 patch called')
		path = os.path.join(self.root, 'Systems/{0}/Memory/{1}/DeviceLog/Entries/{2}', 'index.json').format(ComputerSystemId, MemoryId, LogEntryId)
		patch_object(path)
		return self.get(ComputerSystemId, MemoryId, LogEntryId)

	# HTTP DELETE
	def delete(self, ComputerSystemId, MemoryId, LogEntryId):
		logging.info('LogEntry7 delete called')
		path = create_path(self.root, 'Systems/{0}/Memory/{1}/DeviceLog/Entries/{2}').format(ComputerSystemId, MemoryId, LogEntryId)
		base_path = create_path(self.root, 'Systems/{0}/Memory/{1}/DeviceLog/Entries').format(ComputerSystemId, MemoryId)
		return delete_object(path, base_path)

