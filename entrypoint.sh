#!/bin/sh

# Start my DRF application
python manage.py migrate
python manage.py collectstatic --no-input
exec /bin/sh -c "gunicorn --bind :8000 config.wsgi:application"

chmod +x entrypoint.sh