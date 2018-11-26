# -*- coding: utf-8 -*-
from flask_restful import reqparse

from albumy.common.restful import RestfulBase
from albumy.utils.verification_code import random_int_code


class UserRegister(RestfulBase):
    # todo 
    def _get_verification_code(self):
        _code = random_int_code()
        return
    def post(self):
        req = reqparse.RequestParser()
        req.add_argument("process", choices=["verification_code", "check_verification"], required=True,
                         location=["json"])
        args = req.parse_args()

        return args
