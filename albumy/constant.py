# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/11/25

# regex
import re

MOBILE_PATTERN = re.compile("1[356789]\d{9}")  # 手机
EMAIL_PATTERN = re.compile("\w+@\w+\.\w+")  # 邮箱
USERNAME_PATTERN = re.compile("[\w\u4e00-\u9fa5]{6,16}")  # 用户名
PASSWORD_PATTERN = re.compile("\w{6,16}")  # 密码

# email topic
EMAIL_TOPIC = {
    "REGISTER_ACTIVATE": {
        "subject":"激活账号",
        "body":"激活账号：url {}".format(1),
        # "resource":"https://img-blog.csdnimg.cn/20181104102458943.png",
        "resource":"/Users/tyltr/mySpace/Albumy/Albumy/albumy/static/image/attachment_test_jpg.jpg",



    }
}

STATIC_FILES = ["base.html"]

# 用户注册状态
USER_REGISTERED = 101  # 用户已注册
USER_ACTIVE = 102  # 用户账号已经激活
