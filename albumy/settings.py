# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/11/20


class BaseConfig(object):
    SECRET_KEY="w1rr1lelsnvorhjfob2ctc*!@adcvgtvrt@@1"
    # mysql
    SQLALCHEMY_DATABASE_URI = 'mysql://root:lttrrr035499@localhost:3306/albumy?charset=utf8mb4'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    #redis



class DevConfig(BaseConfig):
    DEBUG=True



class ProdConfig(BaseConfig):
    pass


def get_config():
    pass