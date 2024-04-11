import logging
from smtplib import SMTPAuthenticationError, SMTPException

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send(name, email, message=None):
    try:
        logging.info(f"Sending email to {email}")
        send_mail(
            subject=name,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[f"{email}"],
        )
        logging.info(f"Email sent to {email} successfully!")
    except (SMTPAuthenticationError, SMTPException) as e:
        logging.error(f"Error sending mail: {e}")
    except Exception as e:
        logging.error(f"Error: {e}")
