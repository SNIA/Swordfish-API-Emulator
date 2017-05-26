# Copyright Notice:
# Copyright 2016 Distributed Management Task Force, Inc. All rights reserved.
# License: BSD 3-Clause License. For full text see link: https://github.com/DMTF/Redfish-Interface-Emulator/LICENSE.md

# Resource Dictionary

# Variable to store resource dictionary
resdict = {}

class ResourceDictionary(object):

    def __init__(self):
        print('Init ResourceDictionary.')


    def get_resource(self, path):
        obj = resdict[path].configuration
        return obj

    def get_object(self, path):
        return resdict[path]

    def add_resource(self, path, obj):
        resdict[path] = obj
        return obj

    def delete_resource(self, path):
        del resdict[path]

    def print_dictionary(self):
        for x in resdict:
            print('Key: ')
            print(x)
            print('Value: ')
            print(resdict[x])

