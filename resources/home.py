from flask import Flask
from flask_restful import Api, Resource, reqparse


class Home(Resource):

    @staticmethod
    def get():

        out = {"Home": "Home"}
        return out, 200