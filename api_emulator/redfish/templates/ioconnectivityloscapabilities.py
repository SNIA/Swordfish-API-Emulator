# Copyright Notice:
# Copyright 2017 Distributed Management Task Force, Inc. All rights reserved.
# License: BSD 3-Clause License. For full text see link: https://github.com/DMTF/Redfish-Interface-Emulator/LICENSE.md

# get_IOConnectivityLoSCapabilities_instance()

import copy
from flask import json

_TEMPLATE = \
{
  "@Redfish.Copyright": "Copyright 2014-2017 SNIA. All rights reserved.",
  "@odata.context": "{rb}$metadata#IOConnectivityLoSCapabilities.IOConnectivityLoSCapabilities",
  "@odata.id": "{rb}StorageServices/{s_id}/IOConnectivityLoSCapabilities",
  "@odata.type": "#IOConnectivityLoSCapabilities_1_0_0.IOConnectivityLoSCapabilities",
  "Name": "IOConnectivityLoSCapabilities",
  "SupportedAccessProtocols": ["FC","SCSI"],
  "MaxSupportedIoOperationsPerSecond": 1000,
    "SupportedIOConnectivityLinesOfService": [{
    "AccessProtocol": "FC",
    "MaxSupportedIoOperationsPerSecond": None
  }]
}


def get_IOConnectivityLoSCapabilities_instance(wildcards):
    """
    Instantiates and formats the template

    Arguments:
        wildcard - A dictionary of wildcards strings and their repalcement values
    """
    c = copy.deepcopy(_TEMPLATE)
    d = json.dumps(c)    
    g = d.replace('{rb}', 'NUb')
    g = g.replace('{s_id}', 'NUs')
    g = g.replace('{{', '~~!')
    g = g.replace('}}', '!!~')
    g = g.replace('{', '~!')
    g = g.replace('}', '!~')    
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