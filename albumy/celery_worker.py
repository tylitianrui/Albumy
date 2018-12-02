# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/11/30
from __future__ import absolute_import
from celery import Celery

from albumy.app import create_app
from albumy.celery_schedule import Schedule
from albumy.settings import get_config

config = get_config()
flask_app = create_app(config, celery=True)

# 任务列表，异步任务会在此文件中查找 例如celery_tasks 文件中查找
# 如果是多文件的话，在此增加任务文件
tasks_list = ["albumy.celery_tasks"]
celery_app = Celery(
    flask_app.name,
    # 设置broker   backend
    broker=flask_app.config["CELERY_BROKER_URL"],
    backend=flask_app.config["CELERY_RESULT_BACKEND"],
    # 引入，此处引入的是任务
    include=tasks_list
)
# 配置
celery_app.config_from_object(config)

# 添加定时任务的配置
# celery_app.config_from_object(Schedule)
