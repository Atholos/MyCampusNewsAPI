from resources.predict import Predict
from resources.home import Home
from resources.highlight import Highlight
from resources.newsitem import NewsItem


def initialize_routes(API):
    API.add_resource(Home, "/")
    API.add_resource(Predict, "/predict")
    API.add_resource(Highlight, "/highlight")
    API.add_resource(NewsItem, "/newsitem/<string:month>/<int:number>")
   