FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip --no-cache-dir install --upgrade pip

COPY ./requirements.txt /app

RUN pip --no-cache-dir install -r requirements.txt

COPY . /app

ENTRYPOINT main.py