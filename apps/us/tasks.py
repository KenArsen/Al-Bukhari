import logging
from smtplib import SMTPAuthenticationError, SMTPException

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.exceptions import ValidationError


@shared_task
def send(**data):
    try:
        logging.info(f"Sending email to {data['email']}")
        send_mail(
            subject=data['name'],
            message=data['message'],
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[f"{data['email']}"],
        )
        logging.info(f"Email sent to {data['email']} successfully!")
    except (SMTPAuthenticationError, SMTPException) as e:
        raise ValidationError({'error': str(e)})
    except Exception as e:
        raise ValidationError({'error': str(e)})
