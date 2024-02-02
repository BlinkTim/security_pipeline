FROM ubuntu:19.04

RUN apt-get upgrade
RUN install ssh \
    wget \
    curl \
    python3 \

COPY . /app

RUN chmod -R 777 /app

CMD ["python3", "/app/run.py"]
