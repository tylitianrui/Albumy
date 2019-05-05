# -*- coding: utf-8 -*-
from flask_restful import Resource
from werkzeug.exceptions import HTTPException

from albumy.common.excptions import AlbBaseException


class RestfulBase(Resource):

    def pre_request(func):
        """
        请求的执行前，执行
        :return:
        """

        def method(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except AlbBaseException as err:
                return err.__str__(), err.http_status_code
            except HTTPException as err:
                return err.get_response()

        return method

    method_decorators = [pre_request]


def _resp(status_code=200, message="ok", data=None):
    """
    :param message:
    :param status_code:
    :param data:
    :return:
    """
    result = {
        "code": status_code,
        "message": message
    }
    if data:
        result["data"] = data
    return result, status_code


def success_response(status_code=200, message="ok", data=None):
    return _resp(status_code, message, data)


def raise_400_response(status_code=400, message=u'请求参数错误', data=None):
    return _resp(status_code, message, data)


def raise_401_response(status_code=401, message=u'请求未授权', data=None):
    return _resp(status_code, message, data)
    # raise UnauthorizedException(code=code, message=message, data=data)


def raise_403_response(status_code=403, message=u'请求被拒绝', data=None):
    return _resp(status_code, message, data)
    # raise ForbiddenException(code=code, message=message, data=data)


def raise_404_response(status_code=404, message=u'未找到', data=None):
    return _resp(status_code, message, data)
    # raise NotFoundException(code=code, message=message, data=data)
