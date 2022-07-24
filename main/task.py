from celery import shared_task
import smtplib as smtp
from .models import *


@shared_task
def send_message(em, id):
    email = 'u5ad44in@yandex.ru'
    password = '010100Aa#'
    dest_email = ['m_mirzafar@mail.ru']

    subject = 'SHANYRAQ'
    email_text = f'email: {em}'

    message = 'From: {}\nSubject: {}\n\n{}'.format(email, subject, email_text)

    server = smtp.SMTP_SSL('smtp.yandex.com')
    server.set_debuglevel(1)
    server.ehlo(email)
    server.login(email, password)
    server.sendmail(email, dest_email, message)
    server.quit()

    ch = Email.objects.get(id=int(id))
    ch.status = 1
    ch.save()


