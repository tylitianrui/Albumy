# -*-coding:utf-8-*-

from albumy.common.restful import RestfulBase, success_response


class Pong(RestfulBase):
    def get(self):
        return success_response(status_code=200, data="pong", message="ok")
