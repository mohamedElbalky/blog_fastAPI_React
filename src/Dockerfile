FROM python:3.12.3-slim-bullseye

WORKDIR /app

COPY . .

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get upgrade -y && apt-get -y install gcc libpq-dev

RUN pip install -r requirements.txt

