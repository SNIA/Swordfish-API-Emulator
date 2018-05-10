"""
 * Copyright (c) 2017, The Storage Networking Industry Association.
 *  
 * Redistribution and use in source and binary forms, with or without 
 * modification, are permitted provided that the following conditions are met:
 *  
 * Redistributions of source code must retain the above copyright notice, 
 * this list of conditions and the following disclaimer.
 *  
 * Redistributions in binary form must reproduce the above copyright notice, 
 * this list of conditions and the following disclaimer in the documentation 
 * and/or other materials provided with the distribution.
 *  
 * Neither the name of The Storage Networking Industry Association (SNIA) nor 
 * the names of its contributors may be used to endorse or promote products 
 * derived from this software without specific prior written permission.
 *  
 *  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
 *  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
 *  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
 *  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE 
 *  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
 *  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
 *  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS  
 *  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
 *  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
 *  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
 *  THE POSSIBILITY OF SUCH DAMAGE.
"""

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