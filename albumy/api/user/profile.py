# -*-coding:utf-8-*-
from flask import g
from flask_restful import reqparse

from albumy.common.restful import RestfulBase, success_response
from albumy.extensions import login_required
from albumy.models import UserProfile
from albumy.utils.validate import validate_password, validate_nickname, validate_age


class Profile(RestfulBase):
    @login_required
    def get(self):
        user = g.current_user
        user_profile = UserProfile.query.filter_by(user_id=user.id).first()
        data = {
            "user_id": user_profile.user_id,
            "nickname": user_profile.nickname,
            "age": user_profile.age,
            "head_url": user_profile.head_url,
            "gender": user_profile.gender
        }
        return success_response(data=data)

    @login_required
    def post(self):
        req = reqparse.RequestParser()
        req.add_argument("nickname", type=validate_nickname, default="", location="form")
        req.add_argument("age", type=validate_age, default=0, location="form")
        req.add_argument("gender", type=int, choices=[1, 2], default=0, location="form")
        args = req.parse_args()
        fields = {}
        user = g.current_user
        user_profile = UserProfile.query.filter_by(user_id=user.id).first()

        if args.age:
            fields["age"] = args.age
        if args.nickname:
            fields["nickname"] = args.nickname
        if args.gender:
            fields["gender"] = args.gender
        user_profile.update(**fields)
        return success_response()
