from flask import Flask
from flask_restful import Api, Resource, reqparse
from ..utils.build_article import BuildArticle
from ..utils.db_query import DBQuery
## Route resource class used for returning specific news items
class NewsItem(Resource):
    session = DBQuery()
    builder = BuildArticle()

    def get(self, id):
        print(id)
        article = self.session.query_articleID(id)
        print(article)
        self.builder.setArticle(article)
        print(self.builder.article)
        out = self.builder.build()
        return out, 200
