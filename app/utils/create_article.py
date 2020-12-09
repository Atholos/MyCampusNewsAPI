from .db_create import DBCreate
from .db_query import DBQuery
from flask import current_app


class CreateArticle():
    dbc = DBCreate()
    dbq = DBQuery()

    # Setting the data. Doing this here instead of init enables us to use same class object for multiple article instances. 
    def setData(self,data):
        self.data = data

    def create_newsitem(self):

        # creating author, article, image, header, paragraph, links, database objects

        # Checking if author exists
        author = self.dbq.query_authorName(self.data["author"]["displayName"])
        # If not then we create one->
        if(author == None):
            author = self.dbc.create_author(self.data["author"]["displayName"], self.data["author"]["email"], self.data["author"]["department"], self.data["author"]["jobtitle"])

        article = self.dbc.create_article(self.data["title"], self.data["description"], self.data["highlight"], author.id)

        # filename, url, container, articleid, imgtitle
        headerimage = self.dbq.query_image_filename(self.data["headerImgUrl"]["filename"])
        if(headerimage == None):
            headerimage = self.dbc.create_image(self.data["headerImgUrl"]["filename"], None , current_app.config["IMAGE_CONTAINER_NAME"], self.data["headerImgTitle"], self.data["headerImgUrl"]["heigth"], self.data["headerImgUrl"]["width"])

        # Creating header table to connect article and image
        header = self.dbc.create_header(article.id, headerimage.id)
        # Creating the paragraphs
        paragraphs = self.parse_paragraphs(article.id)

        print(author.id, article.id)
        return self.data  

     # for parsing the paragraphs from dictionary
    def parse_paragraphs(self, articleid):
        # Empty dict of paragraphs to return for testing purposes
        paragraphs = {}

        for paragraph in self.data["paragraphs"]:
            # Key is the order number 
            order_nr = paragraph
            text =  self.data["paragraphs"][paragraph]["text"]
            imgUrl = self.data["paragraphs"][paragraph]["image"]
           
            style = self.data["paragraphs"][paragraph]["style"]
            #If paragraphs has images we create them first.
            image = None
            paraid = None
            if imgUrl != None or "":
                imgTitle =  self.data["paragraphs"][paragraph]["image"]["imgTitle"] 
                # Checking if image exists already and creating a new image if necessary               
                image = self.dbq.query_image_filename(imgUrl)
                if(image == None):
                    image = self.dbc.create_image(imgUrl["filename"], None, current_app.config["IMAGE_CONTAINER_NAME"], imgTitle, imgUrl["heigth"], imgUrl["width"])
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
            if(self.data["paragraphs"][paragraph]["links"]):
                for link in self.data["paragraphs"][paragraph]["links"]:  
                    # paragraph_id, link, link_keyword
                    link_url = self.data["paragraphs"][paragraph]["links"][link]["link"]
                    link_key =  self.data["paragraphs"][paragraph]["links"][link]["link_keyword"]
                    dblink = self.dbc.create_link(paraid, link_url , link_key)

        return paragraphs
        

       
