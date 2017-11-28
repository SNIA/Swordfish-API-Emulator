# Copyright Notice:
# Copyright 2017 Storage Networking Industry Association (SNIA), USA. All rights reserved.
# License: BSD 3-Clause License. For full SNIA copyright terms, please see http://www.snia.org/about/corporate_info/copyright

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

