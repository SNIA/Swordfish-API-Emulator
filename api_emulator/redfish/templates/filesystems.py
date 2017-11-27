# Copyright Notice:
# Copyright 2017 Distributed Management Task Force, Inc. All rights reserved.
# License: BSD 3-Clause License. For full text see link: https://github.com/DMTF/Redfish-Interface-Emulator/LICENSE.md

# get_FileSystems_instance()

import copy, requests
from flask import json

_TEMPLATE = \
{
  "@Redfish.Copyright": "Copyright 2014-2016 SNIA. All rights reserved.",
  "@odata.context": "{rb}$metadata#FileSystems.FileSystems",
  "@odata.id": "{rb}StorageServices/{s_id}/FileSystems/{fss_id}",
  "@odata.type": "#FileSystem.FileSystem",
  "Id": "{fss_id}",
  "Name": "Root",
  "Description": "Root FileSystem, not replicated.",
  "BlockSizeBytes": 8192,
  "Capacity": {
    "Data": {
        "ConsumedBytes":     500000000000,
        "AllocatedBytes":   1000000000000,
        "ProvisionedBytes": 3000000000000
    },
    "MetaData": {
        "ConsumedBytes": 0,
        "AllocatedBytes": 0,
        "ProvisionedBytes": 0
    },
    "Snapshot": {
        "ConsumedBytes": 0,
        "AllocatedBytes": 0,
        "ProvisionedBytes": 0
    }
  },
  "CapacitySources": [
    {
        "ProvidedCapacity": {
            "Data": {
                "ConsumedBytes":     500000000000,
                "AllocatedBytes":   1000000000000,
                "ProvisionedBytes": 3000000000000
            },
            "MetaData": {
                "ConsumedBytes": 0,
                "AllocatedBytes": 0,
                "ProvisionedBytes": 0
            },
            "Snapshot": {
                "ConsumedBytes": 0,
                "AllocatedBytes": 0,
                "ProvisionedBytes": 0
            }
        },
        "ProvidedClassOfService": {"@odata.id": "{rb}StorageServices/{s_id}/ClassesOfService/GoldBoston"},
    "ProvidingPools": {"@odata.id": "{rb}StorageServices/{s_id}/StoragePools/SpecialPool/ProvidingPools"}
    }
  ],
  "Links":[],
  "LowSpaceWarningThresholdPercents": [ 60, 90 ],
  "AccessCapabilities": ["read", "Write"],
  "CaseSensitive": False,
  "CasePreserved": False,
  "CharacterCodeSet": ["ASCII", "Unicode"],
  "MaxFileNameLengthBytes": 256,
  "ClusterSizeBytes": 256,
  "FileSystemType": "CIFS",
  "FileSystemPersistenceType": "Persistent",
  "ResizeIncrementBytes": 256,
  "ExportedShares": {"@odata.id": "/redfish/v1/StorageServices/FileService/FileSystems/FS1/ExportedFileShares/MyShare"},
  "Status": {
    "State": "Enabled",
    "Health": "OK",
    "HealthRollUp": "OK"
  },
  "ClassOfService": {
    "Members": [{"@odata.id": "/redfish/v1/StorageServices/FileService/ClassesOfService/GoldBoston"}]
  }
  
}

def get_FileSystems_instance(wildcards):
    """
    Instantiates and formats the template

    Arguments:
        wildcard - A dictionary of wildcards strings and their repalcement values
    """
    c = copy.deepcopy(_TEMPLATE)
    d = json.dumps(c)
    g = d.replace('{fss_id}', 'NUv')    
    g = g.replace('{rb}', 'NUb')
    g = g.replace('{s_id}', 'NUs')
    g = g.replace('{{', '~~!')
    g = g.replace('}}', '!!~')
    g = g.replace('{', '~!')
    g = g.replace('}', '!~')
    g = g.replace('NUv', '{fss_id}')    
    g = g.replace('NUb', '{rb}')
    g = g.replace('NUs', '{s_id}')
    g = g.format(**wildcards)
    g = g.replace('~~!', '{{')
    g = g.replace('!!~', '}}')
    g = g.replace('~!', '{')
    g = g.replace('!~', '}')
    return json.loads(g)
    c['@odata.context'] = c['@odata.context'].format(**wildcards)
    c['@odata.id'] = c['@odata.id'].format(**wildcards)
    c['Id'] = c['Id'].format(**wildcards)
    
    return c
    