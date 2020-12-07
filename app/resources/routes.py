from app.resources.home import Home
from app.resources.highlight import Highlight
from app.resources.newsitem import NewsItem
from app.resources.newsitems import NewsItems
from app.resources.upload_article import UploadArticle


# Initializing the routes for flask API, When adding a new route add it here.
def initialize_routes(API):
    API.add_resource(Home, "/")
    API.add_resource(Highlight, "/highlight")
    #Route with parameters, Used when looking for a specific item, note that post requests include a body anyway
    API.add_resource(NewsItem, "/newsitem/<int:id>")
    API.add_resource(NewsItems, "/newsitems")
    API.add_resource(UploadArticle, "/upload-article")

   