# -*-coding:utf-8-*-
from flask import Blueprint
from flask_restful import Api

from albumy.api.comment.comment import Comment

comment_blueprint = Blueprint("comment", __name__, url_prefix="/api")
comment_api = Api(comment_blueprint, prefix="/comment")

comment_api.add_resource(Comment, '',"/<int:photo_id>")

