# pull official base image
FROM python:alpine

# set work directory
WORKDIR /WWW

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY Pipfile /WWW/Pipfile
RUN pipenv install --skip-lock --system

# copy entrypoint.sh
COPY entrypoint.sh /entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
