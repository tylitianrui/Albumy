# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/11/20
from flask import Flask


from albumy.extensions import db,bootstrap


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    init_extensions(app)
    register_blueprint(app)
    regiester_convreter(app)


    return app


def init_extensions(app):
    db.init_app(app)
    bootstrap.init_app(app)
    return None


def register_blueprint(app):

    return None


def regiester_convreter(app):
    """
    注册自定义的转化器
    :param app:
    :return:
    """
    from albumy.converter import RegexConverter
    app.url_map.converters["regex"] = RegexConverter
    return None
