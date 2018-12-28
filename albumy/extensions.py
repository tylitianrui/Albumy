# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/11/20
import redis
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_httpauth import HTTPBasicAuth

from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

from albumy.common.redis_client import RedisClient

db = SQLAlchemy()
bootstrap = Bootstrap()
# 散列值
bcrypt = Bcrypt()

# 邮件
mail = Mail()

# redis
redis_client = RedisClient()

from albumy.common.authenticate import AlbumyAuth

albumy_user = AlbumyAuth()
login_required = albumy_user.auth.login_required
varify_password = login_required
