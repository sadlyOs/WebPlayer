import smtplib
from email.message import EmailMessage
from celery import Celery

task = Celery("tasks", broker = 'redis://localhost:6379')
async def get_email_template(username: str, email_to: str):
    email = EmailMessage()
    email["Subject"] = "Тест письмо"
    email["From"] = "ppingvinov00@gmail.com"
    email["To"] = email_to

    email.set_content(
        "You have registered successfully"
    )
    return email

@task.task
async def send_email(username: str, email: str):
    email_to = await get_email_template(username, email)
    async with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        await server.login("ppingvinov00@gmail.com", "jynq qezg kqyz wajc")
        await server.send_message(email_to)