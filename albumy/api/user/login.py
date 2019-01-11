# -*- coding: utf-8 -*-
from datetime import datetime

from flask import g, current_app

from albumy.common.restful import RestfulBase, success_response
from albumy.extensions import varify_password


class UserLogin(RestfulBase):
    @varify_password
    def post(self):
        user = g.current_user
        login_time = datetime.now()
        fields = {
            "last_login":login_time
        }
        user.update(**fields)
        token = user.generate_auth_token(current_app.config["AUTH_TOKEN_EXPIRED_TIME"])
        data = {
            "user_id": user.id,
            "user_name": user.user_name,
            "token": token
        }
        return success_response(data)
