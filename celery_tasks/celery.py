# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/11/29

from __future__ import absolute_import
from celery import Celery
app = Celery("celery_tasks",include=["celery_tasks.tasks"])
app.config_from_object("celery_tasks.config")
if __name__ == '__main__':
    app.start()