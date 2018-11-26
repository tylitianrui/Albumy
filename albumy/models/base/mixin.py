# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/11/23
from flask import current_app
from flask_login import UserMixin
from itsdangerous import Serializer

from albumy.extensions import db


class CURDMixin(object):
    pass


class DeclarePK(object):
    id = db.Column(db.Integer, primary_key=True)

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)


class PasswordUserMixin(UserMixin):
    password = db.Column(db.String(128), nullable=True)

    def set_hash_password(self, password, commit=True):
        # todo  ltr{warn}ltr 暂且明文
        self.password = password
        if commit:
            self.save()

    def check_password(self, value):
        return self.password == value

    def generate_auth_token(self, expire=3600 * 24 * 12):
        s = Serializer(current_app.config["SECRET_KEY"], expires_in=expire)
        return s.dumps({"id": self.id}).decode("ascii")

    @property
    def password(self):
        return "无权限"

    @password.setter
    def password(self,password):
        self.set_hash_password(password)



