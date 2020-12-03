from .db import db

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    paragraph_id = db.Column(db.Integer, db.ForeignKey('paragraph.id'))
    link = db.Column(db.String(500))
    link_keyword = db.Column(db.String(100))

    def __init__(self, paraid, link, link_keyword):
        self.paragraph_id = paraid
        self.link = link
        self.link_keyword = link_keyword
    def __repr__(self):
        return '<Link %r>' % self.link