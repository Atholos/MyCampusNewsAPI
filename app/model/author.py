from .db import db


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    displayName = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    department = db.Column(db.String(120), unique=False)
    jobtitle = db.Column(db.String(200), unique=False)

    def __init__(self, displayName, email, department, jobtitle):
        self.displayName = displayName
        self.email = email
        self.department = department
        self.jobtitle = jobtitle 
    def __repr__(self):
        return '<Author %r>' % self.displayName
