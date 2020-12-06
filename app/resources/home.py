from flask import Flask
from flask_restful import Api, Resource, reqparse


class Home(Resource):
    # Add token check for security?
    @staticmethod
    def get():  
        out = {"Usage": "Please use endpoints for data, highlight can be accessed from /highlight, newstitems from /newsitems , you can also query for individual newsitems by using /newsitem/<itemid>"}
        return out, 200
        