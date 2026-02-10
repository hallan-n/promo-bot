import json

from redis.asyncio import Redis


class RedisCache:
    def __init__(self, url: str, ttl: int = 60):
        self.redis = Redis.from_url(url, decode_responses=True)
        self.ttl = ttl

    async def add(self, key: str, value: str, ttl: int | None = None):
        expire = ttl or self.ttl

        await self.redis.set(key, json.dumps(value), ex=expire)

    async def get(self, key: str):
        data = await self.redis.get(key)

        if data is None:
            return None

        return json.loads(data)

    async def delete(self, key: str):
        await self.redis.delete(key)

    async def clear(self):
        await self.redis.flushdb()
