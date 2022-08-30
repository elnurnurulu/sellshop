import redis

class RedisConfig:
    REDIS_BROKER_URL = 'redis://localhost:6379'
    CHANNEL_NAME = "events"

    @property
    def client(self):
        return redis.Redis.from_url(self.REDIS_BROKER_URL)


class EmailConfig:
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'rustamakifli2003@gmail.com'
    EMAIL_HOST_PASSWORD = 'aprmqfrghbkxxpnq'
    EMAIL_PORT = 465
    EMAIL_USE_TLS = True