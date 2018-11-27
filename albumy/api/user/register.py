# -*- coding: utf-8 -*-
from flask_restful import reqparse

from albumy.common.restful import RestfulBase, success_resp
from albumy.models import User
from albumy.utils.email import send_mail
from albumy.utils.validate import validate_password, validate_email, validate_mobile
from albumy.utils.verification_code import random_int_code


class UserRegister(RestfulBase):

    def post(self):
        req = reqparse.RequestParser()

        req.add_argument("type", choices=["mobile", "email"], required=True, location=["json"])
        req.add_argument("mobile", type=validate_mobile, default="", location=["json"])
        req.add_argument("email", type=validate_email, default="", location=["json"])
        req.add_argument("password", type=validate_password, default="", location=["json"])
        req.add_argument("password_repeat", type=validate_password, default="", location=["json"])
        args = req.parse_args()
        if args["type"] == "mobile":
            if not args["mobile"]:
                return
            else:
                if args["password"] != args["password_repeat"]:
                    return
                if User.is_exist({"mobile": args["mobile"]}):
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
                if User.is_exist({"email": args["email"]}):
                    return
                code = random_int_code()





                # 发送邮件激活
                return success_resp(data=code)

        return args
