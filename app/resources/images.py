from flask import Flask, current_app
from flask_restful import Api, Resource, reqparse, request, abort
import werkzeug
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import string
import random
import os
from azure.storage.blob import ContainerClient, generate_blob_sas, BlobSasPermissions

import uuid
from datetime import datetime, timedelta

parser = reqparse.RequestParser()
parser.add_argument("blob", type=str, help="Name of the blob needed", required=True)
container_name = current_app.config["CONTAINER_NAME"]
account_name = current_app.config["STORAGE_ACCOUNT"]
account_key = current_app.config["STORAGE_KEY"]
container_client = ContainerClient.from_connection_string(current_app.config["CONNECTION_STRING"], container_name=container_name)
client = container_client
id = uuid.uuid1()

class Images(Resource):
    def get(self):
        args = parser.parse_args()
        image = args["blob"]
        url = get_img_url_with_blob_sas_token(image)      
        return {"Image": url}

def get_img_url_with_blob_sas_token(blob_name):
    blob_sas_token = generate_blob_sas(
        account_name=account_name,
        container_name=container_name,
        blob_name=blob_name,
        account_key=account_key,
        permission=BlobSasPermissions(read=True),
        expiry=datetime.utcnow() + timedelta(hours=1)
    )
    blob_url_with_blob_sas_token = f"https://{account_name}.blob.core.windows.net/{container_name}/{blob_name}?{blob_sas_token}"
    return blob_url_with_blob_sas_token

    
def abort_example(image):
    if filename not in container:
        abort(404, message="File not found")
    