from .db_query import DBQuery
from flask import current_app
from azure.storage.blob import ContainerClient, generate_blob_sas, BlobSasPermissions
from datetime import datetime, timedelta


# Used for building the article via queries and returning it in json format
class BuildArticle():

    ## Getting queries and keys from config file for sas creation
    dbq = DBQuery()
    account_name = current_app.config["STORAGE_ACCOUNT"]
    account_key = current_app.config["STORAGE_KEY"]
    
    # Setting the article for builder, this could probably just be inside __init__ instead
    def setArticle(self, article):
        self.article = article

    # Main builder function
    def build(self):
        self.author = self.dbq.query_authorID(self.article.author)
        self.header = self.dbq.query_headerByArticleID(self.article.id)
        self.headerImage = self.dbq.query_imageID(self.header.image_id)
        self.headerurl = self.get_img_url_with_blob_sas_token(self.headerImage)
        self.paragraphs = self.dbq.query_paragraphs_for_article(self.article.id)
        self.dictparagraphs = self.parse_paragraphs(self.paragraphs)
        return self.build_json()

    # Json builder function (actually a dictionary but turns into json via restful return)
    def build_json(self):

        json = {
            "id": self.article.id,
            "title": self.article.title,
            "author": {
                "id": self.author.id,
                "displayName": self.author.displayName,
                "email": self.author.email,
                "department": self.author.department,
                "jobtitle": self.author.jobtitle
            },
            "highlight": self.article.highlight,
            "description": self.article.description,
            "created_at": self.article.created_at.strftime("%d-%b-%Y (%H:%M:%S.%f)"),
            "headerImgUrl": self.headerurl,
            "headerImgTitle": self.headerImage.title,
            "paragraphs": self.dictparagraphs,
        }

        return json


    # Creating a temporary sas token for image access
    def get_img_url_with_blob_sas_token(self, image):
        blob_sas_token = generate_blob_sas(
            account_name=self.account_name,
            container_name=image.container,
            blob_name=image.filename,
            account_key=self.account_key,
            permission=BlobSasPermissions(read=True),
            expiry=datetime.utcnow() + timedelta(hours=1)
        )
        blob_url_with_blob_sas_token = f"https://{self.account_name}.blob.core.windows.net/{image.container}/{image.filename}?{blob_sas_token}"
        return blob_url_with_blob_sas_token

    # Used for generating the paragraph dictionaries
    def parse_paragraphs(self, paragraphs):
        parsed_paragraphs = {}   
        for paragraph in paragraphs:
            parsed_links = {}

            # Realised afterwards that having article id in links would optimize the database usage and reduce the number of queries. 
            links = self.dbq.query_linksByParagraphID(paragraph.id)
            # iterating through links if there are any and creating a dictionary containing the links for selected paragraph
            for link in links:
                parsed_links[link.id] = {
                    "link": link.link,
                    "link_keyword": link.link_keyword
                }
            if parsed_links == {}:
                # changing {} into None or null for readability purposes. Also makes frontend null check easier.
                parsed_links = None

            # Get images if paragraph has one
            image = self.dbq.query_imageID(paragraph.img_id)

            # Initialized variables
            imgUrl = None
            imgTitle = None
            imgHeigth = None
            imgWidth = None 

            if image != None:
                imgUrl = self.get_img_url_with_blob_sas_token(image)
                imgTitle = image.title

            # creating the paragraphs dictionary with paragraph order_nr as key, 
            parsed_paragraphs[paragraph.order_nr] = {
                "id": paragraph.id,
                "text": paragraph.text,
                "style": paragraph.style,
                "imgUrl": imgUrl,
                "imgTitle": imgTitle,
                "imgHeigth": imgHeigth,
                "imgWidth": imgWidth,
                "link_ids": parsed_links
            }
            
        return parsed_paragraphs


    
    
