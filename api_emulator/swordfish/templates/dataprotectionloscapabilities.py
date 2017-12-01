# Copyright Notice:
# Copyright 2017 Storage Networking Industry Association (SNIA), USA. All rights reserved.
# License: BSD 3-Clause License. For full SNIA copyright terms, please see http://www.snia.org/about/corporate_info/copyright

# get_DataProtectionLoSCapabilities_instance()

import copy
from flask import json

_TEMPLATE = \
{
  "@Redfish.Copyright": "Copyright 2014-2016 SNIA. All rights reserved.",
  "@odata.context": "{rb}$metadata#DataProtectionLoSCapabilites.DataProtectionLoSCapabilites",
  "@odata.id": "{rb}StorageServices/{s_id}/DataProtectionLoSCapabilites",
  "@odata.type": "#DataProtectionLoSCapabilites_1_0_0.DataProtectionLoSCapabilites",
  "Name": "DataProtectionLoSCapabilites",
  "SupportedRecoveryGeographicObjectives": [
      "Server",
      "Rack",
      "RackGroup",
      "Row",
      "DataCenter",
      "Region"
    ],
  "SupportedRecoveryPointObjectiveTimes": ["PT0S",
  "PT4S",
  "PT1M",
  "PT1H"],
  "SupportedRecoveryObjectiveTimes": ["Immediate",
  "Online",
  "Nearline",
  "Offline"],
  "SupportedReplicaTypes": [
      "Mirror",
    "Snapshot",
      "Clone",
      "TokenizedClone"],
  "MinimumLifetime": "P1M",
  "SupportsIsolated": True,
  "SupportedReplicaOptions": [],
  "SupportedLocations": [],
  "SupportedDataProtectionLinesOfService": [
    {
    "RecoveryGeographicObjective": "Region",
    "RecoveryPointObjective": "P30D",
    "RecoveryTimeObjective": "Nearline",
    "ReplicaType": "Clone",
    "MinLifetime": "P4M",
    "IsIsolated": True,
    "Schedule": {
      "InitialStartTime": "P4M",
      "RecurrenceInterval": "P1M",
      "EnabledDaysOfWeek": ["Sunday"],
      "EnabledDaysOfMonth": [1,
      2,
      3,
      4,
      5,
      6,
      7],
      "EnabledMonthsOfYear": []
    },
    "ReplicaClassOfService": {
      "@odata.id": "/redfish/v1/StorageServices/1/ClassesOfService/Storage/Silver_Providence"
    },
    "ReplicaAccessLocation": {
      "Country": "",
      "Territory": "",
      "State": "",
      "City": "Providence",
      "Address1": "",
      "Address2": "",
      "Address3": "",
      "PostalCode": "",
      "Building": "",
      "Room": "",
      "Row": "",
      "Rack": "",
      "Shelf": "",
      "Item": "",
      "GPSCoords": "",
      "OtherLocationInfo": ""
    }
  }
  
  
  ]
}


def get_DataProtectionLoSCapabilities_instance(wildcards):
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