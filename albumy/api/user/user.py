# -*- coding: utf-8 -*-
from flask_restful import reqparse

from albumy.celery_tasks import send_email
from albumy.common.restful import RestfulBase, success_response, raise_400_response

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

        return success_response()
    # @varify_code

    def post(self):
        """只有正确的输入验证码，此进行注册"""
        req = reqparse.RequestParser()
        req.add_argument("type", choices=["mobile", "email"], required=True, location=["json"])
        req.add_argument("mobile", type=validate_mobile, default="", location=["json"])
        req.add_argument("email", type=validate_email, default="", location=["json"])
        req.add_argument("password", type=validate_password, default="", location=["json"])
        req.add_argument("password_repeat", type=validate_password, default="", location=["json"])
        req.add_argument("user_name", type=validate_username, default="", location=["json"])
        req.add_argument("user_no", type=int, default=1000, location=["json"])
        args = req.parse_args()
        # 手机注册
        if args["type"] == "mobile":
            if not args["mobile"]:
                return
            else:
                if args["password"] != args["password_repeat"]:
                    return
                if Usermodel.is_exist({"mobile": args["mobile"]}):
                    return
                code = random_int_code()
                return success_response(data=code)

                # 　发送验证码
        # 邮箱注册
        if args["type"] == "email":
            if not args["email"]:
                return raise_400_response(message=u"参数错误")

            else:
                if args["password"] != args["password_repeat"]:
                    return raise_400_response(message=u'两次密码不一致')
                # 　　判断是否已经注册
                if Usermodel.is_exist(email=args["email"]):
                    return raise_400_response(message=u"此邮箱已经注册")

                _fields = {
                    "email": args["email"],
                    "mobile": args["mobile"],
                    "active": False,
                    "user_name": args["user_name"] if args["user_name"] else gen_user_name(),
                    "password": args["password"]
                }

                _user = Usermodel.create(**_fields)

                t = generate_confirm_token(_user.id).decode("utf-8")
                try:
                    User.cache_redis.setex("register_token_user_id_{}".format(_user.id), time=60, value=t)
                except Exception as err:
                    print(err)
                    return "err redis"
                # try:
                #     send_email.delay("REGISTER_ACTIVATE", args["email"],
                #                  body="http://localhost:5000/api/user/user/{}".format(t))
                # except:
                #     return "send"

                return success_response(data="http://localhost:5000/api/user/user/{}".format(t))


class UserTest(RestfulBase):
    def get(self):
        return {
            "test": "ok"
        }
