from flask import Flask
from flask_restful import Api, Resource, reqparse


class NewsItem(Resource):
    
    @staticmethod
    def get(month, number):
        out = {"Item": "This is your news item",
                "for month": month, "number": number}
        return out, 200
