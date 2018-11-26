# -*- coding: utf-8 -*-
from flask_restful import Resource


class RestfulBase(Resource):
    pass


def success_resp(message="message", status_code=200, data=None):
    """

    :param message:
    :param status_code:
    :param data:
    :return:
    """
    result = {
        "code": 0,
        "message": message
    }
    if data:
        result["data"] = data
    return result, status_code
