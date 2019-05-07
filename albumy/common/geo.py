# -*- coding: utf-8 -*-
import os
import re

import geoip2.database


class GeoIP(object):
    """ip 地理信息"""

    def __init__(self):
        #  GeoLite2-City.mmdb文件的目录
        geo_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/file/GeoLite2-City.mmdb")
        try:
            self.reader = geoip2.database.Reader(geo_file)
        except Exception:
            raise Exception("GeoLite2-City.mmdb 文件加载异常")
        else:
            # ip正则
            _ip_regex = r'(2(5[0-5]{1}|[0-4]\d{1})|[0-1]?\d{1,2})(\.(2(5[0-5]{1}|[0-4]\d{1})|[0-1]?\d{1,2})){3}'
            self.ip_regex = re.compile(_ip_regex)

            # 内网ip
            _local_ip_regex = "(^10\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[0-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[" \
                              "1-9]\d|[0-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[0-9])$)|" \
                              "(^172\.(1[6789]|2[0-9]|3[01])\.(1\d{2}|2[0-4]\d|25[" \
                              "0-5]|[1-9]\d|[0-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[0-9])$)|" \
                              "(^192\.168\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[0-9])\.(1\d{2}|2[0-4]\d|25[" \
                              "0-5]|[1-9]\d|[0-9])$)|127\.0\.0\.1"

            self.local_ip_regex = re.compile(_local_ip_regex)

    def verify_ip(self, ip):
        """
        检验ip是否合法，如果合法返回True，ip；否则返回False,None
        :param ip: ip str
        :return:
        """
        slices = ip.split(".")
        try:
            if len(slices) != 4:
                return False, None
            end_slice=slices[3]
            if int(end_slice)>255:
                return False, None
        except:
            return False, None
        ret = self.ip_regex.match(ip)
        if ret:

            return True, ret.group()
        return False, None

    def ip2country(self, ip):
        """
        获取此ip所在的国家或地区，如是内网ip，则返回LOCAL
        :param ip:
        :return:
        """
        flag, _ip = self.verify_ip(ip)
        if not flag:
            raise ValueError("{} does not appear to be an IPv4 or IPv6 address".format(ip))
        _local = self.local_ip_regex.match(_ip)
        if _local:
            return "LOCAL"
        resp = self.reader.city(_ip)
        return resp.country.iso_code



