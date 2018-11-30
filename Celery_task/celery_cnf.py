from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery.schedules import crontab

# 服务器
# app = Celery('Scheduler', broker='redis://localhost:6379/0',
#              backend='redis://localhost:6379/1', include=['Scheduler.tasks'])
# 本机
app = Celery('Celery_task', broker='redis://127.0.0.1:6379/0', backend='redis://127.0.0.1:6379/1',
             include=['Celery_task.tasks'])


app.conf.beat_schedule = {
    'spider-at-noon-execute-five': {
        'task': 'Celery_task.tasks.add',
        'schedule': crontab(minute='*/1'),
        'args': (5, 6)
    },
}
app.conf.timezone = 'UTC'


if __name__ == "__main__":
    app.start()
