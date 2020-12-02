from .db import db

class Link(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    paragraph_id = db.Column(db.Integer, db.ForeignKey('paragraph.id'))
    link = db.Column(db.String(200))
    link_keyword = db.Column(db.String(20))

    def __init__(self, text, style, link, link_keyword):
        self.text = filename
        self.style = style
        self.link = link
        self.link_keyword = link_keyword

    def __repr__(self):
        return '<Image %r>' % self.filename