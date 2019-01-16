# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/11/23
from albumy import constant
from albumy.models.base.mixin import DeclarePK, PasswordUserMixin, declare_foreign_key
from albumy.models.base.model import BaseModel
from datetime import datetime as dt
from albumy.extensions import db


class User(DeclarePK, PasswordUserMixin, BaseModel):
    # 用户登录信息，账号 密码等
    # 设置数据库的表名
    __tablename__ = "alb_user"

    # 用户账号，系统自定生成，运行用户修改一次，例如微信号
    user_name = db.Column(db.String(30), unique=True, nullable=False, index=True)
    reset_user_name = db.Column(db.Boolean, default=False)  # 是否已经自定义过用户账号
    email = db.Column(db.String(30), index=True, default="")
    mobile = db.Column(db.String(11), default="", index=True)
    active = db.Column(db.Integer, default=constant.USER_REGISTERED, unique=False)
    last_login = db.Column(db.DateTime, default=dt.now, index=True)
    # role_code = declare_foreign_key("alb_role")


class UserProfile(DeclarePK, BaseModel):
    # 用户个人信息表
    __tablename__ = "alb_user_profile"
    user_id = declare_foreign_key("alb_user")
    nickname = db.Column(db.String(16), default="", index=True)
    age = db.Column(db.Integer, default=0, index=True)
    head_url = db.Column(db.String(120), default="")
    gender = db.Column(db.Integer, default=0)  # 1 男 2 女  0 未设置

    # 真实信息
    name = db.Column(db.String(16), default="")
    address = db.Column(db.String(60), default="")
