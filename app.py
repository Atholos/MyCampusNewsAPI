# app.py
from flask import Flask, Blueprint
from flask_restful import Api
from resources.routes import initialize_routes

APP = Flask(__name__)
api_bp = Blueprint('api', __name__)
API = Api(APP)

initialize_routes(API)
APP.register_blueprint(api_bp)

if __name__ == '__main__':
    APP.run(debug=True, port=5000)