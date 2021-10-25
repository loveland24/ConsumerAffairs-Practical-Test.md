FROM python:3.8

# set environment varibles
ENV PYTHONUNBUFFERED 1

# set work directory
RUN mkdir /code
RUN mkdir -p /var/logs/celery
RUN mkdir -p /var/logs/django
RUN mkdir -p /var/run/celery

WORKDIR /code

# install dependencies
COPY ./requirements.txt /code/
RUN pip install -r requirements.txt

# copy project
COPY ./theeye /code/

RUN apt-get update && apt-get install -y dos2unix
RUN dos2unix ./start_files/django-local.sh
RUN apt-get --purge remove -y dos2unix && rm -rf /var/lib/apt/lists/*

RUN chmod 777 -R ./start_files