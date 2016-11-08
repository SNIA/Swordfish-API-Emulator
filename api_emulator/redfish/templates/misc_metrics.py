#
# Copyright (c) 2016 Intel Corporation. All Rights Reserved.
# Copyright (c) 2016, The Storage Networking Industry Association.
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. 
#
# Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
#
# Neither the name of The Storage Networking Industry Association (SNIA) nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

"""
MiscMetrics template
"""
from api_emulator.utils import timestamp

_TEMPLATE = \
    {
        "@odata.context": "{rb}$metadata#Chassis/Links/Members/{id}/Links/MiscMetrics/$entity",
        "@odata.id": "{rb}Chassis/{id}/MiscMetrics",
        "@odata.type": "#MiscMetrics.1.0.0.MiscMetrics",
        "Id": "MiscMetrics",
        "Name": "Misc Metrics",
        "Modified": None,
        "Intrusion": [
            {
                "Name": "Sensor ID String",
                "SensorType": "Physical(Chassis) Security",
                "Number": "EntityInstance",
                "Status": {
                    "State": "Enabled",
                    "Health": "OK"
                },
                "CurrentReading": "open"
            }
        ]
    }


def get_misc_metrics_template(rest_base, ident):
    """
    Returns a formatted template

    Arguments:
        rest_base - Base URL of the RESTful interface
        ident     - Identifier of the chassis
    """
    c = _TEMPLATE.copy()
    c['@odata.context'] = c['@odata.context'].format(rb=rest_base, id=ident)
    c['@odata.id'] = c['@odata.id'].format(rb=rest_base, id=ident)
    c['Modified'] = timestamp()
    return c
