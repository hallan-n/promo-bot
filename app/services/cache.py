import json

from redis.asyncio import Redis

from models import Product


class RedisCache:
    def __init__(self, url: str, ttl: int = 60):
        self.redis = Redis.from_url(url, decode_responses=True)
        self.ttl = ttl

    async def add(self, key: str, value: Product, ttl: int | None = None):
        expire = ttl or self.ttl

        await self.redis.set(key, json.dumps(value.dict()), ex=expire)

    async def get(self, key: str) -> Product:
        data = await self.redis.get(key)

        if data is None:
            return None

        return Product(**json.loads(data))

    async def delete(self, key: str):
        await self.redis.delete(key)

    async def clear(self):
        await self.redis.flushdb()

    async def get_products_by_group_name_id(self, name_id: str) -> list[Product]:

        prefix = f"{name_id}:"
        keys = await self.redis.keys(f"{prefix}*")
        products = []

        for key in keys:
            data = await self.get(key)
            if data:
                products.append(data)

        return products
    

    async def get_products_by_group_name_id_with_keys(self, name_id: str) -> list[Product]:
        prefix = f"{name_id}:"
        keys = await self.redis.keys(f"{prefix}*")
        products = []

        for key in keys:
            data = await self.get(key)
            if data:
                products.append((key, data))

        return products
