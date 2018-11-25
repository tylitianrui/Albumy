# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/11/23
from albumy.extensions import db


class CURDMixin(object):
    pass


class DeclarePK(object):
    id = db.Column(db.Integer, primary_key=True)

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)
