# -*- coding: utf-8 -*-
from flask_httpauth import HTTPBasicAuth


class BaseAuth(object):
    _model = None

    def __int__(self):
        self.auth = HTTPBasicAuth()
        self.auth.verify_password(self._verify_password)

    def _verify_password(self, mobile_or_token):
        pass


class AlbumyAuth(BaseAuth):
    def __int__(self):
        super(AlbumyAuth, self).__int__()
