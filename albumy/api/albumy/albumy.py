# -*-coding:utf-8-*-
from flask import g
from flask_restful import reqparse

from albumy.api.albumy.const import VISIBLE_PUBLIC, TYPE_DEFAULT
from albumy.common.restful import RestfulBase, success_response
from albumy.extensions import login_required
from albumy.models import Albumy as AlbumyModel


class Albumy(RestfulBase):
    @login_required
    def post(self):
        req = reqparse.RequestParser()
        req.add_argument("title", type=str, required=True, location="json")
        req.add_argument("sort_id", type=int, default=TYPE_DEFAULT, location="json")
        req.add_argument("visible", type=int, default=VISIBLE_PUBLIC, location="json")
        args = req.parse_args()
        user = g.current_user
        fields = dict(
            user_id=user.id,
            title=args.title,
            sort_id=args.sort_id,
            visible=args.visible,
            cap=0,
        )

        albumy = AlbumyModel.create(**fields)
        return success_response(status_code=201, data=albumy.get_all_info(), message="创建成功")

    @login_required
    def get(self, id=None):
        user = g.current_user
        albumy_query = AlbumyModel.query.filter_by(user_id=user.id, is_delete=False)
        if not id:
            albumies = albumy_query.all()
            data = [albumy.get_all_info_serializable() for albumy in albumies if albumy]
            return success_response(data=data)
        albumy = albumy_query.filter_by(id=id).first()
        data = albumy.get_all_info_serializable()
        return success_response(data=data)
