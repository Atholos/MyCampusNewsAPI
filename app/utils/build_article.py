from .db_query import DBQuery
from flask import current_app
from azure.storage.blob import ContainerClient, generate_blob_sas, BlobSasPermissions
from datetime import datetime, timedelta


# Used for building the article via queries and returning it in json format
class BuildArticle():

    dbq = DBQuery()
    account_name = current_app.config["STORAGE_ACCOUNT"]
    account_key = current_app.config["STORAGE_KEY"]

    def setArticle(self, article):
        self.article = article

    def build(self):
        self.author = self.dbq.query_authorID(self.article.author)
        self.header = self.dbq.query_headerByArticleID(self.article.id)
        self.headerImage = self.dbq.query_imageID(self.header.image_id)
        self.headerurl = self.get_img_url_with_blob_sas_token(self.headerImage)
        #self.paragraphs = self.dbq.query_paragraphs()

        print("Building")
        return self.build_json()

    def build_json(self):

        json = {
            "title": "Welcome to Nokia Finland Christmas Session on December 10",
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
            "paragraphs": {
                
            },
            "links": {

            }
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
