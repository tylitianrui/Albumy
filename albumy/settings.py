# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/11/20


class BaseConfig(object):
    SECRET_KEY = "w1rr1lelsnvorhjfob2ctc*!@adcvgtvrt@@1"
    # mysql
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost:3306/albumy?charset=utf8mb4'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:lttrrr035499@localhost:3306/albumy?charset=utf8mb4'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # redis

    # 邮件
    MAIL_SERVER = 'smtp.126.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'tyltr_test@126.com'
    MAIL_PASSWORD = 'qaz2y34sXcf1'
    MAIL_SENDER = u"tyltr <tyltr_test@126.com>"

    # celery
    CELERY_BROKER_URL = "redis://localhost:6379/1"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/1"


class DevConfig(BaseConfig):
    DEBUG = True


class ProdConfig(BaseConfig):
    pass


def get_config():
    pass
