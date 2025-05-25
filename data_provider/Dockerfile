FROM python:3.8-slim-buster

WORKDIR /kafka_producer

ADD . /kafka_producer

RUN set -ex; \
  	pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
