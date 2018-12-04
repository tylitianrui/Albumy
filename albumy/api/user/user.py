# -*- coding: utf-8 -*-
from flask_restful import reqparse

from albumy.celery_tasks import send_email
from albumy.common.restful import RestfulBase, success_resp

from albumy.models import User as Usermodel

from albumy.utils.gen_default import gen_user_name
from albumy.utils.tokens import generate_confirm_token, parse_confirm_token
from albumy.utils.validate import validate_password, validate_email, validate_mobile, validate_username
from albumy.utils.verification_code import random_int_code




class User(RestfulBase):


    def get(self, token):
        if not token:
            return
        data = parse_confirm_token(token)
        confirm_id = data.get("confirm")
        if not confirm_id:
            return
        _id = User.cache_redis.get("register_token_user_id_{}".format(confirm_id))
        if not _id:
            return
        user = Usermodel.get_by_id(confirm_id)
        activate = {"active": True}
        user.update(**activate)
        User.cache_redis.delete("register_token_user_id_{}".format(confirm_id))

        return success_resp()

    def post(self):
        req = reqparse.RequestParser()
        req.add_argument("type", choices=["mobile", "email"], required=True, location=["json"])
        req.add_argument("mobile", type=validate_mobile, default="", location=["json"])
        req.add_argument("email", type=validate_email, default="", location=["json"])
        req.add_argument("password", type=validate_password, default="", location=["json"])
        req.add_argument("password_repeat", type=validate_password, default="", location=["json"])
        req.add_argument("user_name", type=validate_username, default="", location=["json"])
        req.add_argument("user_no", type=int, default=1000, location=["json"])
        args = req.parse_args()
        if args["type"] == "mobile":
            if not args["mobile"]:
                return
            else:
                if args["password"] != args["password_repeat"]:
                    return
                if Usermodel.is_exist({"mobile": args["mobile"]}):
                    return
                code = random_int_code()
                return success_resp(data=code)

                # 　发送验证码

        if args["type"] == "email":
            if not args["email"]:
                return
            else:
                if args["password"] != args["password_repeat"]:
                    return
                # 　　判断是否已经注册
                if Usermodel.is_exist(email=args["email"]):
                    return

                _fields = {
                    "email": args["email"],
                    "mobile": args["mobile"],
                    "active": False,
                    "user_name": args["user_name"] if args["user_name"] else gen_user_name(),
                    "password": args["password"]
                }

                _user = Usermodel.create(**_fields)

                t = generate_confirm_token(_user.id).decode("utf-8")

                User.cache_redis.setex("register_token_user_id_{}".format(_user.id), time=60, value=t)

                send_email.delay("REGISTER_ACTIVATE", args["email"],
                                 body="http://localhost:5000/api/user/user/{}".format(t))

                return success_resp()



class UserTest(RestfulBase):
    def get(self):
        return {
            "test":"ok"
        }