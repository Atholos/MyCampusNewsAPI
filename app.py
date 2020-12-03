# app.py
from app import create_app
#from flask.cli import FlaskGroup
from app.model.db import db
from app.model.article import Article
from app.model.author import Author
from app.model.image import Image
from app.model.links import Link
from app.model.paragraph import Paragraph

app = create_app()
#cli = FlaskGroup(app)

'''
@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
'''
#if __name__ == "__main__":
    #app.run()