FROM python:3.11

ENV PYTHONDONTWRITEBYCOD 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/requairements.txt

RUN pip install -r /app/requairements.txt

ADD . .