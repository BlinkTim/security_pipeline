FROM ubuntu:19.04

RUN apt-get upgrade
RUN install ssh \
    wget \
    curl \
    python

COPY . /app

RUN chmod -R 777 /app

CMD ["python", "/app/run.py"]
