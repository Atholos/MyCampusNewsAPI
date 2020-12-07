FROM python:3

WORKDIR /home/site/wwwroot
## Installing required packages
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
## Copy all
COPY . .

ENV APP_CONFIG=../config/development.py
ENV FLASK_APP=app.py
ENV DEV_DATABASE_URI="postgresql://myuser:badpass@localhost/postgres"
ENV PROD_DATABASE_URI="postgresql://NMC_News_API%40nmcmycampusdb:G4n1bo!H30Z"$"@nmcmycampusdb.postgres.database.azure.com/NMC_Innovation_Database"
ENV STAGING_DATABASE_URI="postgresql://NMC_News_API%40nmcmycampusdb:G4n1bo!H30Z"$"@nmcmycampusdb.postgres.database.azure.com/NMC_Staging"
ENV NEWS_CONTAINER_NAME="newsfileblob"
ENV IMAGE_CONTAINER_NAME="newsimages"
ENV TEST_CONTAINER_NAME="testfileblob" 
ENV STORAGE_ACCOUNT="nmcinnovationstorage"  
ENV STORAGE_KEY="ypO3eQIw4ENp2KGn7piyVAC+Aaujgg/qa27sv7FWEm8IAtEcbd4vPNC4sxdRAZ1/UEuhlWot7cDKn7W6wR2aGQ==" 
ENV CONNECTION_STRING="DefaultEndpointsProtocol=https;AccountName=nmcinnovationstorage;AccountKey=ypO3eQIw4ENp2KGn7piyVAC+Aaujgg/qa27sv7FWEm8IAtEcbd4vPNC4sxdRAZ1/UEuhlWot7cDKn7W6wR2aGQ==;EndpointSuffix=core.windows.net"



## Enabling ssh
#RUN apk add openssh \
    # && echo "root:Docker!" | chpasswd
#COPY sshd_config /etc/ssh/


#expose port 8000
EXPOSE 8000

# start flask app using Gunicorn
CMD gunicorn -w 4 -b :8000 "app:create_app()"