# -*-coding:utf-8-*-
try:
    import redis
except ImportError:
    redis = None


class RedisClient(object):
    def __init__(self, app=None, strict=True, redis_config_name='CACHE_REDIS_URL', **kwargs):
        self._redis_client = None
        self.provider_class = redis.StrictRedis if strict else redis.Redis
        self.provider_kwargs = kwargs
        self.redis_config_name = redis_config_name

        if app is not None:
            self.init_app(app)

    def init_app(self, app, **kwargs):
        redis_url = app.config.get(
            self.redis_config_name,
            'redis://localhost:6379/0'
        )
        self.provider_kwargs.update(kwargs)
        self._redis_client = self.provider_class.from_url(
            redis_url, decode_responses=True, **self.provider_kwargs)

    def __getattr__(self, name):
        return getattr(self._redis_client, name)

    def __getitem__(self, name):
        return self._redis_client[name]

    def __setitem__(self, name, value):
        self._redis_client[name] = value

    def __delitem__(self, name):
        del self._redis_client[name]
