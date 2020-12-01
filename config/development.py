import os

DEBUG = True # Turns on debugging features in Flask
BCRYPT_LOG_ROUNDS = 12 # Configuration for the Flask-Bcrypt extension
ENV = "development"
SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URI") #Database url
CONTAINER_NAME = os.environ.get("TEST_CONTAINER_NAME") # Azure Container name
IMAGE_CONTAINER_NAME = os.environ.get("TEST_CONTAINER_NAME") # Azure Container name
STORAGE_ACCOUNT = os.environ.get("STORAGE_ACCOUNT")  # Azure account name
STORAGE_KEY = os.environ.get("STORAGE_KEY")   # Azure Storage account access key 
CONNECTION_STRING = os.environ.get("CONNECTION_STRING")
