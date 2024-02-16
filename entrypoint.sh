#!/bin/sh

# Start my DRF application
exec /bin/sh -c "python manage.py migrate \
                && python manage.py collectstatic --no-input \
                && gunicorn --bind :8000 config.wsgi:application"

chmod +x entrypoint.sh