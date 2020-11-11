from resources.predict import Predict
from resources.home import Home


def initialize_routes(API):
    API.add_resource(Predict, '/predict')
    API.add_resource(Home, '/home')