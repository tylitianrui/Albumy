# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/11/20
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bootstrap = Bootstrap()
# 散列值
bcrypt = Bcrypt()

# 邮件
mail = Mail()