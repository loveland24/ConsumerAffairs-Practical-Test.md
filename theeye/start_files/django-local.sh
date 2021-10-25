#!/usr/bin/env bash

python manage.py migrate
python manage.py collectstatic --noinput
celery multi start rabbit -c 3 -A theeye --loglevel=DEBUG -Q theEye  --logfile=/var/logs/celery/worker-%n%I.clog --pidfile=/var/run/celery/worker%n.pid
python manage.py runserver 0.0.0.0:8000
