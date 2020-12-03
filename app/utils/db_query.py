from ..model.db import db
from ..model.author import Author
from ..model.article import Article
from ..model.image import Image
from ..model.paragraph import Paragraph
from ..model.links import Link
from ..model.header import Header

class DBQuery():

    def query_authorName(self, displayname):
        author = Author.query.filter_by(displayName=(displayname)).first()
        print("queried for author by displayname")
        return author
    
    def query_authorID(self, aid):
        author = Author.query.filter_by(id=(aid)).first()
        print("queried for author by id")
        return author