# pull official base image
FROM python:3.6.8-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1 # Prevents Python from writing pyc files to disc
ENV PYTHONUNBUFFERED 1 # Prevents Python from buffering stdout and stderr

# install psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

# copy project
COPY . /usr/src/app/

# install dependencies
RUN pip install -r requirements.txt --upgrade pip

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
