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
from app.utils.create_article import CreateArticle




parser = reqparse.RequestParser()
parser.add_argument("title", type=str, help="title required", required=True)
parser.add_argument("highlight", type=bool, help="highlight",required=True)
parser.add_argument("description", type=str, help="description required",required=True)
parser.add_argument("timestamp", type=str, help="timestamp required",required=True)
parser.add_argument("bannerImgUrl", type=str, help="bannerimng required",required=True)
#parser.add_argument("description", type=str, help="description required",required=True)
#parser.add_argument("description", type=str, help="description required",required=True)
#parser.add_argument("description", type=str, help="description required",required=True)
#parser.add_argument("description", type=str, help="description required",required=True)
parser.add_argument("paragraphs", type=dict, help="paragraphs required",required=True)



id = uuid.uuid1()

class UploadArticle(Resource):

    def post(self):
        create = CreateArticle()
        args = parser.parse_args()
        print(args)
        data = create.create_newsitem()
        return data["highlight"]
        