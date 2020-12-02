from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def initialize_db(app):
    db.init_app(app)


def create_db():
    from .author import Author
    from .article import Article
    from .image import Image
    from .paragraph import Paragraph
    from .links import Link
    from .header import Header

    db.drop_all()
    db.create_all()
    db.session.commit()