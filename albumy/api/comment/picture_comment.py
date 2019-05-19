# -*-coding:utf-8-*-

from albumy.common.restful import RestfulBase, success_response, raise_400_response
from albumy.extensions import login_required
from albumy.models import Comment as CommentModel, Photo
from albumy.utils.validate import validate_comment
from flask import g
from flask_restful import reqparse


class PhotoComment(RestfulBase):
    @login_required
    def get(self, photo_id):
        """
        获取某照片的评论
        :param photo_id:
        :return:
        """
        comments = CommentModel.query.filter_by(photo_id=photo_id, is_delete=False).all()
        if not comments:
            return success_response()
        _data = []
        for item in comments:
            cm = item.get_comment()
            _data.append(cm)
        return success_response(data=_data)

    @login_required
    def post(self):
        req = reqparse.RequestParser()
        req.add_argument("photo_id", type=int, required=True, location="json")
        req.add_argument("comment", type=validate_comment, location="json")
        req.add_argument("userid", type=int, location="json")
        req.add_argument("parent_id", type=int, location="json")
        args = req.parse_args()
        if g.current_user != args["userid"]:
            return raise_400_response(message=u"认证失败")
        photo = Photo.get_by_id(args["photo_id"])
        if not photo:
            return raise_400_response(message=u"此照片不存在")
        parent_comment = CommentModel.query.filter_by(id=args["parent_id"], is_delete=False).first()
        if not parent_comment:
            return raise_400_response(message=u"父级评论参数有误")

        parent_id = args["parent_id"] if args["parent_id"] else 0
        fields = dict(photo_id=args["photo_id"], comment=args["comment"], userid=args["userid"], parent_id=parent_id)
        CommentModel.create(commit=True, **fields)
        return success_response()
