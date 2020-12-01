import os

class Config(object):
    DEBUG = False # Turns on debugging features in Flask
    BCRYPT_LOG_ROUNDS = 12 # Configuration for the Flask-Bcrypt extension
    ENV = "Default"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URI") #Database url
    CONTAINER_NAME = os.environ.get("TEST_CONTAINER_NAME") # Azure Container name
    IMAGE_CONTAINER_NAME = os.environ.get("TEST_CONTAINER_NAME") # Azure Container name
    STORAGE_ACCOUNT = os.environ.get("STORAGE_ACCOUNT")  # Azure account name
    STORAGE_KEY = os.environ.get("STORAGE_KEY")   # Azure Storage account access key 
    CONNECTION_STRING = os.environ.get("CONNECTION_STRING")

class Development(Config):
    DEBUG = True # Turns on debugging features in Flask
    ENV = "Development"

class Production(Config):
    DEBUG = False
    TESTING = False
    ENV = "Production"
    CONTAINER_NAME = os.environ.get("PROD_CONTAINER_NAME") # Azure Container name
    IMAGE_CONTAINER_NAME = os.environ.get("IMAGE_CONTAINER_NAME") # Azure Container name
    SQLALCHEMY_DATABASE_URI = os.environ.get("PROD_DATABASE_URI") #Database url

class Staging(Config):
    DEBUG = False # Turns on debugging features in Flask
    TESTING = True
    BCRYPT_LOG_ROUNDS = 12 # Configuration for the Flask-Bcrypt extension
    ENV = "Staging"
    SQLALCHEMY_DATABASE_URI = os.environ.get("STAGING_DATABASE_URI") #Database url
    CONTAINER_NAME = os.environ.get("TEST_CONTAINER_NAME") # Azure Container name
    IMAGE_CONTAINER_NAME = os.environ.get("TEST_CONTAINER_NAME") # Azure Container name

class Test(Config):
    DEBUG = True # Turns on debugging features in Flask
    TESTING = True
    BCRYPT_LOG_ROUNDS = 12 # Configuration for the Flask-Bcrypt extension
    ENV = "Testing"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URI") #Database url
    CONTAINER_NAME = os.environ.get("TEST_CONTAINER_NAME") # Azure Container name
    IMAGE_CONTAINER_NAME = os.environ.get("TEST_CONTAINER_NAME") # Azure Container name
