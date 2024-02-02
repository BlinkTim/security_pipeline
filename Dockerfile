
FROM ubuntu:19.04

RUN apt-get update && \
    apt-get install -y ssh wget curl python3

WORKDIR /app

COPY . /app

RUN chmod -R 777 /app

CMD ["python3", "/app/run.py"]
