# -*-coding:utf-8-*-
from flask import g
from flask_restful import reqparse

from albumy.common.restful import RestfulBase, success_response, raise_401_response, raise_400_response, \
    raise_404_response
from albumy.extensions import login_required, db
from albumy.models import Photo as PhotoModel, Comment as  CommentModel, User
from albumy.utils.validate import validate_comment


class Comment(RestfulBase):
    @login_required
    def get(self, comment_id=None):
        if not comment_id:
            return raise_400_response()
        comment = CommentModel.get_by_id(comment_id)
        if not comment:
            return raise_404_response()
        return success_response(data=comment.get_comment())


    @login_required
    def post(self):
        req = reqparse.RequestParser()
        current_user = g.current_user

        req.add_argument("photo_id", type=int, required=True, location="json")
        req.add_argument("content", type=validate_comment, required=True, location="json")
        req.add_argument("parent_comment", type=int, location="json")
        args = req.parse_args()
        fields = {
            "photo_id": args["photo_id"],
            "user_id": current_user.id,
            "content": args["content"]
        }
        if args["parent_comment"]:
            fields["parent_id"] = args["parent_comment"]
        comment = CommentModel.create(**fields)
        return success_response(status_code=201, message="创建成功")
