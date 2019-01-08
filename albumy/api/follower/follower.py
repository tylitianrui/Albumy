# -*-coding:utf-8-*-
from datetime import datetime

from flask import g
from flask_restful import reqparse

from albumy.common.restful import RestfulBase, raise_400_response, success_response
from albumy.constant import USER_ACTIVE
from albumy.extensions import login_required, db
from albumy.models import User, User as  UserModel, FollowerModel, UserProfile


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


class FollowerList(RestfulBase):
    @login_required
    def get(self, type=None):
        current_user = g.current_user
        print(current_user.id)
        # 默认是我关注的人
        if type == "follow":
            follow = db.session.query(User, FollowerModel, UserProfile) \
                .join(FollowerModel, FollowerModel.uid == User.id) \
                .join(UserProfile, UserProfile.user_id == FollowerModel.fid) \
                .filter(User.id == current_user.id) \
                .with_entities(UserProfile.user_id, UserProfile.nickname, UserProfile.head_url) \
                .all()
            _key = ["user_id", "user_nickname", "user_head_url"]
            data = [dict(zip(_key, start)) for start in follow]
            return success_response(data=data)
        elif type == "star":
            star = db.session.query(User, FollowerModel, UserProfile) \
                .join(FollowerModel, FollowerModel.fid == User.id) \
                .join(UserProfile, UserProfile.user_id == FollowerModel.uid) \
                .filter(User.id == current_user.id) \
                .with_entities(UserProfile.user_id, UserProfile.nickname, UserProfile.head_url) \
                .all()

            _key = ["user_id", "user_nickname", "user_head_url"]
            data = [dict(zip(_key, item)) for item in star]

            return success_response(data=data)
        else:
            return raise_400_response()
