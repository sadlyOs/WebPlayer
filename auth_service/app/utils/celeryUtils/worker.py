import smtplib
import loguru
from datetime import timedelta
from email.message import EmailMessage

from app.core.config import settings
# from app.core.config import settings
from app.services.user_services import UserService

from celery import Celery

celery = Celery(__name__, broker = f'redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}')
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

def create_email_message(message, email_getter):
    """Create a new email message"""
    email = EmailMessage()
    email.set_content(message)
    email['Subject'] = 'Drope code'
    email['From'] = settings.SMTP_USER
    email['To'] = email_getter
    return email

@celery.task
def create_task(email: str, result: str, task="create_task"):
    email_message = create_email_message(message = f'Your drope code is: {result}', email_getter = email)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
        server.send_message(email_message)
