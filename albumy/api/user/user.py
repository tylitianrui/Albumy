# -*- coding: utf-8 -*-
from flask_mail import Message
from flask_restful import reqparse

from albumy.common.restful import RestfulBase, success_resp
from albumy.extensions import mail
from albumy.models import User as Usermodel
from albumy.utils.email import send_mail
from albumy.utils.gen_default import gen_user_name
from albumy.utils.validate import validate_password, validate_email, validate_mobile, validate_username
from albumy.utils.verification_code import random_int_code


class User(RestfulBase):

    def post(self):
        req = reqparse.RequestParser()
        req.add_argument("type", choices=["mobile", "email"], required=True, location=["json"])
        req.add_argument("mobile", type=validate_mobile, default="", location=["json"])
        req.add_argument("email", type=validate_email, default="", location=["json"])
        req.add_argument("password", type=validate_password, default="", location=["json"])
        req.add_argument("password_repeat", type=validate_password, default="", location=["json"])
        req.add_argument("user_name", type=validate_username, default="", location=["json"])
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
                    #
                    "user_no": 1,
                    "email": args["email"],
                    "mobile": args["mobile"],
                    "active": False,
                    "user_name": args["user_name"] if args["user_name"] else gen_user_name(),
                    "password": args["password"]
                }

                code = random_int_code()

                # 发送邮件激活
                msg = Message(subject="Hello World!",
                              sender="tyltr_test@126.com",
                              recipients=["913173651@qq.com"])
                mail.send(msg)
                return success_resp(data=code)

        return args
