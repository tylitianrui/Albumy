# -*-coding:utf-8-*-
from datetime import datetime

from flask import g
from flask_restful import reqparse

from albumy.common.restful import RestfulBase, raise_400_response, success_response
from albumy.extensions import login_required
from albumy.models import User, FollowerModel


class Follower(RestfulBase):
    @login_required
    def post(self):
        req = reqparse.RequestParser()
        # 我要关注的人 follow_id
        req.add_argument("follow_id", type=int, default="", location="json")
        req.add_argument("cancel", type=bool, default=False, location="json")
        args = req.parse_args()
        follow_id = args["follow_id"]
        to_follow = User.get_by_id(follow_id)
        if not to_follow:
            return raise_400_response()
        user = g.current_user
        follow_relationship = FollowerModel.query.filter_by(uid=user.id, fid=follow_id).first()
        if not follow_relationship:
            fields = {
                "uid": user.id,
                "fid": follow_id
            }
            FollowerModel.create(**fields)
            return success_response(status_code=0, message="关注成功")
        fields = dict(
            is_cancel_follow=args["cancel"],
            updated_at=datetime.now()
        )
        if args["cancel"]:
            follow_relationship.update(**fields)
            return success_response(status_code=1, message="取消关注")
        else:

            follow_relationship.update(**fields)
            return success_response(status_code=0, message="关注成功")
