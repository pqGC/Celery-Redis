from __future__ import absolute_import, unicode_literals
from Celery_task.celery_cnf import app
import time


# 爬虫相关
@app.task
def spider(*args):
    print('execute every one hour')


@app.task
def add(x, y):
    print('x + y = ', x+y)
    return x + y
