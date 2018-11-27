# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/11/27

import time


def get_timestamp():
    """
    时间戳，基于毫秒
    :return:
    """
    _time = int(time.time()*1000)
    return _time


if __name__ == '__main__':
    print(get_timestamp())
