# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/11/20

from flask import render_template
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from albumy.app import create_app
from albumy.constant import *
from albumy.models import *
from albumy.settings import get_config

config = get_config()
app = create_app(config=config)

manager = Manager(app)

Migrate(app, db)
manager.add_command("db", MigrateCommand)


@app.route("/")
def welcome():
    return "<h1>welcome! </br> this is albumy!<h1>"



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
