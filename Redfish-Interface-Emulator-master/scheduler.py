import logging
import os
import psutil

from apscheduler.schedulers.background import BackgroundScheduler
from flask_mail import Mail, Message

import g

logging.basicConfig()
mail = Mail(g.app)


def check_system_health():
    """
    Calculate system memory related information and trigger alert notifications if occupied completely.
    :return:
    """
    virtual_memory = psutil.virtual_memory()
    # Checking with sample value.
    if virtual_memory.available < 1814634112:
        # TODO: Need to trigger notify method. with required params.
        # Ex: notify("Notification on system storage outrange", "Message", ['xxx@gmail.com'])
        print("#########################Trigger notification e-mail for admins########################")
    else:
        print("System storage didn't run out of way!..")
    return True


def notify(subject, message, to):
    msg = Message(subject, sender='xxxx@gmail.com', recipients=to)
    msg.body = message
    mail.send(msg)
    return True


def schedule():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_system_health, 'interval', seconds=30)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
