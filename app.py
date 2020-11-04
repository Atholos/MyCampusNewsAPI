# app.py
from flask import Flask
from flask_restful import Api, Resource, reqparse
import joblib
import numpy as np
from predict import Predict

APP = Flask(__name__)
API = Api(APP)

API.add_resource(Predict, '/predict')

if __name__ == '__main__':
    APP.run(debug=True, port='1080')