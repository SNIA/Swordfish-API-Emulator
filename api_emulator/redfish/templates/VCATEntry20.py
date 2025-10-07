#
# Copyright (c) 2017-2025, The Storage Networking Industry Association.
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

# Template for - VCATEntry20
# Program name - VCATEntry20.py

import copy
from flask import json

_TEMPLATE = \
{
	"@Redfish.Copyright": "Copyright 2014-2025 SNIA. All rights reserved.",
	"@odata.id": "{rb}ResourceBlocks/{ResourceBlockId}/Systems/{SystemId}/FabricAdapters/{FabricAdapterId}/Ports/{PortId}/GenZ/VCAT/{VCATEntryId}",
	"@odata.type": "#VCATEntry.v1_0_3.VCATEntry",
	"Id": "{VCATEntryId}",
	"Name": "VCATEntry",
}

def get_VCATEntry20_instance(wildcards):
		"""
		Instantiates and formats the template
		Arguments:
			wildcard - A dictionary of wildcards strings and their replacement values
		"""
		c = copy.deepcopy(_TEMPLATE)
		d = json.dumps(c)
		g = d.replace('{ResourceBlockId}', '-0-')
		g = g.replace('{SystemId}', '-1-')
		g = g.replace('{FabricAdapterId}', '-2-')
		g = g.replace('{PortId}', '-3-')
		g = g.replace('{VCATEntryId}', '-4-')
		g = g.replace('{rb}', 'NUb')
		g = g.replace('{{', '~~!')
		g = g.replace('}}', '!!~')
		g = g.replace('{', '~!')
		g = g.replace('}', '!~')
		g = g.replace('0', '{ResourceBlockId}')
		g = g.replace('1', '{SystemId}')
		g = g.replace('2', '{FabricAdapterId}')
		g = g.replace('3', '{PortId}')
		g = g.replace('4', '{VCATEntryId}')
		g = g.replace('NUb', '{rb}')
		g = g.format(**wildcards)
		g = g.replace('~~!', '{{')
		g = g.replace('!!~', '}}')
		g = g.replace('~!', '{')
		g = g.replace('!~', '}')
		return json.loads(g)