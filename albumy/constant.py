# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/11/25

# regex
import re

MOBILE_PATTERN = re.compile("1[356789]\d{9}")  # 手机
EMAIL_PATTERN = re.compile("\w+@\w+\.\w+")  # 邮箱
USERNAME_PATTERN = re.compile("[\w\u4e00-\u9fa5]{6,16}")  # 用户名
PASSWORD_PATTERN = re.compile("\w{6,16}")  # 密码




STATIC_FILES = ["base.html"]

# 用户注册状态
USER_REGISTERED = 101  #                  用户已注册
USER_ACTIVE = 102      #                  用户账号已经激活

