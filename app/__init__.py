# app.py
import os
from flask import Flask, Blueprint
from flask_restful import Api
from azure.storage.blob import ContainerClient


def create_app(config='default'):

    app = Flask(__name__)
    app.config.from_object(config)
    #app.config.from_pyfile("config.py")

    from app.model.db import initialize_db
    initialize_db(app)

    api = Api(app)

    
    #with app.app_context():
        #Upload_utils(app)
    

    from app.resources.routes import initialize_routes
  

    #app.register_blueprint(api_bp)
    with app.app_context():
        # Include our Routes
        from app.resources.routes import initialize_routes
        initialize_routes(api)
        #from app.utils.upload_utils import Upload_utils
        #Upload_utils()
        '''
        # Register Blueprints
        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(admin.admin_bp)
        '''
        return app