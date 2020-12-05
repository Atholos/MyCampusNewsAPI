from flask import Flask
from flask_restful import Api, Resource, reqparse
from ..utils.build_article import BuildArticle
from ..utils.db_query import DBQuery
## Route resource class used for returning specific news items
class NewsItems(Resource):
    session = DBQuery()
    builder = BuildArticle()

    def get(self):
        print(id)
        data = {}
        articles = self.session.query_10_articles()
        print(articles)
        for article in articles:
            print(article)
            self.builder.setArticle(article)
            data[article.id] = self.builder.build()
        out = self.builder.build()
        return out, 200
