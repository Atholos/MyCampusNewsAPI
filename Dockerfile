FROM python:3

WORKDIR /home/site/wwwroot

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# expose port 8000
EXPOSE 8000

# start flask app using Gunicorn
CMD gunicorn -w 4 -b :8000 app:APP