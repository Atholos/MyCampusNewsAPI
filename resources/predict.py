from flask import Flask
from flask_restful import Api, Resource, reqparse


class Predict(Resource):

    @staticmethod
    def post():
        '''
        parser = reqparse.RequestParser()
        parser.add_argument('petal_length')
        parser.add_argument('petal_width')
        parser.add_argument('sepal_length')
        parser.add_argument('sepal_width')

        args = parser.parse_args()  # creates dict

        X_new = np.fromiter(args.values(), dtype=float)  # convert input to array
        '''
        out = {"Prediction": "iris-setosa"} 
        
        ##{'Prediction': IRIS_MODEL.predict([X_new])[0]}

        return out, 200
        