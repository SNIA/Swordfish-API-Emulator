import g

import sys, traceback
import logging
import copy
from flask import Flask, request, make_response, render_template
from flask_restful import reqparse, Api, Resource


from templates.StorageServices import get_StorageServices_instance



class SampleAPI(Resource):

    def __init__(self):
        print "ahshg"
        try:
            global config
            
            #wildcards = kwargs
            config=get_StorageServices_instance({'rb':'redfish/v1','id':1})
            print config
            print "12"
            resp = config, 200
        except Exception:
            traceback.print_exc()

    def get(self,ident):
        
        try:
            storageservices_json = open('/redfish/v1/StorageServices/1')
            data = json.load(storageservices_json)
            resp = 404
            if ident in members:
                resp = members[ident], 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        return resp
           


