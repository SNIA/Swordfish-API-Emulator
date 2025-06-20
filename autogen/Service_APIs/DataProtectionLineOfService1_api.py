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

# Resource implementation for - /redfish/v1/StorageServices/{StorageServiceId}/ClassesOfService/{ClassOfServiceId}/DataProtectionLinesOfService/{DataProtectionLineOfServiceId}
# Program name - DataProtectionLineOfService1_api.py

import g
import json, os
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import check_authentication, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection

config = {}

INTERNAL_ERROR = 500

# DataProtectionLineOfService1 Collection API
class DataProtectionLineOfService1CollectionAPI(Resource):
	def __init__(self, **kwargs):
		logging.info('DataProtectionLineOfService1 Collection init called')
		self.root = PATHS['Root']
		self.auth = kwargs['auth']

	# HTTP GET
	def get(self, StorageServiceId, ClassOfServiceId):
		logging.info('DataProtectionLineOfService1 Collection get called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = os.path.join(self.root, 'StorageServices/{0}/ClassesOfService/{1}/DataProtectionLinesOfService', 'index.json').format(StorageServiceId, ClassOfServiceId)
			return get_json_data (path)
		else:
			return msg, code

	# HTTP POST
	def post(self, StorageServiceId, ClassOfServiceId):
		logging.info('DataProtectionLineOfService1 Collection post called')
		return 'POST is not a supported command for DataProtectionLineOfService1CollectionAPI', 405

	# HTTP PUT
	def put(self, StorageServiceId, ClassOfServiceId):
		logging.info('DataProtectionLineOfService1 Collection put called')
		return 'PUT is not a supported command for DataProtectionLineOfService1CollectionAPI', 405

	# HTTP PATCH
	def patch(self, StorageServiceId, ClassOfServiceId):
		logging.info('DataProtectionLineOfService1 Collection patch called')
		return 'PATCH is not a supported command for DataProtectionLineOfService1CollectionAPI', 405

	# HTTP DELETE
	def delete(self, StorageServiceId, ClassOfServiceId):
		logging.info('DataProtectionLineOfService1 Collection delete called')
		return 'DELETE is not a supported command for DataProtectionLineOfService1CollectionAPI', 405


# DataProtectionLineOfService1 API
class DataProtectionLineOfService1API(Resource):
	def __init__(self, **kwargs):
		logging.info('DataProtectionLineOfService1 init called')
		self.root = PATHS['Root']
		self.auth = kwargs['auth']

	# HTTP GET
	def get(self, StorageServiceId, ClassOfServiceId, DataProtectionLineOfServiceId):
		logging.info('DataProtectionLineOfService1 get called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = create_path(self.root, 'StorageServices/{0}/ClassesOfService/{1}/DataProtectionLinesOfService/{2}', 'index.json').format(StorageServiceId, ClassOfServiceId, DataProtectionLineOfServiceId)
			return get_json_data (path)
		else:
			return msg, code

	# HTTP POST
	def post(self, StorageServiceId, ClassOfServiceId, DataProtectionLineOfServiceId):
		logging.info('DataProtectionLineOfService1 post called')
		return 'POST is not a supported command for DataProtectionLineOfService1API', 405

	# HTTP PUT
	def put(self, StorageServiceId, ClassOfServiceId, DataProtectionLineOfServiceId):
		logging.info('DataProtectionLineOfService1 put called')
		return 'PUT is not a supported command for DataProtectionLineOfService1API', 405

	# HTTP PATCH
	def patch(self, StorageServiceId, ClassOfServiceId, DataProtectionLineOfServiceId):
		logging.info('DataProtectionLineOfService1 patch called')
		return 'PATCH is not a supported command for DataProtectionLineOfService1API', 405

	# HTTP DELETE
	def delete(self, StorageServiceId, ClassOfServiceId, DataProtectionLineOfServiceId):
		logging.info('DataProtectionLineOfService1 delete called')
		return 'DELETE is not a supported command for DataProtectionLineOfService1API', 405


