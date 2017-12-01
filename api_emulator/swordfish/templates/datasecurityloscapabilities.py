# Copyright Notice:
# Copyright 2017 Storage Networking Industry Association (SNIA), USA. All rights reserved.
# License: BSD 3-Clause License. For full SNIA copyright terms, please see http://www.snia.org/about/corporate_info/copyright

# get_DataSecurityLoSCapabilities_instance()

import copy
from flask import json

_TEMPLATE = \
{
  "@Redfish.Copyright": "Copyright 2014-2016 SNIA. All rights reserved.",
  "@odata.context": "{rb}$metadata#DataSecurityLoSCapabilities.DataSecurityLoSCapabilities",
  "@odata.id": "{rb}StorageServices/{s_id}/DataSecurityLoSCapabilities",
  "@odata.type": "#DataSecurityLoSCapabilities_1_0_0.DataSecurityLoSCapabilities",
  "Name": "DataSecurityLoSCapabilities",
  "SupportedMediaEncryptionStrengthBits": [0, 128, 256],
  "SupportedHostAuthentication": ["Password"],
  "SupportedUserAuthentication": ["None", "Ticket"],
  "SupportedSecureChannel": ["None", "TLS"],
  "SupportedSecureChannelStrengthBits": [0, 128, 256],
  "SupportedAntivirusScanPolicies": [],
  "SupportedAntivirusEngineProviders": [],
  "SupportedDataSanitization": ["None", "Clear", "CryptographicErase"],
    "SupportedDataSecurityLinesOfService": [{
    "MediaEncryptionStrength": "Bits_256",
    "ChannelEncryptionStrength": "Bits_128",
    "HostAuthenticationType": "Ticket",
    "UserAuthenticationType": "Password",
    "SecureChannelProtocol": "TLS",
    "AntivirusScanPolicies": [],
    "AntivirusEngineProvider": None,
    "DataSanitizationPolicy": "CryptographicErase"
  }]
}


def get_DataSecurityLoSCapabilities_instance(wildcards):
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