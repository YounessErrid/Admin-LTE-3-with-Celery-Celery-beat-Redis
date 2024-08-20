from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def say_hello():
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Hello, world!")


@shared_task
def send_daily_email():
    # Replace with your email logic
    send_mail(
        subject='Daily Report from django',
        message='This is your daily report!',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=['user@test.com'],  # Replace with actual recipient
        fail_silently=False,
    )
    print("Daily email sent.")