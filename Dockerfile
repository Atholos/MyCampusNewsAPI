FROM python:3

WORKDIR D:\myCampus\MyCampusNewsAPI

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./app.py" ]