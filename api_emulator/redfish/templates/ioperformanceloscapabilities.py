# Copyright Notice:
# Copyright 2017 Distributed Management Task Force, Inc. All rights reserved.
# License: BSD 3-Clause License. For full text see link: https://github.com/DMTF/Redfish-Interface-Emulator/LICENSE.md

# get_IOPerformanceLoSCapabilities_instance()

import copy
from flask import json

_TEMPLATE = \
{
  "@Redfish.Copyright": "Copyright 2014-2016 SNIA. All rights reserved.",
  "@odata.context": "{rb}$metadata#IOPerformanceLoSCapabilities.IOPerformanceLoSCapabilities",
  "@odata.id": "{rb}StorageServices/{s_id}/IOPerformanceLoSCapabilities",
  "@odata.type": "#IOPerformanceLoSCapabilities_1_0_0.IOPerformanceLoSCapabilities",  
  "Name": "IOPerformanceLoSCapabilities",
  "IoOperationsPerSecondLimitingIsSupported": True,
  "MinSamplePeriod": "PT5S",
  "MaxSamplePeriod": "PT1H",
  "MaxIoOperationsPerSecondPerTerabyte": 1000,
  "MinAverageIoOperationLatencyMicroseconds": 200,
  "SupportedIOWorkloads": [{
    "Name": "Duplicon:DSS"
  },
  {
    "Name": "Duplicon:OLTP"
  },
  {
    "Name": "Duplicon:Streaming",
    "Components": [{
      "AccessPattern ": "SequentialRead",
      "AverageIOBytes ": 8192,
      "PercentOfData ": 66,
      "PercentOfIOPS ": 33
    },
    {
      "AccessPattern ": "SequentialWrite",
      "AverageIOBytes ": 4096,
      "PercentOfData ": 33,
      "PercentOfIOPS ": 66
    }]
  }],
  "SupportedIOPerformanceLinesOfService": [{
    "IoOperationsPerSecondIsLimitedBoolean": False,
    "SamplePeriod": "PT1M",
    "MaxIoOperationsPerSecondPerTerabyte": 83,
    "AverageIoOperationLatencyMicroseconds": 8000,
    "IOWorkload": {
      "Name": "Duplicon: OLTP"
    }
  },
  {
    "IoOperationsPerSecondIsLimitedBoolean": "false",
    "SamplePeriod": "PT1M",
    "MaxIoOperationsPerSecondPerTerabyte": 133,
    "AverageIoOperationLatencyMicroseconds": 5000,
    "IOWorkload": {
      "Name": "Duplicon: OLTP"
    }
  }]
}


def get_IOPerformanceLoSCapabilities_instance(wildcards):
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