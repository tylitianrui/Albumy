# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/11/23
from albumy import constant
from albumy.models.base.mixin import DeclarePK, PasswordUserMixin
from albumy.models.base.model import BaseModel
from datetime import datetime as dt
from albumy.extensions import db


class User(DeclarePK, PasswordUserMixin, BaseModel):
    # 设置数据库的表名
    __tablename__ = "alb_user"

    user_name = db.Column(db.String(30), unique=True, nullable=False, index=True)
    email = db.Column(db.String(30), index=True, default="")
    mobile = db.Column(db.String(11), default="", index=True)
    active = db.Column(db.Integer, default=constant.USER_REGISTERED, unique=False)
    last_login = db.Column(db.DateTime, default=dt.now, index=True)
