from .db import db


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(80), unique=True)
    url = db.Column(db.String(120), unique=True)
    container = db.Column(db.String(120), unique=False)
    articleid = db.Column(db.Integer, unique=False)
    description = b.Column(db.String(200), unique=False)

    def __init__(self, filename, url, container, articleid, description):
        self.filename = filename
        self.url = url
        self.container = container
        self.articleid = articleid
        self.description = description 
    def __repr__(self):
        return '<Image %r>' % self.filename
