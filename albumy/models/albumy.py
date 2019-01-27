# -*-coding:utf-8-*-
from albumy.models import DeclarePK, BaseModel, db, declare_foreign_key


class Albumy(DeclarePK, BaseModel):
    __tablename__ = "albumy"
    title = db.Column(db.String(20), nullable=False)  # 相册标题
    user_id = declare_foreign_key("alb_user", index=True)  # 相册主人
    sort_id = declare_foreign_key("alb_post_sort")  # 类别
    cap = db.Column(db.Integer, nullable=False)  # 容量
    visible = db.Column(db.Integer, nullable=False)  # 可见，例如尽自己、粉丝可见。。。。


class PostSort(DeclarePK, BaseModel):
    """相册分类"""
    __tablename__ = "alb_post_sort"
    user_id = declare_foreign_key("alb_user")
    name = db.Column(db.String(20), nullable=False)
    desc = db.Column(db.String(50), nullable=False)


class Photo(DeclarePK, BaseModel):
    __tablename__ = "alb_photo"
    albumy_id = declare_foreign_key("albumy")
    title = db.Column(db.String(20), nullable=False)
    url = db.Column(db.String(100), nullable=False)


class Comment(DeclarePK, BaseModel):
    __tablename__ = "alb_photo_comment"
    photo_id = declare_foreign_key("alb_photo")
    user_id = declare_foreign_key("alb_user")
    content = db.Column(db.String(100), nullable=False)
    parent_id = declare_foreign_key("alb_photo_comment")


class PhotoLike(DeclarePK, BaseModel):
    __tablename__ = "alb_photo_like"
    photo_id = declare_foreign_key("alb_photo")
    user_id = declare_foreign_key("alb_user")



