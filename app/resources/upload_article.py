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

    data = {
        "title": "Welcome to Nokia Finland Christmas Session on December 10",
        "author": {
            "id": 1,
            "displayName": "Maki, Tuuli-Maria (Nokia - FI/Espoo)",
            "email": "tuuli-maria.maki@nokia.com",
            "department": "MN L1 Espoo TC",
            "jobtitle": "Campus Communication trainee"
        },
        "highlight": True,
        "description":
        "Welcome to Christmas Session with stand-up comedian & TV host Jaakko Saariluoma on Dec 10",
        "timestamp": "2020-11-27",
        "headerImgUrl": "Welcome to Christmas Session with stand-up comedian & TV host Jaakko Saariluoma on Dec 10 .jpg",
        "headerImgTitle": "Open internal positions in Espoo",
        "paragraphs": {
            "1": {
                "text": "Dear colleagues,",
                "imgUrl": None,
                "imgTitle": None,
                "style": "Normal"
            },
            "2": {
                "text":
                    "Many things have changed this year due to COVID-19, and so have our plans for the traditional local Christmas parties in Finland. This year we offer you something else. We invite you all to experience something fun together virtually, just before the year end.",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
            },
            "3": {
                "text":
                    "Welcome to a relaxed session with actor, stand-up comedian and television host Jaakko Saariluoma. He´s a quick thinker, sharp and fun – always a step ahead of everyone. Take your seats and get ready to be entertained!",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
            },
            "4": {
                "text":
                    "The session will be hosted by one of Finland’s leading business speakers and writers André Noël Chaker. As an entrepreneur, André has been a leading force in many science, technology, gaming and sports related start-up ventures.",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
            },
            "5": {
                "text":
                "Opening by André Noël Chaker",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
            },
            "6": {
                "text": "Nokia’s season’s greetings",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
            },
            "7": {
                "text":  "by Country Senior Officer Tommi Uitto and Site Heads Vesa Kohtamäki, Erja Sankari and Petri Ahokas",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
            },
            "8": {
                "text": "André’s take on Finns & Christmas by André Noël Chaker",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
            },
            "9": {
                "text": "Christmas music from Nokia sites in Finland by Nokia employees",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
            },
            "10": {
                "text":
                "Stand-up show by Jaakko Saariluoma",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
            },
            "11": {
                "text":
                    "Take a sneak peek on Jaakko’s greetings to our Nokia employees here.",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
            },
            "12": {
                "text":
                    "This is an internal event dedicated for Nokia employees in Finland. Join us for a fun and relaxed session!",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
            },
            "13": {
                "text": "Welcome!",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
            },
            "14": {
                "text":
                    "Tip! You may want to consider arranging your own virtual Christmas get-together with your team right after this show.",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
            },
            "15": {
                "text": "Br,",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
            },
            "16": {
                "text": "Finland Communications",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
            },
            "17": {
                "text": "How to join the session:",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
            },
            "18": {
                "text": "The session is a live stream. A recording of the session will be made available soon afterwards",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
            },
            "19": {
                "text": "The live stream will be available here.",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "List Paragraph"
            },
            "20": {
                "text": "Password for the session is: NokiaFinland",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "List Paragraph"
            },
            "21": {
                "text": "Please note that for optimal viewing, it is best not to use VPN. If the live stream doesn't load when the session starts, please refresh the page or try another browser.",
                    "imgUrl": None,
                    "imgTitle": None,
                    "style": "Normal"
            },
        },
        "links": {
            "20": {
                "link": "https://nokia.sharepoint.com/:v:/r/sites/espoo_HQ_campus/Espoo Campus Pictures/2020/Christmas session with Jaakko Saariluoma 10.12.2020/Jaakko Saariluoma's greetings to Nokia employees.mp4?csf=1&web=1&e=8pEZab",
                "link_keyword": "here" 
            },
            "21": {
                "link": "https://livekatsomo.fi/streams/nokia-saariluoma/",
                "link_keyword": "here"
            }
        }
    }

    def post(self):
        create = CreateArticle()
        create.setData(self.data)
        args = parser.parse_args()
        # print(args)
        data = create.create_newsitem()
        return data
