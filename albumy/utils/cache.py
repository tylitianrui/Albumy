# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/12/2

from redis import ConnectionPool, StrictRedis


def get_cache_redis(redis_url):
    """
    创建redis的缓存
    :param redis_url:
    :return:
    """
    pool = ConnectionPool.from_url(redis_url)
    redis = StrictRedis(connection_pool=pool)
    return redis

