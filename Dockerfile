FROM python:2.7-slim

MAINTAINER Eduardo Zimermam Pereira "eduardozimerman@live.com"

WORKDIR /app
COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000


CMD ["python", "application.py"]