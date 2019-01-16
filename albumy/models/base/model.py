# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/11/23
from datetime import datetime as dt

from albumy.extensions import db
from albumy.models.base.mixin import CRUDMixin


class BaseModel(CRUDMixin, db.Model):
    """model的基类"""
    __abstract__ = True  # 设置抽象类
    # 创建 更新时间
    created_at = db.Column(db.DateTime,default=dt.now)
    updated_at = db.Column(db.DateTime,default=dt.now)
    is_delete = db.Column(db.Boolean,default=False,nullable=False)



