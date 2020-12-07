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
from app.utils.create_article import CreateArticle
from app.utils.article_dicts import ArticleDicts


parser = reqparse.RequestParser()
parser.add_argument("title", type=str, help="title required", required=True)
parser.add_argument("highlight", type=bool, help="highlight", required=True)
parser.add_argument("description", type=str,
                    help="description required", required=True)
parser.add_argument("timestamp", type=str,
                    help="timestamp required", required=True)
parser.add_argument("bannerImgUrl", type=str,
                    help="bannerimng required", required=True)
#parser.add_argument("description", type=str, help="description required",required=True)
#parser.add_argument("description", type=str, help="description required",required=True)
#parser.add_argument("description", type=str, help="description required",required=True)
#parser.add_argument("description", type=str, help="description required",required=True)
parser.add_argument("paragraphs", type=dict,
                    help="paragraphs required", required=True)


id = uuid.uuid1()


class UploadArticle(Resource):
    # Add token check for security? or secret key in this case 
    #articles = ArticleDicts()
    #newsItems = articles.newsItems

    def post(self):
        #create = CreateArticle()
        #args = parser.parse_args()
        #items = []
        #for item in self.newsItems:
            #create.setData(item)
            #newsitem = create.create_newsitem()
            #items.append(newsitem)
        return {"Error": "not in use right now"}
