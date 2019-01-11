# -*-coding:utf-8-*-
import base64


def create_basic_auth(user, passwd):
    """
    创建basic auth的token
    :param user:
    :param passwd:
    :return:
    """
    content = "{}:{}".format(user, passwd)
    auth_token = base64.b64encode(content.encode("ascii"))
    return auth_token.decode("ascii")


def parse_basic_auth(auth_token):
    """
    解析basic auth，获取
    :param auth_token:
    :return:
    """
    content = base64.b64decode(auth_token).decode("ascii")
    user, *_, passwd = content.split(":")
    return user, passwd


if __name__ == '__main__':
    user = ""
    pwd = ""
    print(create_basic_auth(user=user, passwd=pwd))
    print(parse_basic_auth("dGU6"))

