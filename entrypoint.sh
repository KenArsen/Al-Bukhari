#!/bin/sh

# Start my DRF application
exec /bin/sh -c "python manage.py migrate \
                && python manage.py collectstatic --no-input \
                && gunicorn --bind :8000 config.wsgi:application"

# Create super user
python manage.py shell -c "from apps.user.models import User; \
User.objects.create_superuser('admin@gmail.com', 'admin') if not User.objects.filter(email='admin@gmail.com').exists() else None"

chmod +x entrypoint.sh