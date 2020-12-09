from flask import Flask, current_app
from flask_restful import Api, Resource, reqparse, request, abort
from werkzeug.datastructures import FileStorage
from ..utils.parse_news import Parse_News
from ..utils.create_article import CreateArticle

 # Request Parser, names of the paramateres alongside their types, help is sent in response when the required parameter is not found in the request
parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument("description", type=str,
                    help="description required", required=True)
parser.add_argument("displayName", type=str, help="author displayName required", required=True)
parser.add_argument("department", type=str, help="author department required", required=True)
parser.add_argument("jobtitle", type=str,
                    help="author jobtitle required", required=True)
parser.add_argument("email", type=str,
                    help="author email required", required=True)
parser.add_argument("document", type=FileStorage, location='files',
                    help="Need document to parse", required=True)

class News_Parser(Resource):
    # Dummy author
    author = {
        "displayName": "Blaa",
        "email": "Blaa",
        "department": "Blaa",
        "jobtitle": "Blaa"
    }

     # Add token check for security?
    def post(self):

        args = parser.parse_args()
        # Getting the right values from args
        self.author["displayName"] = args["displayName"]
        self.author["email"] = args["email"]
        self.author["department"] = args["department"]
        self.author["jobtitle"] = args["jobtitle"]
        description = args["description"]
        doc = args["document"]

        # Parsing the document
        newsParser = Parse_News()
        newsParser.setValues(self.author, description)
        document = newsParser.initialize_doc(doc)
        newsParser.parse_news(document)
        article = newsParser.createArticle()

        # Create article to db class
        create = CreateArticle()
        create.setData(article)
        out = create.create_newsitem()

        return out, 200
