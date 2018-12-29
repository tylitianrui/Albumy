# -*-coding:utf-8-*-
from albumy.extensions import db
from albumy.models import DeclarePK, BaseModel
from albumy.models.base.mixin import declare_foreign_key


class Follower(DeclarePK, BaseModel):
    """
    uid的关注者是fid，fid关注了uid
    """
    __tablename__ = "alb_follower"
    uid = declare_foreign_key("alb_user", index=True)
    fid = declare_foreign_key("alb_user", index=True)
    is_cancel_follow = db.Column(db.Boolean(),default=False)
