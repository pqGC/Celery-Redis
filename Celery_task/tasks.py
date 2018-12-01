from __future__ import absolute_import, unicode_literals
from Celery_task.celery_cnf import app
import time
import pika


# 爬虫相关
@app.task
def spider(*args):
    print('execute every one hour')


@app.task
def add(x, y):
    print('x + y = ', x+y)
    return x + y


@app.task
def RabbitMQ_test():
    """
    需要启动RabbitMQ项目的recv_msg3.py
    :return:
    """
    creds_broker = pika.PlainCredentials("test", "123456")
    # 定义连接池
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='127.0.0.1', port=5672, credentials=creds_broker))
    # 创建一个消息通道
    channel = connection.channel()
    # 创建一个消息队列，消息队列的名称为task_queue，
    # 这里的第二个参数durable，是对消息队列的设置，
    # 使得RabbitMQ在发生异常退出时发送的消息不会被丢失，该消息会被发送给其他消费者
    channel.queue_declare(queue='mytest')
    for i in range(10):
        channel.basic_publish(exchange='', routing_key='mytest', body=str(i),
                              # 注意当未定义exchange时，routing_key需和queue的值保持一致
                              properties=pika.BasicProperties(delivery_mode=2))  # mode>=2表示消息的持久化
        print('send success msg to rabbitmq   msg--->{}'.format(i))
    connection.close()  # 关闭连接
