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

    # celery 配置
    CELERY_BROKER_URL = "redis://localhost:6379/1"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/1"
    # 任务序列化反序列化采用 msgpack，任务结果采用json
    # todo ltr{doc}ltr
    """
    msgpack  json 都是数据交换的格式
    但是msgpack是二进制文件，比json性能更加高，而且更小
    但json的可读性高
    
    """
    CELERY_TASK_SERIALIZER = "msgpack"
    CELERY_RESULT_SERIALIZER = "json"  # 读取任务结果一般对性能的要求不高，所以使用可读性更好的json

    # 任务的过期时间
    CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24

    # 接受的内容类型
    CELERY_ACCEPT_CONTENT = ["json", "msgpack"]


class DevConfig(BaseConfig):

    DEBUG = True


class ProdConfig(BaseConfig):
    pass


def get_config():
    return DevConfig
