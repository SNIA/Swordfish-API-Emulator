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

# Resource implementation for - /redfish/v1/CompositionService/ResourceBlocks/{ResourceBlockId}/Systems/{ComputerSystemId}/LogServices/{LogServiceId}/Entries/{LogEntryId}
# Program name - LogEntry2_api.py

import g
import json, os
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.LogEntry2 import get_LogEntry2_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# LogEntry2 Collection API
class LogEntry2CollectionAPI(Resource):
	def __init__(self):
		logging.info('LogEntry2 Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ResourceBlockId, ComputerSystemId, LogServiceId):
		logging.info('LogEntry2 Collection get called')
		path = os.path.join(self.root, 'CompositionService/ResourceBlocks/{0}/Systems/{1}/LogServices/{2}/Entries', 'index.json').format(ResourceBlockId, ComputerSystemId, LogServiceId)
		return get_json_data (path)

	# HTTP POST Collection
	def post(self, ResourceBlockId, ComputerSystemId, LogServiceId):
		logging.info('LogEntry2 Collection post called')

		if LogServiceId in members:
			resp = 404
			return resp
		path = create_path(self.root, 'CompositionService/ResourceBlocks/{0}/Systems/{1}/LogServices/{2}/Entries').format(ResourceBlockId, ComputerSystemId, LogServiceId)
		return create_collection (path, 'LogEntry')

	# HTTP PUT Collection
	def put(self, ResourceBlockId, ComputerSystemId, LogServiceId):
		path = os.path.join(self.root, 'CompositionService/ResourceBlocks/{0}/Systems/{1}/LogServices/{2}/Entries', 'index.json').format(ResourceBlockId, ComputerSystemId, LogServiceId)
		put_object (path)
		return self.get(ResourceBlockId)

# LogEntry2 API
class LogEntry2API(Resource):
	def __init__(self):
		logging.info('LogEntry2 init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ResourceBlockId, ComputerSystemId, LogServiceId, LogEntryId):
		logging.info('LogEntry2 get called')
		path = create_path(self.root, 'CompositionService/ResourceBlocks/{0}/Systems/{1}/LogServices/{2}/Entries/{3}', 'index.json').format(ResourceBlockId, ComputerSystemId, LogServiceId, LogEntryId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, ResourceBlockId, ComputerSystemId, LogServiceId, LogEntryId):
		logging.info('LogEntry2 post called')
		path = create_path(self.root, 'CompositionService/ResourceBlocks/{0}/Systems/{1}/LogServices/{2}/Entries/{3}').format(ResourceBlockId, ComputerSystemId, LogServiceId, LogEntryId)
		collection_path = os.path.join(self.root, 'CompositionService/ResourceBlocks/{0}/Systems/{1}/LogServices/{2}/Entries', 'index.json').format(ResourceBlockId, ComputerSystemId, LogServiceId)

		# Check if collection exists:
		if not os.path.exists(collection_path):
			LogEntry2CollectionAPI.post(self, ResourceBlockId, ComputerSystemId, LogServiceId)

		if LogEntryId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'ResourceBlockId':ResourceBlockId, 'ComputerSystemId':ComputerSystemId, 'LogServiceId':LogServiceId, 'LogEntryId':LogEntryId, 'rb':g.rest_base}
			config=get_LogEntry2_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('LogEntry2API POST exit')
		return resp

	# HTTP PUT
	def put(self, ResourceBlockId, ComputerSystemId, LogServiceId, LogEntryId):
		logging.info('LogEntry2 put called')
		path = os.path.join(self.root, 'CompositionService/ResourceBlocks/{0}/Systems/{1}/LogServices/{2}/Entries/{3}', 'index.json').format(ResourceBlockId, ComputerSystemId, LogServiceId, LogEntryId)
		put_object(path)
		return self.get(ResourceBlockId, ComputerSystemId, LogServiceId, LogEntryId)

	# HTTP PATCH
	def patch(self, ResourceBlockId, ComputerSystemId, LogServiceId, LogEntryId):
		logging.info('LogEntry2 patch called')
		path = os.path.join(self.root, 'CompositionService/ResourceBlocks/{0}/Systems/{1}/LogServices/{2}/Entries/{3}', 'index.json').format(ResourceBlockId, ComputerSystemId, LogServiceId, LogEntryId)
		patch_object(path)
		return self.get(ResourceBlockId, ComputerSystemId, LogServiceId, LogEntryId)

	# HTTP DELETE
	def delete(self, ResourceBlockId, ComputerSystemId, LogServiceId, LogEntryId):
		logging.info('LogEntry2 delete called')
		path = create_path(self.root, 'CompositionService/ResourceBlocks/{0}/Systems/{1}/LogServices/{2}/Entries/{3}').format(ResourceBlockId, ComputerSystemId, LogServiceId, LogEntryId)
		base_path = create_path(self.root, 'CompositionService/ResourceBlocks/{0}/Systems/{1}/LogServices/{2}/Entries').format(ResourceBlockId, ComputerSystemId, LogServiceId)
		return delete_object(path, base_path)

