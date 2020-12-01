import os

TESTING = False
DEBUG = False # Turns on debugging features in Flask
BCRYPT_LOG_ROUNDS = 12 # Configuration for the Flask-Bcrypt extension
ENV = "production"
SQLALCHEMY_DATABASE_URI = os.environ.get("PROD_DATABASE_URL") #Database url
CONTAINER_NAME = os.environ.get("NEWS_CONTAINER_NAME") # Azure Container name
IMAGE_CONTAINER_NAME = os.environ.get("IMAGE_CONTAINER_NAME") # Azure Container name
STORAGE_ACCOUNT = os.environ.get("STORAGE_ACCOUNT")  # Azure account name
STORAGE_KEY = os.environ.get("STORAGE_KEY")   # Azure Storage account access key 
CONNECTION_STRING = os.environ.get("CONNECTION_STRING")
