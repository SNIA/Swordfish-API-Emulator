# Copyright Notice:
# Copyright 2017 Storage Networking Industry Association (SNIA), USA. All rights reserved.
# License: BSD 3-Clause License. For full SNIA copyright terms, please see http://www.snia.org/about/corporate_info/copyright

# get_DataStorageLoSCapabilities_instance()

import copy
from flask import json

_TEMPLATE = \
{
  "@Redfish.Copyright": "Copyright 2014-2016 SNIA. All rights reserved.",
  "@odata.context": "{rb}$metadata#DataStorageLoSCapabilities.DataStorageLoSCapabilities",
  "@odata.id": "{rb}StorageServices/{s_id}/DataStorageLoSCapabilities",
  "@odata.type": "#DataStorageLoSCapabilities_1_0_0.DataStorageLoSCapabilities",
  "Name": "DataStorageLoSCapabilities",
  "SupportedAccessCapabilities": ["Read",
  "Write"],
  "SupportedRecoveryTimeObjectives": ["Immediate",
  "Online",
  "Nearline",
  "Offline"],
  "SupportedLocations": [],
  "SupportedSpaceGuaranteed": True,
  "SupportedSpaceEfficient": True,
    "SupportedDataStorageLinesOfService": [{
    "RecoveryTimeObjective": 0,
    "ProvisioningPolicy": "Thin",
    "SpaceEfficient": True
  }]
}


def get_DataStorageLoSCapabilities_instance(wildcards):
    """s_id
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