from .db import db


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(80), unique=True)
    url = db.Column(db.String(120), unique=True)
    container = db.Column(db.String(120), unique=False)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    title = db.Column(db.String(200), unique=False)

    def __init__(self, filename, url, container, articleid, title):
        self.filename = filename
        self.url = url
        self.container = container
        self.articleid = articleid
        self.title = title 
    def __repr__(self):
        return '<Image %r>' % self.filename
