from .db_create import DBCreate
from .db_query import DBQuery
from flask import current_app


class CreateArticle():

    dbc = DBCreate()
    dbq = DBQuery()

    def setData(self,data):
        self.data = data

    def create_newsitem(self):

        # creating author, article, image, header, paragraph, links, database objects

        author  = self.dbc.create_author(self.data["author"]["displayName"], self.data["author"]["email"], self.data["author"]["department"], self.data["author"]["jobtitle"])
        article = self.dbc.create_article(self.data["title"], self.data["description"], self.data["highlight"], author.id)
        # filename, url, container, articleid, imgtitle
        headerimage = self.dbc.create_image(self.data["headerImgUrl"], None , current_app.config["IMAGE_CONTAINER_NAME"], self.data["headerImgTitle"])
        header = self.dbc.create_header(article.id, headerimage.id)
        paragraphs = self.parse_paragraphs(article.id)
       
        print(author.id, article.id)
      
        return {"author": author.id, "article": article.id, "headerimage": headerimage.id, "header": header.id, "paragraphs": paragraphs}  

     # for parsing the paragraphs from dictionary
    def parse_paragraphs(self, articleid):
        # Empty dict of paragraphs to return for testing purposes
        paragraphs = {}

        for paragraph in self.data["paragraphs"]:
            # Key is the order number 
            order_nr = paragraph
            text =  self.data["paragraphs"][paragraph]["text"]
            imgUrl = self.data["paragraphs"][paragraph]["imgUrl"]
            imgTitle =  self.data["paragraphs"][paragraph]["imgTitle"]
            style = self.data["paragraphs"][paragraph]["style"]
            #If paragraphs has images we create them first.
            image = None
            paraid = None
            if imgUrl != None or "":
                image = self.dbc.create_image(imgUrl, None, current_app.config["IMAGE_CONTAINER_NAME"], articleid, imgTitle)
                # self, text, style, articleid, imageid, ordernr
                dbpara = self.dbc.create_paragraph(text, style, articleid, image.id, order_nr)
                paraid = dbpara.id
                # Adding database objects id to testing dictionary
                paragraphs[paragraph] = paraid
            else:
                #If paragraph has no image then go here
                dbpara = self.dbc.create_paragraph(text, style, articleid, image, order_nr)
                paraid = dbpara.id
                 # Adding database objects id to testing dictionary
                paragraphs[paragraph] = paraid

            # Checking if paragraph has any links attached to it
            for link in self.data["links"]:
                if link == order_nr:
                    # paragraph_id, link, link_keyword
                    link_url = self.data["links"][link]["link"]
                    link_key =  self.data["links"][link]["link_keyword"]
                    dblink = self.dbc.create_link(paraid, link_url , link_key)

        return paragraphs
        

       
