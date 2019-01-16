# -*-coding:utf-8-*-
from albumy.extensions import db
from albumy.models import DeclarePK, BaseModel


class Role(DeclarePK, BaseModel):
    __tablename__ = "alb_role"
    role_code = db.Column(db.Integer, nullable=False)
    desc = db.Column(db.String(50), nullable=False)
