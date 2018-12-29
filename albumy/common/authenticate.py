# # -*- coding: utf-8 -*-
from flask import current_app, request, g
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from sqlalchemy import or_

from albumy.constant import USER_ACTIVE
from albumy.models import User


def get_user_from_auth_token(token, model):
    """
    根据认证的token 找出对应model中的用户
    :param token: token
    :param model:
    :return: 用户，如果解析失败、出现错误等 返回None
    """
    s = Serializer(current_app.config["SECRET_KEY"])
    try:
        token = s.loads(token)
    except Exception:
        return None
    user_id = token.get("id", "")
    if not user_id:
        return None
    user = model.get_by_id(user_id)
    if not user:
        return None
    return user


class BaseAuth(object):
    _model = None

    def __init__(self):
        self.auth = HTTPBasicAuth()
        self.auth.verify_password(self._verify_password)

    def _verify_password(self, username_or_token, password):

        # token 登录
        token = request.values.get("token", "")
        if not token and username_or_token and not password:
            token = username_or_token
        if token:
            user = get_user_from_auth_token(token, self._model)
            if user and user.active == USER_ACTIVE:
                g.current_user = user
                return True

        # 如果密码登录
        if username_or_token and password:
            if hasattr(self._model, "mobile") and hasattr(self._model, "email"):
                user = self._model.query.filter(or_(
                    self._model.mobile == str(username_or_token),
                    self._model.email == str(username_or_token))
                ).first()
                if user and user.active == USER_ACTIVE:
                    if not user.check_password(password):
                        return False
                    g.current_user = user
                    return True
        return False


class AlbumyAuth(BaseAuth):
    _model = User

    def __init__(self):
        super(AlbumyAuth, self).__init__()
