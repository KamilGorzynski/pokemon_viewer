FROM python:3.10.0b3-slim

ENV PYTHONBUFFERED 1

RUN pip install --upgrade pip

WORKDIR /usr/src

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install flower

COPY . .

CMD gunicorn pokemon_viewer_backend.wsgi -k gevent -w 4 --worker-connections 1000 --bind 0.0.0.0:80