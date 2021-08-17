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
#

# FabricAdapterPort Template File

import copy
from flask import json

_TEMPLATE={
    "@odata.type": "Port.v1_4_0.Port",
    "@odata.id": "{rb}Systems/{s_id}/FabricAdapters/{fa_id}/Ports/{fap_id}",

    "Id": "{fap_id}",
    "Name": "Port",
    "Description": "Fabric Adapter port",
    "PortType": "Upstream",
    "PhysicalPort": "TRUE",

    "PortId": "2",
    "SpeedGBps": 4,
    "MaxSpeedGBps": 8,
    "MaxWidth": 8,

    "LinkNetworkTechnology": "Ethernet",
    "LinkState": "Enabled",
    "LinkStatus": "LinkUp",
    "MaxFrameSize": 1518,
    "MaxSpeedGbps": 100,
    "PortMedium": "Electrical",
    "SignalDetected": "true",
    "Width": 4
    }



def get_FabricAdapterPorts_instance(wildcards):

    c = copy.deepcopy(_TEMPLATE)
    d = json.dumps(c)
    g = d.replace('{s_id}', 'NUv')
    g = g.replace('{rb}', 'NUb')
    g = g.replace('{fa_id}', 'NUf')
    g = g.replace('{fap_id}', 'NUp')
    g = g.replace('{{', '~~!')
    g = g.replace('}}', '!!~')
    g = g.replace('{', '~!')
    g = g.replace('}', '!~')
    g = g.replace('NUv', '{s_id}')
    g = g.replace('NUb', '{rb}')
    g = g.replace('NUf', '{fa_id}')
    g = g.replace('NUp', '{fap_id}')
    g = g.format(**wildcards)
    g = g.replace('~~!', '{{')
    g = g.replace('!!~', '}}')
    g = g.replace('~!', '{')
    g = g.replace('!~', '}')
    return json.loads(g)
