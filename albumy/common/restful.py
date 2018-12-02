# -*- coding: utf-8 -*-
from flask_restful import Resource

from albumy.common.excptions import AlbBaseException, BadRequestException, UnauthorizedException, ForbiddenException, \
    NotFoundException
from albumy.settings import BaseConfig
from albumy.utils.cache import get_cache_redis


class RestfulBase(Resource):


    cache_redis =get_cache_redis(BaseConfig.get("CACHE_REDIS_URL"))


def success_resp( status_code=200, message="message",data=None):
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


def raise_error_response(error_code, message='error', data=None):
    raise AlbBaseException(error_code, message, data)


def raise_400_response(code=400, message=u'请求参数错误', data=None):
    raise BadRequestException(code=code, message=message, data=data)


def raise_401_response(code=401, message=u'请求未授权', data=None):
    raise UnauthorizedException(code=code, message=message, data=data)


def raise_403_response(code=403, message=u'请求被拒绝', data=None):
    raise ForbiddenException(code=code, message=message, data=data)


def raise_404_response(code=404, message=u'未找到', data=None):
    raise NotFoundException(code=code, message=message, data=data)



