# app.py
import os
from flask import Flask, Blueprint, current_app
from flask_restful import Api
from azure.storage.blob import ContainerClient
from flask_cors import CORS


def create_app():

    # Creating flask application and setting the correct configurations
    app = Flask(__name__)
    app.config.from_object("config.default")
    #app.config.from_pyfile(myconfig)
    app.config.from_envvar("APP_CONFIG")

    # Initializing database connection
    from app.model.db import initialize_db
    initialize_db(app)

    # Initializing flask-restful API
    api = Api(app)
    CORS(app)


    #app.register_blueprint(api_bp)
    with app.app_context():
        # Include our Routes
        from app.resources.routes import initialize_routes
        initialize_routes(api)
        #print(current_app.config)
        from app.utils.create_article import CreateArticle
        from app.utils import build_article
        from app.model.db import db, create_db
        create_db()
        '''
        Register Blueprints example 
        app.register_blueprint(auth.auth_bp)
        '''
        return app
   