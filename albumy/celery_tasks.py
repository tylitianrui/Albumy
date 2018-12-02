# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/11/30
from __future__ import absolute_import

from flask_mail import Message

from albumy.celery_worker import celery_app, flask_app
from albumy.constant import EMAIL_TOPIC
from albumy.extensions import mail




@celery_app.task
def send_email(topic,recipients,**kwargs):
    topic = EMAIL_TOPIC.get(topic,"")

    if topic:
        topic.update(kwargs)
        print(topic)
        msg = Message(
            # 主题
            subject=topic.get("subject"),
            # subject="激活账号!",
            # 发送者
            sender=flask_app.config["MAIL_SENDER"],
            # 收信者
            recipients=[recipients],
            # 正文
            body=topic.get("body")

        )
        resource = topic.get("resource","")
        # 添加附件
        if resource:
            with flask_app.open_resource(resource) as fp:
                msg.attach("image.jpg", "image/jpg", fp.read())

        # 使用flask的上下文进行发送
        with flask_app.app_context():
            mail.send(msg)


@celery_app.task
def send_emails(users):
    with mail.connect() as conn:
        for user in users:
            message = '...'
            subject = "hello, %s" % user.name
            msg = Message(recipients=[user.email],
                          body=message,
                          subject=subject)

            conn.send(msg)




