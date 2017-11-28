# Copyright Notice:
# Copyright 2017 Storage Networking Industry Association (SNIA), USA. All rights reserved.
# License: BSD 3-Clause License. For full SNIA copyright terms, please see http://www.snia.org/about/corporate_info/copyright

# Exceptions thrown in the Emulator

class ConfigurationError(Exception):
    pass

class StaticLoadError(Exception):
    pass

class CreatePooledNodeError(Exception):
    pass

class RemovePooledNodeError(Exception):
    pass

class OVFParseError(Exception):
    pass

class EventSubscriptionError(Exception):
    pass

