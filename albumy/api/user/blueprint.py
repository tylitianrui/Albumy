# -*- coding: utf-8 -*-


from flask import Blueprint
from flask_restful import Api

from albumy.api.user.login import UserLogin
from albumy.api.user.user import User, UserTest

user_blueprint = Blueprint("user", __name__, url_prefix="/api")
# decorators=[csrf_protect.exempt]
user_api = Api(user_blueprint,prefix="/user",
               default_mediatype="application/json; charset=utf-8")

user_api.add_resource(UserLogin,"/login")
user_api.add_resource(User,"/user","/user/<token>")
user_api.add_resource(UserTest,"/user/test")
