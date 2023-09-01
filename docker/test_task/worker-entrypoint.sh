#!/bin/sh

until cd /app/test_task
do
    echo "Waiting for server volume..."
done

# run a worker :)
celery -A test_task worker -B --loglevel=info
