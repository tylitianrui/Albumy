# -*-coding:utf-8-*-
from flask import g

from albumy.api.albumy.const import VISIBLE_PUBLIC, VISBLE_FOLLOWER
from albumy.common.restful import RestfulBase, raise_400_response, success_response
from albumy.extensions import login_required, db
from albumy.models import Albumy as AlbumyModel, User as UserModel, FollowerModel


class OthersAlbumy(RestfulBase):
    def _permission_view_albumy(self, user_id, albumy_owner_id, albumy_id=None):
        #  判断是否是相册主人的粉丝
        rel = FollowerModel.query.filter_by(uid=user_id, fid=albumy_owner_id).first()
        if albumy_id:
            query =AlbumyModel.query.filter(AlbumyModel.id == albumy_id)
        else:
            query = AlbumyModel.query

        albumy_list = query.filter(AlbumyModel.user_id == albumy_owner_id) \
            .filter(AlbumyModel.visible == VISIBLE_PUBLIC).all()
        if rel:
            _albumy_list = query.filter(AlbumyModel.user_id == albumy_owner_id) \
                .filter(AlbumyModel.visible == VISBLE_FOLLOWER).all()
            albumy_list.extend(_albumy_list)
        return albumy_list

    @login_required
    def get(self, user_id, id=None):
        if not user_id:
            return raise_400_response()
        owner = UserModel.get_by_id(user_id)
        if not owner:
            return raise_400_response(message="用户不存在")
        user = g.current_user
        albumy_list = self._permission_view_albumy(user.id, owner.id,id)
        data = [albumy.get_info() for albumy in albumy_list if albumy]
        return success_response(data=data)
