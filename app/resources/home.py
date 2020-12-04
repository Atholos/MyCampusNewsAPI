from flask import Flask
from flask_restful import Api, Resource, reqparse


class Home(Resource):

    @staticmethod
    def get():
        
        out = {"Usage": "Please use endpoints for data, highlight can be accessed from /highlight, newstitems from /newsitems"}
        return out, 200
        