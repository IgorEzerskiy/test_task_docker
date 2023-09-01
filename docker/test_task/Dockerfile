FROM python:3.10.12-alpine

RUN apk update && apk add python3-dev gcc libc-dev

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install gunicorn
ADD ./requirements.txt /app/
RUN pip install -r requirements.txt

ADD ./test_task /app/test_task
ADD ./docker /app/docker

RUN chmod +x /app/docker/test_task/server-entrypoint.sh
RUN chmod +x /app/docker/test_task/worker-entrypoint.sh
