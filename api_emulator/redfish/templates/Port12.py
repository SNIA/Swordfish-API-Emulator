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

# Template for - Port12
# Program name - Port12.py

import copy
from flask import json

_TEMPLATE = \
{
	"@Redfish.Copyright": "Copyright 2014-2021 SNIA. All rights reserved.",
	"@odata.id": "{rb}ResourceBlocks/{ResourceBlockId}/Storage/{StorageId}/Controllers/{StorageControllerId}/Ports/{PortId}",
	"@odata.type": "#Port.v1_6_1.Port",
	"Id": "{PortId}",
	"Name": "Port View 1",
}

def get_Port12_instance(wildcards):
		"""
		Instantiates and formats the template
		Arguments:
			wildcard - A dictionary of wildcards strings and their repalcement values
		"""
		c = copy.deepcopy(_TEMPLATE)
		d = json.dumps(c)
		g = d.replace('{ResourceBlockId}', '0')
		g = g.replace('{StorageId}', '0')
		g = g.replace('{StorageControllerId}', '1')
		g = g.replace('{PortId}', '2')
		g = g.replace('{rb}', 'NUb')
		g = g.replace('{{', '~~!')
		g = g.replace('}}', '!!~')
		g = g.replace('{', '~!')
		g = g.replace('}', '!~')
		g = g.replace('0', '{ResourceBlockId}')
		g = g.replace('1', '{StorageId}')
		g = g.replace('2', '{StorageControllerId}')
		g = g.replace('3', '{PortId}')
		g = g.replace('NUb', '{rb}')
		g = g.format(**wildcards)
		g = g.replace('~~!', '{{')
		g = g.replace('!!~', '}}')
		g = g.replace('~!', '{')
		g = g.replace('!~', '}')
		return json.loads(g)