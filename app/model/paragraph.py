from .db import db

class Paragraph(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(2000), unique=False)
    style = db.Column(db.String(120), unique=False)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    img_id = db.Column(db.Integer, db.ForeignKey('image.id'))
    order_nr = db.Column(db.Integer)

    def __init__(self, text, style, articleid, imageid, ordernr):
        self.text = text
        self.style = style
        self.article_id = articleid
        self.img_id = imageid
        self.order_nr = ordernr
    def __repr__(self):
        return '<Paragraph %r>' % self.text