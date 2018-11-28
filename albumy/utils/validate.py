# -*- coding: utf-8 -*-
import re

from albumy.constant import MOBILE_PATTERN, EMAIL_PATTERN, USERNAME_PATTERN, PASSWORD_PATTERN


def validate_mobile(mobile):
    ret = re.match(MOBILE_PATTERN, mobile)
    if ret:
        _mobile = ret.group()
        return _mobile
    return validate_fail(mobile)


def validate_email(email):
    ret = re.match(EMAIL_PATTERN, email)
    if ret:
        _mobile = ret.group()
        return _mobile
    return validate_fail(email)


def validate_username(username):
    ret = re.match(USERNAME_PATTERN, username)
    if ret:
        _username = ret.group()
        return _username
    msg = "用户名为6-16位中文、英文、数字、下划线"
    return validate_fail(username, msg)


def validate_password(password):
    ret = re.match(PASSWORD_PATTERN, password)
    if ret:
        _password = ret.group()
        return _password
    msg = "密码为6-16位英文、数字、下划线"
    return validate_fail(password, msg)


def validate_fail(field, msg=""):
    _msg = "invalid literal,input:{}.".format(field)
    if msg:
        _msg += msg
    raise Exception(_msg)
