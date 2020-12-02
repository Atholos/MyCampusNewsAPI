from ..model.db import db
from ..model.author import Author
from ..model.article import Article
from ..model.image import Image
from ..model.paragraph import Paragraph
from ..model.links import Link
from ..model.header import Header


class DBCreate(): 

    def create_author(self, displayName, email, department, jobtitle):
        author = Author(displayName, email, department , jobtitle)
        print("Creating an author")
        db.session.add(author)
        db.session.commit()
        return author

    def create_article(self, title, description, highlight, authorid):
        self.article = Article(title, description, highlight, authorid)
        print("Creating the article")
        db.session.add(article)
        db.session.commit()
        return self.article.id
    
    def create_image(self, filename, url, container, articleid, imgtitle):
        image = Image(filename, url , container , articleid, imgtitle)
        db.session.add(image)
        db.session.commit()
        return image

    def create_paragraph(self, text, style, articleid, imageid, ordernr):
        paragraph = Paragraph(text, style, articleid, imageid, ordernr)
        db.session.add(paragraph)
        db.session.commit()
        return paragraph

    def create_link(self,text , style, link, link_keyword):
        link = Link(text,style,link,link_keyword)
        db.session.add(link)
        db.session.commit()
        return link

    def create_header(self, articleid, imageid):
        header = Header(articleid,imageid)
        db.session.add(header)
        db.session.commit()
        return header
    
    
    
