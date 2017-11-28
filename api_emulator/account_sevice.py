# Copyright Notice:
# Copyright 2017 Storage Networking Industry Association (SNIA), USA. All rights reserved.
# License: BSD 3-Clause License. For full SNIA copyright terms, please see http://www.snia.org/about/corporate_info/copyright

# Redfish Emulator Role Service.
#   Temporary version, to be removed when AccountService goes dynamic

class AccountService(object):

    def __init__(self):
        self._accounts = { 'Administrator': 'Password',
                           'User': 'Password' }
        self._roles = { 'Administrator': 'Admin',
                        'User': 'ReadOnlyUser' }

    def checkPriviledgeLevel(self, user, level):
        if self._roles[user] == level:
            return True
        else:
            return False

    def getPassword(self, username):
        if self._accounts.has_key(username):
            return self._accounts[username]
        else:
            return None

    def checkPrivilege(self, privilege, username, errorResponse):
        def wrap(func):
            def inner(*args, **kwargs):
                if self.checkPriviledgeLevel(username(), privilege):
                    return func(*args, **kwargs)
                else:
                    return errorResponse()
            return inner
        return wrap
