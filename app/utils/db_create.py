from ..model.db import db
from ..model.author import Author
from ..model.article import Article
from ..model.image import Image
from ..model.paragraph import Paragraph
from ..model.links import Link
from ..model.header import Header

# class for creating database objects / rows
class DBCreate(): 
    # Author
    def create_author(self, displayName, email, department, jobtitle):
        author = Author(displayName, email, department , jobtitle)
        print("Creating an author")
        db.session.add(author)
        db.session.commit()
        return author
    # Article has relation with author
    def create_article(self, title, description, highlight, authorid):
        article = Article(title, description, highlight, authorid)
        print("Creating the article")
        db.session.add(article)
        db.session.commit()
        return article
    # Image, contains information on image filename and container instead of normal url (Required for azure blob) 
    def create_image(self, filename, url, container, imgtitle, heigth, width):
        image = Image(filename, url , container , imgtitle, heigth, width)
        db.session.add(image)
        db.session.commit()
        return image
    # Paragraph has relations with articles and images
    def create_paragraph(self, text, style, articleid, imageid, ordernr):
        paragraph = Paragraph(text, style, articleid, imageid, ordernr)
        db.session.add(paragraph)
        db.session.commit()
        return paragraph
    # Link has relation with paragraphs
    def create_link(self, paragraphid, link, link_keyword):
        link = Link(paragraphid, link,link_keyword)
        db.session.add(link)
        db.session.commit()
        return link
    # Header is a mid table for connecting articles and images as headers 
    def create_header(self, articleid, imageid):
        header = Header(articleid,imageid)
        db.session.add(header)
        db.session.commit()
        return header
    
    
    
