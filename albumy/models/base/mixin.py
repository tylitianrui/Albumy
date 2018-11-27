# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/11/23
from flask import current_app
from flask_login import UserMixin
from itsdangerous import Serializer

from albumy.extensions import db, bcrypt


class CRUDMixin(object):
    """Mixin that adds convenience methods for CRUD (create, read, update, delete) operations."""

    @classmethod
    def create(cls, commit=True, **kwargs):
        """Create a new record and save it the database."""
        instance = cls(**kwargs)
        if commit:
            return instance.save()
        else:
            db.session.add(instance)
            return instance

    def update(self, commit=True, **kwargs):
        """Update specific fields of a record."""
        for attr, value in kwargs.items():
            setattr(self, attr, value)

        return commit and self.save() or self

    def save(self, commit=True):
        """Save the record."""
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        """Remove the record from the database."""
        db.session.delete(self)
        return commit and db.session.commit()

    @classmethod
    def is_exist(cls, kv):
        """
            判断某字段k上是否有某值v
            :param kv: {k:v}
            :return:
            """
        kv.update({"id_deleted": False})
        if cls.query.filter_by(**kv).first():
            return True
        return False


class DeclarePK(object):
    id = db.Column(db.Integer, primary_key=True)

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)


class PasswordUserMixin(UserMixin):
    password = db.Column(db.String(128), nullable=True)

    def set_hash_password(self, password, commit=True):
        """
        产生哈希密码
        :param password:
        :param commit:
        :return:
        """
        # 密码
        self.password = bcrypt.generate_password_hash(password)
        if commit:
            self.save()

    def check_password(self, value):
        """
        校验密码
        :param value:
        :return:
        """
        return bcrypt.check_password_hash(self.password, value)

    def generate_auth_token(self, expire=3600 * 24 * 12):
        """
        产生认证token
        :param expire: token过期时间
        :return:
        """
        s = Serializer(current_app.config["SECRET_KEY"], expires_in=expire)
        return s.dumps({"id": self.id}).decode("ascii")

    @property
    def password(self):
        return "无权限"
