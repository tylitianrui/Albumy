# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/12/1

# celery的定时任务
from datetime import timedelta


class Schedule(object):

    CELERYBEAT_SCHEDULE = {
        # 定时任务
        "email": {
            # 引入任务
            "task": "albumy.celery_tasks.send_email",
            # 时间间隔
            "schedule": timedelta(seconds=60),
            # 参数
            "args": (1,2,3)
        }
    }
