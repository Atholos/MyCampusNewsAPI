# app.py
import os
from flask import Flask, Blueprint, current_app
from flask_restful import Api
from azure.storage.blob import ContainerClient
from flask_cors import CORS


def create_app():

    # Creating flask application and setting the correct configurations
    app = Flask(__name__)
    app.config.from_object("config.default") # Getting the default config first to make sure we have one
    app.config.from_object(os.environ.get("APP_CONFIG")) # Overwriting the default config with one from the Environment variable 

    # Initializing database connection
    from app.model.db import initialize_db
    initialize_db(app)

    # Initializing flask-restful API and CORS
    api = Api(app)
    CORS(app)

    with app.app_context():
        # Include our Routes
        from app.resources.routes import initialize_routes
        initialize_routes(api)
        # Importing classes so they can use app context (current_app, g)
        from app.utils.create_article import CreateArticle
        from app.utils import build_article
        from app.model.db import db, create_db
        #Creating the db. dropping the current one if in development or staging
        create_db()
        
        return app
   