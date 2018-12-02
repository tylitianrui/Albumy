# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/11/27
import string

from celery import current_app

from albumy.utils.time_utils import get_timestamp


def gen_user_name():
    """
    生成默认的用户名，需要保证每个用户名都不重复
    :return:
    """
    _time = get_timestamp()
    _user_name = "user_{}".format(zip10(_time))
    return _user_name


def zip10(num):
    """
    将10进制数压缩成62进制，为了减少字符
    :param num: 10进制数
    :return: 62进制 —> str
    """
    base = "".join([string.digits, string.ascii_lowercase, string.ascii_uppercase])
    if num < 62:
        return base[num]
    else:
        return zip10(num // 62) + zip10(num % 62)




if __name__ == '__main__':
    l = zip10(120)
    print(l)
    print(gen_user_name())
