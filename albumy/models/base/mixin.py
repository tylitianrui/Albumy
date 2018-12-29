# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/11/23
from datetime import datetime

from flask import current_app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

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
        # 更新时间
        setattr(self, "updated_at", datetime.now())

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
    def is_exist(cls, **kv):
        """
            判断某字段k上是否有某值v
            :param kv: {k:v}
            :return:
            """

        _instance = cls(**kv)
        if _instance.query.filter_by(**kv).first():
            return True
        return False


class DeclarePK(object):
    id = db.Column(db.Integer, primary_key=True)

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)


class PasswordUserMixin(UserMixin):
    password_hash = db.Column(db.String(128), nullable=True)

    def set_hash_password(self, password, commit=True):
        """
        产生哈希密码
        :param password:
        :param commit:
        :return:
        """
        # 密码

        self.password_hash = bcrypt.generate_password_hash(password)
        if commit:
            self.save()

    def check_password(self, value):
        """
        校验密码
        :param value:
        :return:
        """

        return bcrypt.check_password_hash(self.password_hash, value)

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

    @password.setter
    def password(self, password):
        self.set_hash_password(password)


def declare_foreign_key(table, pk='id', nullable=False, **kwargs):
    return db.Column(
        db.ForeignKey('{}.{}'.format(table, pk)),
        nullable=nullable, **kwargs)


def declare_union_index(table_name_in_db, *args):
    # todo
    """
    声明复合索引
    :param table_name_in_db: 在数据库里面的表名
    :param args: [(a,b),(c,d),(e,f,g)]  声明三个复合索引a_b, c_d,  e_f_g
    :return:
    """
    uixs = []
    for uix in  args:
        uixs.append(db.UniqueConstraint(uix, name='uix_{}_{}'.format(table_name_in_db,"_".join(uix))),)

    return (
        db.UniqueConstraint('user_id', 'post_id', name='uix_user_post_user_id_post_id'),
        db.Index('ix_user_post_user_id_insert_time', 'user_id', 'insert_time'),
    )
