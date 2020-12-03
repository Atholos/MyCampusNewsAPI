from ..model.db import db
from ..model.author import Author
from ..model.article import Article
from ..model.image import Image
from ..model.paragraph import Paragraph
from ..model.links import Link
from ..model.header import Header

class DBQuery():

    # Author queries
    def query_authorName(self, displayname):
        author = Author.query.filter_by(displayName=(displayname)).first()
        print("queried for author by displayname")
        return author
    
    def query_authorID(self, author_id):
        author = Author.query.get(author_id)
        print("queried for author by id")
        return author

    # Article queries
    def query_articleID(self, article_id):
        article = Article.query.get(article_id)
        print("queried for article by id")
        return article

    # 10 newest articles
    def query_articleID(self):
        articles = Article.query.order_by(Article.created_at).limit(10).all()
        print("queried for article by id")
        return articles 

    # Image queries
    def query_imageID(self, image_id):
        image = Image.query.get(image_id)
        return image

    # Paragraph queries
    def query_paragraphID(self, paragraph_id):
        paragraph = Paragraph.query.get(paragraph_id)
        return paragraph

    def query_paragraphByArticleID(self, article_id):
        paragraph = Paragraph.query.filter_by(article_id=(article_id)).first()
        return paragraph

    # Get all paragraphs for an article
    def query_paragraph_for_article(self, article_id):
        paragraphs = Paragraph.query.filter_by(article_id=(article_id)).all()
        return paragraphs

     # Header queries
    def query_headerID(self, header_id):
        header = Header.query.get(header_id)
        return header
    
    def query_headerByArticleID(self, article_id):
        header = Header.query.filter_by(article_id=(article_id)).first()
        return header
    
    # Links queries
    def query_linksID(self, link_id):
        link = Link.query.get(link_id)
        return link
    
    def query_linksByParagraphID(self, paragraph_id):
        link = Link.query.filter_by(paragraph_id=(paragraph_id)).first()
        return link
    


