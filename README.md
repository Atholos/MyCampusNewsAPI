# MyCampusNewsAPI
News fetching API for Nokia My Campus Project

This Rest API was built with Flask (Python) and is deployed inside a docker container to azure.

# Running the API in dev environment:

Install pip and required packages, please note that on windows python is ran with "py" instead of "python" 

python -m pip install --upgrade pip

pip install -r requirements.txt

Run the app in dev mode:

python -m flask run

Run with Gunicorn (Note that gunicorn only runs in unix environment like docker containers):

gunicorn -w 4 -b :8000 "app:create_app()"

# Building and running inside a container 

Installing docker:
https://docs.docker.com/docker-for-windows/install/

Building docker container image:

docker build .

Running docker container:

docker run --name "yourcontainername" "containerid"
  
See all images:

docker images -a
  
Note that you can add tags to your image with -t "tag" after the . , while running you can name your container with --name and it can be whatever you want. you get your container id after building an container from the image
  
checking for active containers:

docker ps

stopping a container:

docker stop <container>


# Environment

You need .env file to run the app with following contents:

ENV APP_CONFIG="config.development" # config.default loads the default configuration. config.development loads the dev config

ENV FLASK_APP=app.py # This enables flask to find your app.

ENV DEV_DATABASE_URI="yourDEVdatabaseURI" # Your dev database
  
ENV PROD_DATABASE_URI="yourPRODdatabaseURI" # Your Production database
  
ENV STAGING_DATABASE_URI="yourStagingDatabaseURI" # Your staging database
  
ENV NEWS_CONTAINER_NAME="newsfileblob" # Your azure container name used for storing data
  
ENV IMAGE_CONTAINER_NAME="newsimages" # Your azure container name used for storing images
  
ENV TEST_CONTAINER_NAME="testfileblob" # Your azure container used for testing
  
ENV STORAGE_ACCOUNT="storageAccount" # Your storage account 
  
ENV STORAGE_KEY="KeyToYourStorageAccount" # Key to your storage account
  
ENV CONNECTION_STRING="yourconnectionstring" # Storage account connection string


# API endpoints:

Get | For getting todays highlight news article

/highlight

Get | For getting 10 freshest news articles

/newsitems

Get | For getting a news article by ID (This was mostly used for testing but could be utilized later on)

/newsitems/<itemID>
  
POST | For parsing documents as new articles and adding them to database

/news-parser

Following query params are required:

str description: (Short description of the article)

str email: (Author email)

str displayName: (Author displayName)

str department: (Author department)

str jobtitle: (Author jobtitle)

file document: (The docx file you wish to upload)
  
  
API also requires a header to be sent with: "authorization": "Token"


