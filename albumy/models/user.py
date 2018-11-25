# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/11/23
from albumy.extensions import db
from albumy.models.base.mixin import DeclarePK
from albumy.models.base.model import BaseModel


class User(DeclarePK,BaseModel):
    __tablename__ = "alb_user"

    user_no = db.Column(db.Integer,unique=True,nullable=False)
