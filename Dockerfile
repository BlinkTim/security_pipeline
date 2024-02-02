
FROM ubuntu:19.04

RUN apt-get update && \
    apt-get install ssh wget curl python json

WORKDIR /app

COPY . /app

RUN chmod -R 777 /app

CMD ["python", "/app/main.py"]
