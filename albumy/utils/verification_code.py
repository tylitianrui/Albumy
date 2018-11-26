# -*- coding: utf-8 -*-
import random


def random_int_code(num=6):
    """
    随机生成num位的随机数
    :param num:
    :return:
    """
    _code = random.randint(10 ** (num - 1), 10 ** num - 1)
    return "{}".format(_code)


