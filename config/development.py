DEBUG = True # Turns on debugging features in Flask
BCRYPT_LOG_ROUNDS = 12 # Configuration for the Flask-Bcrypt extension
SQLALCHEMY_DATABASE_URI = "postgresql://myuser:badpass@localhost/postgres" #Database url
CONTAINER_NAME = "testfileblob" # Azure Container name
STORAGE_ACCOUNT = "nmcinnovationstorage"  # Azure account name
STORAGE_KEY = "ypO3eQIw4ENp2KGn7piyVAC+Aaujgg/qa27sv7FWEm8IAtEcbd4vPNC4sxdRAZ1/UEuhlWot7cDKn7W6wR2aGQ=="   # Azure Storage account access key 
STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=nmcinnovationstorage;AccountKey=ypO3eQIw4ENp2KGn7piyVAC+Aaujgg/qa27sv7FWEm8IAtEcbd4vPNC4sxdRAZ1/UEuhlWot7cDKn7W6wR2aGQ==;EndpointSuffix=core.windows.net"
