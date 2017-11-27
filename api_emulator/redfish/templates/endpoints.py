# Copyright Notice:
# Copyright 2017 Distributed Management Task Force, Inc. All rights reserved.
# License: BSD 3-Clause License. For full text see link: https://github.com/DMTF/Redfish-Interface-Emulator/LICENSE.md

# get_Endpoints_instance()

import copy
from flask import json

_TEMPLATE = \
{
  "@Redfish.Copyright": "Copyright 2014-2017 SNIA. All rights reserved.",
  "@odata.context": "{rb}$metadata#Endpoint.Endpoint",
  "@odata.id": "{rb}StorageServices/{s_id}/Endpoints/{ep_id}",
  "@odata.type": "#Endpoint.v1_0_0.Endpoint",
  "Description": "This instance represents a SCSI implemented over FC",
  "Name": "SCSI2",
  "Status": {
    "State": "Enabled",
    "Health": "Degraded"
  },
  "Identifiers": [
    {
      "DurableName": "60123456789abcdef60123456789abcdef",
      "DurableNameFormat": "NAA"
    }
  ],
  "BroadcastResetSupported": False,
  "EndpointRole": "Target",
  "RelativePortIdentifier": 3,
  "TargetPortGroupIdentifier": 1,
  "SupportingEndpoints": [
    {
      "ConnectionID": None,
      "ConnectedEndpoint": {
        "@odata.id": "{rb}StorageServices/{s_id}/Endpoints/{ep_id}"
      }
    }
  ]
}


def get_Endpoints_instance(wildcards):
    """
    Instantiates and formats the template

    Arguments:
        wildcard - A dictionary of wildcards strings and their repalcement values
    """
    c = copy.deepcopy(_TEMPLATE)
    d = json.dumps(c)
    g = d.replace('{ep_id}', 'NUv')
    g = g.replace('{rb}', 'NUb')
    g = g.replace('{s_id}', 'NUs')
    g = g.replace('{{', '~~!')
    g = g.replace('}}', '!!~')
    g = g.replace('{', '~!')
    g = g.replace('}', '!~')
    g = g.replace('NUv', '{ep_id}')
    g = g.replace('NUb', '{rb}')
    g = g.replace('NUs', '{s_id}')
    g = g.format(**wildcards)
    g = g.replace('~~!', '{{')
    g = g.replace('!!~', '}}')
    g = g.replace('~!', '{')
    g = g.replace('!~', '}')
    return json.loads(g)
    # c['@odata.context'] = c['@odata.context'].format(**wildcards)
    # c['@odata.id'] = c['@odata.id'].format(**wildcards)
    # c['Id'] = c['Id'].format(**wildcards)
    #
    # return c