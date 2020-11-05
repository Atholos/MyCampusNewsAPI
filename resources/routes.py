from resources.predict import Predict


def initialize_routes(API):
    API.add_resource(Predict, '/predict')