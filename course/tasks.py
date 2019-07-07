from datetime import datetime, timedelta
from django_rq import job
from .models import Notification
from redis import Redis
from rq_scheduler import Scheduler


@job("default")
def send_notifications():
    notifications = Notification.objects.filter(is_send=False)
    for notification in notifications:
        result = send_email(notification.email, notification.email_content)

        if result is True:
            notification.is_send = True
            notification.save(update_fields=['is_send'])

    return True

send_notifications.delay()
redis_conn = Redis()
scheduler = Scheduler(connection=redis_conn)
# scheduler = django_rq.get_scheduler('default')
job = scheduler.enqueue_in(timedelta(seconds=5), send_notifications)

def send_email(email, content):
    # Заглушка
    return True