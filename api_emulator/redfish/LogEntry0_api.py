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

# Resource implementation for - /redfish/v1/Managers/{ManagerId}/LogServices/{LogServiceId}/Entries/{LogEntryId}
# Program name - LogEntry0_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.LogEntry0 import get_LogEntry0_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# LogEntry0 Collection API
class LogEntry0CollectionAPI(Resource):
	def __init__(self):
		logging.info('LogEntry0 Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ManagerId, LogServiceId):
		logging.info('LogEntry0 Collection get called')
		path = os.path.join(self.root, 'Managers/{0}/LogServices/{1}/Entries', 'index.json').format(ManagerId, LogServiceId)
		return get_json_data (path)

	# HTTP POST Collection
	def post(self, ManagerId, LogServiceId):
		logging.info('LogEntry0 Collection post called')

		if LogServiceId in members:
			resp = 404
			return resp
		path = create_path(self.root, 'Managers/{0}/LogServices/{1}/Entries').format(ManagerId, LogServiceId)
		if not os.path.exists(path):
			os.mkdir(path)
			create_collection (path, 'LogEntry')

		res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
		if request.data:
			config = json.loads(request.data)
			if "@odata.id" in config:
				return LogEntry0API.post(self, ManagerId, LogServiceId, os.path.basename(config['@odata.id']))
			else:
				return LogEntry0API.post(self, ManagerId, LogServiceId, str(res))
		else:
			return LogEntry0API.post(self, ManagerId, LogServiceId, str(res))

	# HTTP PUT Collection
	def put(self, ManagerId, LogServiceId):
		logging.info('LogEntry0 Collection put called')

		path = os.path.join(self.root, 'Managers/{0}/LogServices/{1}/Entries', 'index.json').format(ManagerId, LogServiceId)
		put_object (path)
		return self.get(ManagerId)

# LogEntry0 API
class LogEntry0API(Resource):
	def __init__(self):
		logging.info('LogEntry0 init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ManagerId, LogServiceId, LogEntryId):
		logging.info('LogEntry0 get called')
		path = create_path(self.root, 'Managers/{0}/LogServices/{1}/Entries/{2}', 'index.json').format(ManagerId, LogServiceId, LogEntryId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, ManagerId, LogServiceId, LogEntryId):
		logging.info('LogEntry0 post called')
		path = create_path(self.root, 'Managers/{0}/LogServices/{1}/Entries/{2}').format(ManagerId, LogServiceId, LogEntryId)
		collection_path = os.path.join(self.root, 'Managers/{0}/LogServices/{1}/Entries', 'index.json').format(ManagerId, LogServiceId)

		# Check if collection exists:
		if not os.path.exists(collection_path):
			LogEntry0CollectionAPI.post(self, ManagerId, LogServiceId)

		if LogEntryId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'ManagerId':ManagerId, 'LogServiceId':LogServiceId, 'LogEntryId':LogEntryId, 'rb':g.rest_base}
			config=get_LogEntry0_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('LogEntry0API POST exit')
		return resp

	# HTTP PUT
	def put(self, ManagerId, LogServiceId, LogEntryId):
		logging.info('LogEntry0 put called')
		path = os.path.join(self.root, 'Managers/{0}/LogServices/{1}/Entries/{2}', 'index.json').format(ManagerId, LogServiceId, LogEntryId)
		put_object(path)
		return self.get(ManagerId, LogServiceId, LogEntryId)

	# HTTP PATCH
	def patch(self, ManagerId, LogServiceId, LogEntryId):
		logging.info('LogEntry0 patch called')
		path = os.path.join(self.root, 'Managers/{0}/LogServices/{1}/Entries/{2}', 'index.json').format(ManagerId, LogServiceId, LogEntryId)
		patch_object(path)
		return self.get(ManagerId, LogServiceId, LogEntryId)

	# HTTP DELETE
	def delete(self, ManagerId, LogServiceId, LogEntryId):
		logging.info('LogEntry0 delete called')
		path = create_path(self.root, 'Managers/{0}/LogServices/{1}/Entries/{2}').format(ManagerId, LogServiceId, LogEntryId)
		base_path = create_path(self.root, 'Managers/{0}/LogServices/{1}/Entries').format(ManagerId, LogServiceId)
		return delete_object(path, base_path)

