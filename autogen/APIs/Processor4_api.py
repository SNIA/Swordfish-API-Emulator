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

# Resource implementation for - /redfish/v1/CompositionService/ResourceBlocks/{ResourceBlockId}/Processors/{ProcessorId}/SubProcessors/{ProcessorId2}
# Program name - Processor4_api.py

import g
import json, os
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.Processor4 import get_Processor4_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# Processor4 Collection API
class Processor4CollectionAPI(Resource):
	def __init__(self):
		logging.info('Processor4 Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ResourceBlockId, ProcessorId):
		logging.info('Processor4 Collection get called')
		path = os.path.join(self.root, 'CompositionService/ResourceBlocks/{0}/Processors/{1}/SubProcessors', 'index.json').format(ResourceBlockId, ProcessorId)
		return get_json_data (path)

	# HTTP POST Collection
	def post(self, ResourceBlockId, ProcessorId):
		logging.info('Processor4 Collection post called')

		if ProcessorId in members:
			resp = 404
			return resp
		path = create_path(self.root, 'CompositionService/ResourceBlocks/{0}/Processors/{1}/SubProcessors').format(ResourceBlockId, ProcessorId)
		return create_collection (path, 'Processor')

	# HTTP PUT Collection
	def put(self, ResourceBlockId, ProcessorId):
		logging.info('Processor4 Collection put called')

		path = os.path.join(self.root, 'CompositionService/ResourceBlocks/{0}/Processors/{1}/SubProcessors', 'index.json').format(ResourceBlockId, ProcessorId)
		put_object (path)
		return self.get(ResourceBlockId)

# Processor4 API
class Processor4API(Resource):
	def __init__(self):
		logging.info('Processor4 init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ResourceBlockId, ProcessorId, ProcessorId2):
		logging.info('Processor4 get called')
		path = create_path(self.root, 'CompositionService/ResourceBlocks/{0}/Processors/{1}/SubProcessors/{12}', 'index.json').format(ResourceBlockId, ProcessorId, ProcessorId2)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, ResourceBlockId, ProcessorId, ProcessorId2):
		logging.info('Processor4 post called')
		path = create_path(self.root, 'CompositionService/ResourceBlocks/{0}/Processors/{1}/SubProcessors/{12}').format(ResourceBlockId, ProcessorId, ProcessorId2)
		collection_path = os.path.join(self.root, 'CompositionService/ResourceBlocks/{0}/Processors/{1}/SubProcessors', 'index.json').format(ResourceBlockId, ProcessorId)

		# Check if collection exists:
		if not os.path.exists(collection_path):
			Processor4CollectionAPI.post(self, ResourceBlockId, ProcessorId)

		if ProcessorId2 in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'ResourceBlockId':ResourceBlockId, 'ProcessorId':ProcessorId, 'ProcessorId2':ProcessorId2, 'rb':g.rest_base}
			config=get_Processor4_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('Processor4API POST exit')
		return resp

	# HTTP PUT
	def put(self, ResourceBlockId, ProcessorId, ProcessorId2):
		logging.info('Processor4 put called')
		path = os.path.join(self.root, 'CompositionService/ResourceBlocks/{0}/Processors/{1}/SubProcessors/{12}', 'index.json').format(ResourceBlockId, ProcessorId, ProcessorId2)
		put_object(path)
		return self.get(ResourceBlockId, ProcessorId, ProcessorId2)

	# HTTP PATCH
	def patch(self, ResourceBlockId, ProcessorId, ProcessorId2):
		logging.info('Processor4 patch called')
		path = os.path.join(self.root, 'CompositionService/ResourceBlocks/{0}/Processors/{1}/SubProcessors/{12}', 'index.json').format(ResourceBlockId, ProcessorId, ProcessorId2)
		patch_object(path)
		return self.get(ResourceBlockId, ProcessorId, ProcessorId2)

	# HTTP DELETE
	def delete(self, ResourceBlockId, ProcessorId, ProcessorId2):
		logging.info('Processor4 delete called')
		path = create_path(self.root, 'CompositionService/ResourceBlocks/{0}/Processors/{1}/SubProcessors/{12}').format(ResourceBlockId, ProcessorId, ProcessorId2)
		base_path = create_path(self.root, 'CompositionService/ResourceBlocks/{0}/Processors/{1}/SubProcessors').format(ResourceBlockId, ProcessorId)
		return delete_object(path, base_path)

