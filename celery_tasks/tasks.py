# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/11/29

from __future__ import absolute_import

from celery_tasks.celery import app

@app.task
def add(x,y):
    return x+y
