FROM python:3

WORKDIR /home/site/wwwroot
## Installing required packages
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
## Copy all
COPY . .

## Enabling ssh
#RUN apk add openssh \
    # && echo "root:Docker!" | chpasswd
#COPY sshd_config /etc/ssh/


#expose port 8000
EXPOSE 8000

# start flask app using Gunicorn
CMD gunicorn -w 4 -b :8000 "app:create_app()"