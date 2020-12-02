from .db import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False)
    description = db.Column(db.String(200), unique=False)
    highlight = db.Column(db.Boolean, unique=False)
    author = db.Column(db.Integer, db.ForeignKey('author.id'))
    headerImg = db.Columm(db.Integer, db.ForeignKey('image.id'))
    
    def __init__(self, title, description, highlight, author):
        self.title = title
        self.description = description 
        self.highlight = highlight
        self.author = author
    def __repr__(self):
        return '<Article %r>' % self.title
