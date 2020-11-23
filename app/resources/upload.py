from flask import Flask, current_app
from flask_restful import Api, Resource, reqparse, request, abort
import werkzeug
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import string
import random
import os
from azure.storage.blob import ContainerClient
import uuid
from app.utils.upload_utils import Upload_utils




parser = reqparse.RequestParser()
parser.add_argument("name", type=str, help="Name for the picture required", required=True)
parser.add_argument("description", type=str, help="Image description required",required=True)
parser.add_argument("file", type=werkzeug.datastructures.FileStorage, location='files', required=True)
#container = "testfileblob"

id = uuid.uuid1()

#APP = current_app
#client = ContainerClient.from_connection_string(APP.config["CONNECTION_STRING"], container_name=APP.config["CONTAINER_NAME"])

class Upload(Resource):
    
    #APP = current_app
    #client = ContainerClient.from_connection_string(APP.config["CONNECTION_STRING"], container_name=APP.config["CONTAINER_NAME"])
    #up_u = Upload_utils(APP)

    def post(self):
        args = parser.parse_args()
        file = args["file"]
        #filename = args["name"]
        filename = str(id)+secure_filename(file.filename)
        saved = file.read()
       # up_u.upload(saved, filename, client)
        return {"File": "Uploaded"}