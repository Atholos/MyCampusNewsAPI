from .db import db


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200), unique=True)
    url = db.Column(db.String(300), unique=True)
    container = db.Column(db.String(200), unique=False)
    title = db.Column(db.String(200), unique=False)
    heigth = db.Column(db.Integer)
    width =  db.Column(db.Integer)

    def __init__(self, filename, url, container, title, heigth, width):
        self.filename = filename
        self.url = url
        self.container = container
        self.title = title
        self.heigth = heigth
        self.width = width
    def __repr__(self):
        return '<Image %r>' % self.filename
