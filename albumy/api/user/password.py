# -*-coding:utf-8-*-
from flask import g, current_app
from flask_restful import reqparse

from albumy.common.restful import RestfulBase, success_response, raise_400_response, raise_404_response
from albumy.extensions import login_required
from albumy.models import User
from albumy.utils.tokens import generate_confirm_token, parse_confirm_token
from albumy.utils.validate import validate_password, validate_email_or_mobile
from albumy.celery_tasks import send_email


class Password(RestfulBase):
    """
    逻辑说明：密码的修改主要分为主动修改密码、忘记密码被动修改两类
    主动修改是在用户登录的前提下，进行的
    忘记密码是在用户未登录的情况下可进行的，给用户一个url（具有时限、一次性）
    ，在url中修改
    """

    @login_required
    def __modify_password(self):
        req = reqparse.RequestParser()
        req.add_argument("old_password", type=validate_password, default="", location="form")
        req.add_argument("new_password", type=validate_password, default="", location="form")
        args = req.parse_args()
        user = g.current_user
        if not user.check_password(args["old_password"]):
            return raise_400_response(message="密码错误")
        fields = dict(
            password=args["new_password"]

        )
        user.update(**fields)
        return success_response()

    def __forget_password(self, token):
        data = parse_confirm_token(token)
        user_id = data.get("confirm")
        if (not user_id) and data.get("msg"):
            return success_response(message="连接过时")

        if user_id:
            req = reqparse.RequestParser()
            req.add_argument("password", type=validate_password, default="", location="form")
            req.add_argument("repeat_password", type=validate_password, default="", location="form")
            args = req.parse_args()
            if args["password"] != args["repeat_password"]:
                return success_response(status_code=0, message="两次密码不一致")
            user = User.get_by_id(user_id)

            fields = {
                'password': args["password"]
            }
            user.update(**fields)
            return success_response(message="密码重置成功")

    def post(self, token=None):
        if not token:
            return self.__modify_password()
        return self.__forget_password(token)

    def get(self):
        req = reqparse.RequestParser()
        req.add_argument("email_or_mobile", type=validate_email_or_mobile, default="", location="form")
        args = req.parse_args()
        email_or_mobile = args.get("email_or_mobile")
        # 如果输入的是手机，则找到他的邮箱
        if email_or_mobile.isnumeric():
            _user = User.query.filter_by(mobile=email_or_mobile).first()

        else:
            _user = User.query.filter_by(email=email_or_mobile).first()
        if not _user:
            return raise_404_response(message=u"此账号未注册")
        token = generate_confirm_token(_user.id).decode("utf-8")
        try:
            send_email.delay("RESET_PASSWORD", _user.email,
                             body="{}/api/user/password/{}".format(current_app.config["DOMAIN"], token))
        except Exception as e:
            print(e)
        data = {
            "url": "{}/api/user/password/{}".format(current_app.config["DOMAIN"], token)
        }
        return success_response(data=data)
