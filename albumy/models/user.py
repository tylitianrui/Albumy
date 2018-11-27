# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/11/23
from albumy import constant
from albumy.extensions import db
from albumy.models.base.mixin import DeclarePK, PasswordUserMixin
from albumy.models.base.model import BaseModel


class User(DeclarePK, PasswordUserMixin, BaseModel):
    # 设置数据库的表名
    __tablename__ = "alb_user"

    user_no = db.Column(db.Integer, unique=True, nullable=False)
    user_name = db.Column(db.String(30), unique=True, nullable=False, index=True)
    email = db.Column(db.String(30), index=True, default="")
    mobile = db.Column(db.String(11), default="", index=True)
    active = db.Column(db.Integer, default=constant.USER_REGISTERED, unique=False)
