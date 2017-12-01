# Copyright Notice:
# Copyright 2017 Storage Networking Industry Association (SNIA), USA. All rights reserved.
# License: BSD 3-Clause License. For full SNIA copyright terms, please see http://www.snia.org/about/corporate_info/copyright

# get_ClassesOfService_instance()

import copy
from flask import json

_TEMPLATE = \
{
  "@Redfish.Copyright": "Copyright 2014-2016 SNIA. All rights reserved.",
  "@odata.context": "{rb}$metadata#StorageServices/{s_id}/ClassesOfService/{clos_id}",
  "@odata.id": "{rb}StorageServices/{s_id}/ClassesOfService/{clos_id}",
  "@odata.type": "#ClassOfService_1_0_0.ClassOfService",
  "Id": "{clos_id}",
  "Name": "GoldBoston",
  "Description": "Gold class of service in Boston",
  "ClassOfServiceVersion": "01.00.00",
  "LinesOfService": {
      "IOConnectivityLineOfService": {
        "Name": "FiberChannel",
        "AccessProtocol": "FC",
        "MaxSupportedIoOperationsPerSecond": None
      },
      "IOPerformanceLineOfService": {
        "Name": "Lite-OLTP-HDD",
        "IoOperationsPerSecondIsLimitedBoolean": "false",
        "SamplePeriod": "PT1M",
        "MaxIoOperationsPerSecondPerTerabyte": 133,
        "AverageIoOperationLatencyMicroseconds": 5000,
        "IOWorkload": {
            "Name": "Duplicon:OLTP"
        }
      },
      "DataProtectionLineOfService": [],
      "DataSecurityLineOfService": {
        "Name": "SecureData",
        "MediaEncryptionStrength": "Bits_256",
        "ChannelEncryptionStrength": "Bits_128",
        "HostAuthenticationType": "Ticket",
        "UserAuthenticationType": "Password",
        "SecureChannelProtocol": "TLS",
        "AntivirusScanPolicies": [],
        "AntivirusEngineProvider": None,
        "DataSanitizationPolicy": "CryptographicErase"
      },
      "DataStorageLineOfService": {
        "Name": "HA-Thin",
        "RecoveryTimeObjective": 0,
        "ProvisioningPolicy": "Thin",
        "SpaceEfficient": True
      }
  }
}


def get_ClassesOfService_instance(wildcards):
    """
    Instantiates and formats the template

    Arguments:
        wildcard - A dictionary of wildcards strings and their repalcement values
    """
    c = copy.deepcopy(_TEMPLATE)
    d = json.dumps(c)
    g = d.replace('{clos_id}', 'NUv')
    g = g.replace('{rb}', 'NUb')
    g = g.replace('{s_id}', 'NUs')
    g = g.replace('{{', '~~!')
    g = g.replace('}}', '!!~')
    g = g.replace('{', '~!')
    g = g.replace('}', '!~')
    g = g.replace('NUv', '{clos_id}')
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