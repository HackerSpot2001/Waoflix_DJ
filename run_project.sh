#!/bin/sh
python3 manage.py migrate --noinput
python3 manage.py collectstatic --noinput
gunicorn waoflix_app.wsgi:application --bind 0.0.0.0:8000