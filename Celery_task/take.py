from Celery_task.tasks import add

# 生产者
a = add.delay(10, 20)
print(a.result)  # 获取结果
print(a.ready)  # 是否处理
print(a.get(timeout=1))  # 获取结果
print(a.status)  # 是否处理

