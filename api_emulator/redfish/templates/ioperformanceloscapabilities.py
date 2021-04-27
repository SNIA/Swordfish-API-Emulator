#
# Copyright (c) 2017-2021, The Storage Networking Industry Association.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# Neither the name of The Storage Networking Industry Association (SNIA) nor
# the names of its contributors may be used to endorse or promote products
# derived from this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
#  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
#  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
#  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
#  THE POSSIBILITY OF SUCH DAMAGE.
#

# get_IOPerformanceLoSCapabilities_instance()

import copy
from flask import json

_TEMPLATE = \
{
  "@Redfish.Copyright": "Copyright 2014-2021 SNIA. All rights reserved.",
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
