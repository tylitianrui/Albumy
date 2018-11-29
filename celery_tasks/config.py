# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/11/29

BROKER_URL = "redis://localhost:6379/1"
# BROKER_URL = "redis://localhost:6379/1"
# todo 官方推荐适应rabbitmq，因为celery的设计就是基于rabbitmq 当本程序没有配置好rebbitmq
CELERY_RESULT_BACKEND = "redis://localhost:6379/1"
CELERY_TASK_SERIALIZER = "msgpack"

CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
CELERY_ACCEPT_CONTENT = ["json", "msgpack"]
