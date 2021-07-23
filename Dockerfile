FROM coding-public-docker.pkg.coding.net/public/docker/python:3.8

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt





