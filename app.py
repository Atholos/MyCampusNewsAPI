# app.py
from app import create_app
from flask.cli import FlaskGroup
from app.model import db, author, article, image, links, paragraph


app = create_app()
cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

create_db()
#if __name__ == "__main__":
    #app.run()