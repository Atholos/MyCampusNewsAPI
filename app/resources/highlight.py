from flask import Flask, current_app
from flask_restful import Resource
from ..utils.build_article import BuildArticle
from ..utils.db_query import DBQuery


class Highlight(Resource):
    session = DBQuery()
    builder = BuildArticle()
    
    def get(self):
        article = self.session.query_highlight_article()
        print(article)
        self.builder.setArticle(article)
        print(self.builder.article)
        out = self.builder.build()
        return out, 200
