# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/11/30
from __future__ import absolute_import

from flask_mail import Message

from albumy.celery_worker import celery_app, flask_app
from albumy.extensions import mail




@celery_app.task
def send_email(recipients,subject,body):
    msg = Message(
        subject="Hello 1111111World!",
        sender=flask_app.config["MAIL_SENDER"],
        recipients=["913173651@qq.com"],
        body="""<img class="s-news-img" src="https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq/it/u=1094860756,3266178535&amp;fm=173&amp;app=49&amp;f=JPEG?w=218&amp;h=146&amp;s=F6A19E0DA4CD514714A9ADC90300F0B7" height="119" width="179">"""
    )
    # 使用flask的上下文
    with flask_app.app_context():
        mail.send(msg)



