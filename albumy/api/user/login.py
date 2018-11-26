# -*- coding: utf-8 -*-
from flask_restful import reqparse

from albumy.common.restful import RestfulBase, success_resp


class UserLogin(RestfulBase):
    def post(self):
        req = reqparse.RequestParser()
        req.add_argument("test")
        req.add_argument("hello",)
        args = req.parse_args()
        print(args)

        return success_resp()