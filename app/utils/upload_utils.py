import string
import random
import os
import flask
from azure.storage.blob import ContainerClient
from flask import current_app,g





class Upload_utils():

    #APP = current_app
    #client = ContainerClient.from_connection_string(APP.config["CONNECTION_STRING"], container_name=APP.config["CONTAINER_NAME"])

    def upload(source, dest):
        '''
        Upload a file or directory to a path inside the container
        '''
        if (os.path.isdir(source)):
            upload_dir(source, dest)
        else:
            upload_file(source, dest)

    def upload_file(source, dest):
        '''
            Upload a single file to a path inside the container
        '''
        print(f'Uploading {source.filename} to {dest}')
        #client.upload_blob(name=dest, data=source)
        #with open(source, 'rb') as data:
            #client.upload_blob(name=dest, data=data)

    def upload_dir(source, dest):
        '''
        Upload a directory to a path inside the container
        '''
        prefix = '' if dest == '' else dest + '/'
        prefix += os.path.basename(source) + '/'
        for root, dirs, files in os.walk(source):
            for name in files:
                dir_part = os.path.relpath(root, source)
                dir_part = '' if dir_part == '.' else dir_part + '/'
                file_path = os.path.join(root, name)
                blob_path = prefix + dir_part + name
                upload_file(file_path, blob_path)
    
    def abort_example(filename):
        if filename not in container:
            abort(404, message="File not found")