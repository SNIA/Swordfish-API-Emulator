# Copyright Notice:
# Copyright 2017 Distributed Management Task Force, Inc. All rights reserved.
# License: BSD 3-Clause License. For full text see link: https://github.com/DMTF/Redfish-Interface-Emulator/LICENSE.md

# get_StorageGroups_instance()

import copy
from flask import json

_TEMPLATE = \
{
  "@Redfish.Copyright": "Copyright 2014-2016 SNIA. All rights reserved.",
  "@odata.context": "{rb}$metadata#StorageGroup.StorageGroup/{sg_id}",
  "@odata.id": "{rb}StorageServices/{s_id}/StorageGroups/{sg_id}",
  "@odata.type": "#StorageGroup_1_0_0.StorageGroup",
  "Id": "{sg_id}",
  "Name": "SG_abc_005",
  "Description": "System SATA",
  "ElementName": "MyGroup",
  "GroupExposed": False,
  "GroupConsistent": True,
  "IOAccessType": "ReadWrite",
  "AccessState": "Active/Optimized",
  "Status": {
    "State": "Enabled",
    "Health": "OK",
    "HealthRollUp": "OK"
  },
  "Actions": {
    "#StorageGroup.ExposeVolumes": {
      "target": "{rb}StorageServices/{s_id}/StorageGroups/{sg_id}/Actions/StorageGroup.ExposeVolumes"
    },
    "#StorageGroup.HideVolumes": {
      "target": "{rb}StorageServices/{s_id}/StorageGroups/{sg_id}/Actions/StorageGroup.HideVolumes"
    }
  },
  "EndpointGroups": [],
  "Volumes": {"@odata.id": "{rb}StorageServices/{s_id}/Volumes"},
  "Links": {
    "ParentStorageGroups": [],
    "ChildStorageGroups": []
    }
}


def get_StorageGroups_instance(wildcards):
    """
    Instantiates and formats the template

    Arguments:
        wildcard - A dictionary of wildcards strings and their repalcement values
    """
    c = copy.deepcopy(_TEMPLATE)
    d = json.dumps(c)
    g = d.replace('{sg_id}', 'NUv')
    g = g.replace('{rb}', 'NUb')
    g = g.replace('{s_id}', 'NUs')
    g = g.replace('{{', '~~!')
    g = g.replace('}}', '!!~')
    g = g.replace('{', '~!')
    g = g.replace('}', '!~')
    g = g.replace('NUv', '{sg_id}')
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