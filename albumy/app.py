# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/11/20
from flask import Flask

from albumy.extensions import db, bootstrap, bcrypt, mail, redis_client


def create_app(config, celery=False):
    app = Flask(__name__)
    app.config.from_object(config)
    init_extensions(app)
    if not celery:
        register_blueprint(app)
        regiester_convreter(app)
    return app


def init_extensions(app):
    db.init_app(app)
    bootstrap.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)
    # cache.init_app(app)
    redis_client.init_app(app)
    return None


def register_blueprint(app):
    from albumy.api import user_blueprint
    from albumy.api import follower_blueprint
    from albumy.api import albumy_blueprint

    app.register_blueprint(user_blueprint)
    app.register_blueprint(follower_blueprint)
    app.register_blueprint(albumy_blueprint)
    return None


def regiester_convreter(app):
    """
    注册自定义的转化器
    :param app:
    :return:

    """
    # todo ltr{doc}ltr :自定义转换器
    """
    flask的 url默认有 int path  string  float 等转换器，以便于获取url中信息(restful)，默认是string
    例如：
    /student/<int:stuid>  获取stuid  
    /book/<title>    获取title 
    原理：url中转换器是根据BaseConverter中regex进行匹配的。各种转换器的regex是固定的。例如
    float 转化器  regex = r'\d+\.\d+'
    path  转换器  regex = '[^/].*?'
    如过需要定制化的转换器，实现‘个性化’地获取url的数据怎么办？自定义转换器。实现步骤如下：
    1.集成 BaseConverter，把regex作为参数传入，而不是固定写死的。这样就可以根据用户传入regex进行过滤了
    2.将自定义的转换器添加到转换器字典中，供程序调用。完成
    url中即可使用方式：
    /<regex('\w{1,2}\.\w+'):name>    
    # 此处的regex 为添加转化器的key，即 app.url_map.converters["regex"] = RegexConverter 中的key，regex
    def index(name):
        .....
    
    延伸：既然可将regex作为参数传入，那么也可以传入其他参数 if you  want
    可参源码 UnicodeConverter 类 length
    
    """
    from albumy.converter import RegexConverter
    app.url_map.converters["regex"] = RegexConverter
    return None
