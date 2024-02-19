#!/bin/sh

# Start my DRF application
python manage.py migrate
python manage.py collectstatic --no-input

# Create super user
python manage.py shell -c "from apps.user.models import User; \
User.objects.create_superuser(email='admin@gmail.com', password='admin') if not User.objects.filter(email='admin@gmail.com').exists() else None"

exec /bin/sh -c "gunicorn --bind :8000 config.wsgi:application"

chmod +x entrypoint.sh