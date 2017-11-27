
import json,os,re,sys

from flask import jsonify, request
from flask.ext.restful import Resource
import psutil

from constants import PATHS


def matchvolumes(fpath):
    return True if re.search(r'Volumes/[0-9]+$',fpath) else False

def matchfilesystems(fpath):
    return True if re.search(r'FileSystems/FS[0-9]+$',fpath) else False


class JsonVolumesDataFilterAPI(Resource):

        def __init__(self):
            self.root = PATHS['Root']
    
        def get(self):
            vpath = '{}StorageServices'.format(PATHS['Root'])
            volumes = {}
            for item in os.walk(vpath):
                fpath = item[0]
                # if path matches volume systems
                if matchvolumes(fpath):
                    parentPath = fpath.split("/")[-3]+"_Volumes"
                    currentPath = fpath.split("/")[-1]
                    if not volumes.get(parentPath):
                        volumes[parentPath] = {}                            
                    if os.path.exists(fpath+"/index.json"):
                        with open(fpath+"/index.json", 'r') as json_service_json:
                            data = json.load(json_service_json)
                            reqdata = ['Capacity','CapacitySources','LowSpaceWarningThresholdPercents']
                            for item in reqdata:
                                if data.get(item):
                                    if item == "CapacitySources" or item == "Capacity":
                                        if type(data.get(item)) is dict:
                                            iterlist = data[item]['Data']
                                        elif type(data.get(item)) is list:
                                            if item == "Capacity":
                                                iterlist = data[item][0]['Data']  
                                            elif item == "CapacitySources":
                                                iterlist = data[item][0]
                                                if iterlist.get('ProvidedCapacity'):
                                                    iterlist = iterlist.get('ProvidedCapacity')
                                        for key,val in iterlist.iteritems():
                                            if key in ["ConsumedBytes","AllocatedBytes","GuaranteedBytes","ProvisionedBytes"]:
                                                if not volumes[parentPath].get(currentPath):
                                                    volumes[parentPath][currentPath] = {}
                                                if not volumes[parentPath][currentPath].get(item):
                                                    volumes[parentPath][currentPath][item] = {}            
                                                volumes[parentPath][currentPath][item][key] = val 
                                    elif item == "LowSpaceWarningThresholdPercents":
                                        volumes[parentPath][currentPath]['LowSpaceWarningThresholdPercents'] = data['LowSpaceWarningThresholdPercents']
                elif matchfilesystems(fpath):
                    if os.path.exists(fpath+"/index.json"):
                        with open(fpath+"/index.json", 'r') as json_service_json:
                            data = json.load(json_service_json)
                            
                            #print data
            #print volumes
            return jsonify(volumes)
        




class JsonFSDataFilterAPI(Resource):

        def __init__(self):
            self.root = PATHS['Root']
    
        def get(self):
            fspath = '{}StorageServices'.format(PATHS['Root'])
            file_systems = {}
            for item in os.walk(fspath):
                fpath = item[0]
                # if path matches volume systems
                if matchfilesystems(fpath):                	
                    parentPath = fpath.split("/")[-3]+"_FileSystems"
                    currentPath = fpath.split("/")[-1]
                    print currentPath
                    print parentPath
                    if not file_systems.get(parentPath):
                        file_systems[parentPath] = {}                            
                    if os.path.exists(fpath+"/index.json"):
                        with open(fpath+"/index.json", 'r') as json_service_json:
                            data = json.load(json_service_json)
                            reqdata = ['Capacity','CapacitySources','LowSpaceWarningThresholdPercents']
                            for item in reqdata:
                                if data.get(item):
                                    if item == "CapacitySources" or item == "Capacity":
                                        if type(data.get(item)) is dict:
                                            iterlist = data[item]['Data']
                                        elif type(data.get(item)) is list:
                                            if item == "Capacity":
                                                iterlist = data[item][0]['Data']  
                                            elif item == "CapacitySources":
                                                iterlist = data[item][0]
                                                if iterlist.get('ProvidedCapacity'):
                                                    iterlist = iterlist.get('ProvidedCapacity')
                                        for key,val in iterlist.iteritems():
                                            if key in ["ConsumedBytes","AllocatedBytes","GuaranteedBytes","ProvisionedBytes"]:
                                                if not file_systems[parentPath].get(currentPath):
                                                    file_systems[parentPath][currentPath] = {}
                                                if not file_systems[parentPath][currentPath].get(item):
                                                    file_systems[parentPath][currentPath][item] = {}            
                                                file_systems[parentPath][currentPath][item][key] = val 
                                    elif item == "LowSpaceWarningThresholdPercents":
                                        file_systems[parentPath][currentPath]['LowSpaceWarningThresholdPercents'] = data['LowSpaceWarningThresholdPercents']
                elif matchfilesystems(fpath):
                    if os.path.exists(fpath+"/index.json"):
                        with open(fpath+"/index.json", 'r') as json_service_json:
                            data = json.load(json_service_json)
                            
                            print data
            print file_systems
            return jsonify(file_systems)






