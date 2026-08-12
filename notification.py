from plyer import notification
from datetime import datetime, timedelta
import time

from storage import tasks, save_tasks


def send_notification(task):

    notification.notify(
        title="TODO Reminder",
        message=(
            f"{task.task} is due at "
            f"{task.due_time.strftime('%H:%M')}"
        ),
        timeout=10
    )


def check_reminders():

    while True:

        now = datetime.now()

        for task in tasks:

            if task.completed:
                continue

            time_left = task.due_time - now

            if (
                not task.reminder_sent
                and timedelta(0) <= time_left <= timedelta(minutes=5)
            ):

                send_notification(task)

                task.reminder_sent = True

                save_tasks()

        time.sleep(30)