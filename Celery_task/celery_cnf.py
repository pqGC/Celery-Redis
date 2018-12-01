from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery.schedules import crontab


"""
启动Celery命令： celery -A Celery_task.celery_cnf worker -l info -P eventlet
启动beat定时任务：celery beat -A Celery_task.celery_cnf -l info
"""


# 服务器
# app = Celery('Scheduler', broker='redis://localhost:6379/0',
#              backend='redis://localhost:6379/1', include=['Scheduler.tasks'])
# 本机 Redis
# app = Celery('Celery_task', broker='redis://127.0.0.1:6379/0', backend='redis://127.0.0.1:6379/1',
#              include=['Celery_task.tasks'])
# 本机 RabbitMQ
app = Celery('Celery_task',
             broker='amqp://test:123456@127.0.0.1:5672/',
             backend='amqp://test:123456@127.0.0.1:5672/',
             include=['Celery_task.tasks'])


app.conf.beat_schedule = {
    'spider-at-noon-execute-five': {
        'task': 'Celery_task.tasks.add',
        'schedule': crontab(minute='*/1'),
        'args': (5, 6)
    },
}


app.conf.beat_schedule = {
    'RabbitMQ-at-noon-execute-hour': {
        'task': 'Celery_task.tasks.RabbitMQ_test',
        'schedule': crontab(minute='*/1'),
        'args': ()
    },
}
app.conf.timezone = 'UTC'


if __name__ == "__main__":
    app.start()
