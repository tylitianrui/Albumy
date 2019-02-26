# -*-coding:utf-8-*-
from flask import Blueprint
from flask_restful import Api

from albumy.api.comment.comment import Comment
from albumy.api.comment.picture_comment import PhotoComment

comment_blueprint = Blueprint("comment", __name__, url_prefix="/api")
comment_api = Api(comment_blueprint, prefix="/comment")

comment_api.add_resource(Comment, "", "/<int:comment_id>")


photo_comment_blueprint = Blueprint("photo_comment", __name__, url_prefix="/api")
photo_comment_api = Api(photo_comment_blueprint, prefix="/photo_comment")
photo_comment_api.add_resource(PhotoComment, "/<int:photo_id>")
