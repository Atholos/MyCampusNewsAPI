from flask import Flask
from flask_restful import Api, Resource, reqparse

## Route resource class used for returning specific news items
class NewsItem(Resource):

    # static methods cannot take data from outside the function
    @staticmethod
    def get(month, number):
        out = {"Item": "This is your news item",
                "for month": month, "number": number}
        return out, 200
