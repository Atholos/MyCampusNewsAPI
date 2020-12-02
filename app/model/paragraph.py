from .db import db

class Paragraph(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), unique=False)
    style = db.Column(db.String(120), unique=False)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    img_id = db.Column(db.String(200), db.ForeignKey('image.id'))

    def __init__(self, text, style, articleid, imageid):
        self.text = filename
        self.style = style
        self.article_id = articleid
        self.img_id = imageid
    def __repr__(self):
        return '<Image %r>' % self.filename