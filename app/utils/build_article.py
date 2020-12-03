from .db_query import DBQuery
from flask import current_app
from azure.storage.blob import ContainerClient, generate_blob_sas, BlobSasPermissions


# Used for building the article via queries and returning it in json format
class BuildArticle():

    dbq = DBQuery()
    account_name = current_app.config["STORAGE_ACCOUNT"]
    account_key = current_app.config["STORAGE_KEY"]

    def setArticle(self, article):
        self.article = article

    def build(self):
        self.author = dbq.query_authorID(article.author)
        self.header = dbq.query_headerByArticleID(article.id)
        self.headerImage = dbq.query_imageID(header.image_id)
        self.headerurl = self.image_container_link(headerImage)

        print("Building")

    def build_json(self):

        json = {
            "title": "Welcome to Nokia Finland Christmas Session on December 10",
            "author": {
                "id": self.author.id,
                "displayName": self.author.displayName,
                "email": self.author.email,
                "department": self.author.department,
                "jobtitle": self.author.job
            },
            "highlight": self.article.highlight,
            "description": self.article.description,
            "created_at": self.article.created_at,
            "headerImgUrl": "",
            "headerImgTitle": "",
            "paragraphs": {

            },
            "links": {

            }
        }

        print("building the json")
        return json

    def image_container_link(self, image):
        print("creating a temporary link for image")
        return self.get_img_url_with_blob_sas_token(image)

    def get_img_url_with_blob_sas_token(image):
        blob_sas_token = generate_blob_sas(
            account_name=account_name,
            container_name=image.container,
            blob_name=image.filename,
            account_key=account_key,
            permission=BlobSasPermissions(read=True),
            expiry=datetime.utcnow() + timedelta(hours=1)
        )
        blob_url_with_blob_sas_token = f"https://{account_name}.blob.core.windows.net/{container_name}/{blob_name}?{blob_sas_token}"
        return blob_url_with_blob_sas_token
