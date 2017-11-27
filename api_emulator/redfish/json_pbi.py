import json

from flask import jsonify, request
from flask.ext.restful import Resource
import psutil, constants

from constants import PATHS




class JsonVolDataAPI(Resource):

        def __init__(self):
            self.root = PATHS['Root']
    
        def get(self):
    
            path = '{}StorageServices/1/Volumes/4/index.json'.format(PATHS['Root'])
            print path
        
        
            try:
                with open(path, 'r') as add_json_data_json:
                    data = json.load(add_json_data_json)
                    add_json_data_json.close()                
                
                finalcapacity = {}
                if data.get('Capacity'):  
                    if type(data.get('Capacity')) is list:
                        for key,val in (data['Capacity'][0]['Data']).iteritems():
                            finalcapacity["Capacity_Data_"+key] = val 
                    else:
                        for key,val in (data['Capacity']['Data']).iteritems():
                            finalcapacity["Capacity_Data_"+key] = val 
                print finalcapacity
                if data.get('CapacitySources'):  
                    if type(data.get('CapacitySources')) is list:
                        for key,val in (data['CapacitySources'][0]['ProvidedCapacity']).iteritems():
                            finalcapacity["CapacitySources_ProvidedCapacity_"+key] = val 
                    else:
                        for key,val in (data['CapacitySources']['ProvidedCapacity']).iteritems():
                            finalcapacity["CapacitySources_ProvidedCapacity_"+key] = val 
                print finalcapacity
            except Exception as e:
                return {"error": "Unable read file because of following error::{}".format(e)}, 500

            return jsonify(finalcapacity)


class JsonSPDataAPI(Resource):

        def __init__(self):
            self.root = PATHS['Root']
    
        def get(self):
    
            path = '{}StorageServices/1/StoragePools/BasePool/index.json'.format(PATHS['Root'])
            print path
        
        
            try:
                with open(path, 'r') as add_service_json:
                    data = json.load(add_service_json)
                    add_service_json.close()
                

                finalcapacity = {}
                if data.get('Capacity'):  
                    if type(data.get('Capacity')) is list:
                        for key,val in (data['Capacity'][0]['Data']).iteritems():
                            finalcapacity["Capacity_Data_"+key] = val 
                    else:
                        for key,val in (data['Capacity']['Data']).iteritems():
                            finalcapacity["Capacity_Data_"+key] = val 
                print finalcapacity
                if data.get('CapacitySources'):  
                    if type(data.get('CapacitySources')) is list:
                        for key,val in (data['CapacitySources'][0]['ProvidedCapacity']).iteritems():
                            finalcapacity["CapacitySources_ProvidedCapacity_"+key] = val 
                    else:
                        for key,val in (data['CapacitySources']['ProvidedCapacity']).iteritems():
                            finalcapacity["CapacitySources_ProvidedCapacity_"+key] = val 
                print finalcapacity
            except Exception as e:
                return {"error": "Unable read file because of following error::{}".format(e)}, 500

            return jsonify(finalcapacity)

class JsonFSDataAPI(Resource):

        def __init__(self):
            self.root = PATHS['Root']
    
        def get(self):
    
            path = '{}StorageServices/FileService/FileSystems/FS3/index.json'.format(PATHS['Root'])
            print path
        
        
            try:
                with open(path, 'r') as add_json_data_json:
                    data = json.load(add_json_data_json)
                    add_json_data_json.close()
                

                finalcapacity = {}
                
                if data.get('Capacity'):  
                    if type(data.get('Capacity')) is list:
                        for key,val in (data['Capacity'][0]['Data']).iteritems():
                            finalcapacity["Capacity_Data_"+key] = val 
                    else:
                        for key,val in (data['Capacity']['Data']).iteritems():
                            finalcapacity["Capacity_Data_"+key] = val 

                if data.get('LowSpaceWarningThresholdPercents'):                    
                    if type(data.get('LowSpaceWarningThresholdPercents')) is list:                        
                        finalcapacity["LowSpaceWarningThresholdPercents"] = data['LowSpaceWarningThresholdPercents']                    
                
                if data.get('CapacitySources'):  
                    if type(data.get('CapacitySources')) is list:
                        for key,val in (data['CapacitySources'][0]['ProvidedCapacity']['Data']).iteritems():
                            finalcapacity["CapacitySources_ProvidedCapacity_Data_"+key] = val 
                    else:
                        for key,val in (data['CapacitySources']['ProvidedCapacity']['Data']).iteritems():
                            finalcapacity["CapacitySources_ProvidedCapacity_Data_"+key] = val 
                if data.get('CapacitySources'):  
                    if type(data.get('CapacitySources')) is list:
                        for key,val in (data['CapacitySources'][0]['ProvidedCapacity']['MetaData']).iteritems():
                            finalcapacity["CapacitySources_ProvidedCapacity_MetaData_"+key] = val 
                    else:
                        for key,val in (data['CapacitySources']['ProvidedCapacity']['MetaData']).iteritems():
                            finalcapacity["CapacitySources_ProvidedCapacity_MetaData_"+key] = val
                if data.get('CapacitySources'):  
                    if type(data.get('CapacitySources')) is list:
                        for key,val in (data['CapacitySources'][0]['ProvidedCapacity']['Snapshot']).iteritems():
                            finalcapacity["CapacitySources_ProvidedCapacity_Snapshot_"+key] = val 
                    else:
                        for key,val in (data['CapacitySources']['ProvidedCapacity']['Snapshot']).iteritems():
                            finalcapacity["CapacitySources_ProvidedCapacity_Snapshot_"+key] = val

                print finalcapacity
            except Exception as e:
                return {"error": "Unable read file because of following error::{}".format(e)}, 500

            return jsonify(finalcapacity)