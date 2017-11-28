# Copyright Notice:
# Copyright 2017 Storage Networking Industry Association (SNIA), USA. All rights reserved.
# License: BSD 3-Clause License. For full SNIA copyright terms, please see http://www.snia.org/about/corporate_info/copyright

# get_Volumes_instance()

import copy
from flask import json

_TEMPLATE = \
{
  "@Redfish.Copyright": "Copyright 2014-2016 SNIA. All rights reserved.",
  "@odata.context": "{rb}$metadata#Volume.Volume",
  "@odata.id": "{rb}StorageServices/{s_id}/Volumes/{v_id}",
  "@odata.type": "#VolumeCollection_1_0_0.VolumeCollection",
  "Name": "Volumes",
  "Members@odata.count": 6,
  "Description": "",
  "Id": '{v_id}',
  "Identifiers": [
    {
      "DurableNameFormat": "NAA6",
      "DurableName": "65456765456761001244076100123487"
    }
  ],
  "Manufacturer": "SuperDuperSSD",
  "Model": "Drive Model string",
  "Status": {
    "State": "Enabled",
    "Health": "OK"
  },
  "AccessCapabilities": [
    "Read",
    "Write",
    "Append",
    "Streaming"
  ],
  "BlockSizeBytes": 512,
  "LowSpaceWarningThresholdPercent": [
    70,
    80,
    90 ],
  "CapacitySources": [
    {
      "ConsumedBytes": 0,
      "AllocatedBytes": 10737418240,
      "GuaranteedBytes": 536870912,
      "ProvisionedBytes": 1099511627776,
      "Links": {
        "ClassOfService": {
          "@odata.id": "{rb}StorageServices/{s_id}/ClassesOfService/SilverBoston"
        },
        "ProvidingPool": {
            "Members": [{"@odata.id": "{rb}StorageServices/{s_id}/StoragePools/SpecialPool"}]
        },
        "StorageGroups": {
    "@odata.id": "{rb}StorageServices/{s_id}/Volumes/{v_id}/StorageGroups"
       },
        "ProvidingVolume": None,
        "AllocatedPools": None
        
        }
    }],
  
  "Capacity":[
     {
    "Data": {
      "ConsumedBytes": 0,
      "AllocatedBytes": 10737418240,
      "GuaranteedBytes": 536870912,
      "ProvisionedBytes": 1099511627776
    },
    "Metadata": {
      "ConsumedBytes": 536870912,
      "AllocatedBytes": 536870912
    },
    "Snapshots": {
      "ConsumedBytes": 0,
      "AllocatedBytes": 21474836480,
      "GuaranteedBytes": 536870912,
      "ProvisionedBytes": 2199023255552
    }
  }
],
  "ReplicaInfos": [{
  "ReplicaState": "Synchronized",
  "ReplicaProgressStatus": "Completed",
  "ReplicaRole": "Target",
  "@odata.id": {
    "Replica": "{rb}StorageServices/{s_id}/Volumes/{v_id}"
  }
  }],
  "Permissions": [
              {"Read": "True"},
              {"Write": "True"}]
  
 
}


def get_Volumes_instance(wildcards):
    """
    Instantiates and formats the template

    Arguments:
        wildcard - A dictionary of wildcards strings and their repalcement values
    """
    c = copy.deepcopy(_TEMPLATE)
    d = json.dumps(c)
    g = d.replace('{v_id}', 'NUv')
    g = g.replace('{rb}', 'NUb')
    g = g.replace('{s_id}', 'NUs')
    g = g.replace('{{', '~~!')
    g = g.replace('}}', '!!~')
    g = g.replace('{', '~!')
    g = g.replace('}', '!~')
    g = g.replace('NUv', '{v_id}')
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