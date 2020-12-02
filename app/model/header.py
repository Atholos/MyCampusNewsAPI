from .db import db


class Header(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'))

    def __init__(self, articleid, imageid):
       self.article_id = articleid
       self.image_id = imageid
    def __repr__(self):
        return '<Image %r>' % self.filename
