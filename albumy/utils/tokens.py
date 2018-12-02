# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/11/20
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature


def generate_confirm_token(obj, expiration_in=60):
    s = Serializer(current_app.config['SECRET_KEY'], expiration_in)
    return s.dumps({'confirm': obj})


def parse_confirm_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        _confirm = s.loads(token)  # 如果token验证不成功，会报两种错误
    except SignatureExpired:  # 时间过期
        return dict(msg = 'valid token, but expired')
    except BadSignature:  # token错误
        return dict( msg = 'Invalid token')
    return _confirm

