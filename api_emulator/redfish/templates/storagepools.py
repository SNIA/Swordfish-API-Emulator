# Copyright Notice:
# Copyright 2017 Storage Networking Industry Association (SNIA), USA. All rights reserved.
# License: BSD 3-Clause License. For full SNIA copyright terms, please see http://www.snia.org/about/corporate_info/copyright

# get_StoragePools_instance()

import copy
from flask import json

_TEMPLATE = \
{
  "@Redfish.Copyright": "Copyright 2014-2016 SNIA. All rights reserved.",
  "@odata.context": "{rb}$metadata#StoragePool.StoragePool/{sp_id}",
  "@odata.id": "{rb}StorageServices/{s_id}/StoragePool/{sp_id}",
  "@odata.type": "#StoragePool_1_0_0.StoragePool",
  "Id": "{sp_id}",
  "Name": "",
  "Description": "System Storage pool",
  "BlockSizeBytes": 8192,
  "Capacity": {
    "Data": {
      "ConsumedBytes": 0,
      "AllocatedBytes": 0,
      "GuaranteedBytes": 0,
      "ProvisionedBytes": 0
    },
    "Metadata": 0,
    "Snapshot": 0
  },
  "CapacitySources": [
    {
      "ProvidedCapacity": {
        "ConsumedBytes": 70368744177664,
        "AllocatedBytes": 140737488355328,
        "GuaranteedBytes": 17592186044416,
        "ProvisionedBytes": 562949953421312
      },
      "Links": {
        "ClassOfService": {
          "@odata.id": "/redfish/v1/StorageServices/1/ClassesOfService/GoldBoston"
        },
        "ProvidingPool":0,
        "ProvidingVolume": 0
      }
    }
  ],
  "LowSpaceWarningThresholdPercents": [
    70,
    80,
    90
  ],
  "Status": {
    "State": "Enabled",
    "Health": "OK",
    "HealthRollUp": "OK"
  },
  "Links": [],  
  "AllocatedPools": [],
  "ClassesOfService": {"@odata.id": "/redfish/v1/StorageServices/1/StoragePools/BasePool/ClassesOfService"},
  "AllocatedVolumes": [{"@odata.id": "/redfish/v1/StorageServices/1/StoragePools/BasePool/Volumes"}],
  
}
  
 





def get_StoragePools_instance(wildcards):
    """
    Instantiates and formats the template

    Arguments:
        wildcard - A dictionary of wildcards strings and their repalcement values
    """
    c = copy.deepcopy(_TEMPLATE)
    d = json.dumps(c)
    g = d.replace('{sp_id}', 'NUv')
    g = g.replace('{rb}', 'NUb')
    g = g.replace('{s_id}', 'NUs')
    g = g.replace('{{', '~~!')
    g = g.replace('}}', '!!~')
    g = g.replace('{', '~!')
    g = g.replace('}', '!~')
    g = g.replace('NUv', '{sp_id}')
    g = g.replace('NUb', '{rb}')
    g = g.replace('NUs', '{s_id}')
    g = g.format(**wildcards)
    g = g.replace('~~!', '{{')
    g = g.replace('!!~', '}}')
    g = g.replace('~!', '{')
    g = g.replace('!~', '}')
    return json.loads(g)
    #c['@odata.context'] = c['@odata.context'].format(**wildcards)
    #c['@odata.id'] = c['@odata.id'].format(**wildcards)
    #c['Id'] = c['Id'].format(**wildcards)
    
    

    #return c