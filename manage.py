# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/11/20

from albumy.constant import *
from flask import render_template, abort
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from albumy.app import create_app

from albumy.settings import BaseConfig, DevConfig, get_config
from albumy.models import *
from albumy.utils.cache import get_cache_redis

config = get_config()
app = create_app(config=config)
# print(app.name)

# cache_redis=get_cache_redis(app.config["CACHE_REDIS_URL"])
manager = Manager(app)

Migrate(app, db)
manager.add_command("db", MigrateCommand)

@app.route("/")
def hello():
    return  "hello"


@app.route("/static/<regex('\w*\.{0,1}\w*'):filename>")
def static_manager(filename):
    # 设置可以被访问的静态文件

    if filename in STATIC_FILES:
        if filename.endswith(".html"):
            return render_template(filename)
    else:
        return render_template("404.html")


if __name__ == '__main__':
    manager.run()
