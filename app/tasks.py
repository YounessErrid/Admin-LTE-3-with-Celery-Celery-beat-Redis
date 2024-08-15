from celery import shared_task

@shared_task
def my_periodic_task():
    # Your scheduled task logic here
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Periodic task executed!")


@shared_task
def say_hello():
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Hello, world!")