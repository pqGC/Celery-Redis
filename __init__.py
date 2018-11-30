"""
celery  -A Scheduler worker -f task.log -l info --detach

celery  -A Scheduler beat -f  periodic_task.log -l info --detach
"""