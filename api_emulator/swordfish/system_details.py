import json

from flask import jsonify, request
from flask.ext.restful import Resource
import psutil

from .constants import PATHS


class SystemDetailsAPI(Resource):
    def get(self):
        details = psutil.virtual_memory()
        data = {
            'total_disk_space': details.total,
            'available_space': details.available,
            'used_space': details.used,
            'percentage_used': details.percent
        }

        return jsonify(data)


class SystemMemoryDetailsAPI(Resource):

    def __init__(self):
        self.root = PATHS['Root']

    def get(self):
	
        path = '{}StorageServices/FileService/StoragePools/BasePool/index.json'.format(PATHS['Root'])
        try:
            details = open(path)
            data = json.load(details)
            data = data['CapacitySources'][0]['ProvidedCapacity']
            c = {}
            for k, v in data.items():
                if k == "AllocatedBytes" and data['AllocatedBytes']:
                    c['total'] = data['AllocatedBytes']
                if k == "ConsumedBytes" and data['ConsumedBytes']:
                    c['consumed'] = data['ConsumedBytes']

            c['remaining'] = c['total'] - c['consumed']

        except Exception as e:
            return {"error": "Unable to read file because of following error::{}".format(e)}, 500

        return jsonify(c)



class AddServiceAPI(Resource):
    def __init__(self):
        self.root = PATHS['Root']
	
    def get(self):
	
        path = '{}AddService/IPAddress.json'.format(PATHS['Root'])
	

        try:
            with open(path, 'r') as add_service_json:
                data = json.load(add_service_json)
                add_service_json.close()

        except Exception as e:
            return {"error": "Unable to read file because of following error::{}".format(e)}, 500

        return jsonify(data)    

      
     
    
    def post(self):
        
        path = '{}AddService/IPAddress.json'.format(PATHS['Root'])
        
        
        try:
            with open(path,"r") as pdata:
                pdata = json.load(pdata)
            data = json.loads(request.data)
            #print request.data
            pdata["Device"].append({"IPAddress":data["IPAddress"],"url":"http://"+data["IPAddress"]+":5000/redfish/v1/"})
			
            
            with open(path,"w") as jdata:                
                
                json.dump(pdata,jdata)

                   
        except Exception as e:
            return {"error": "Unable to read file because of following error::{}".format(e)}, 500

        return jsonify(pdata)





