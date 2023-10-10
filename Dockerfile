FROM python:3.10.0b3-slim

ENV PYTHONBUFFERED 1

RUN pip install --upgrade pip

COPY . /src

WORKDIR /src

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x docker-entrypoint.sh
