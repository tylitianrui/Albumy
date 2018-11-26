# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/11/25
from werkzeug.routing import BaseConverter


class AlbumyBaseConverter(BaseConverter):
    def get_converter_name(self):
        raise NotImplementedError


class RegexConverter(AlbumyBaseConverter):
    """转换器"""

    def __init__(self, url_map, regex):
        super(RegexConverter, self).__init__(url_map)
        self.regex = regex

    def get_converter_name(self):
        return "RegexConverter"
