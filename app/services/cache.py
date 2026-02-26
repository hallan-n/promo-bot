import json

from models import Product
from redis.asyncio import Redis
import random


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

    async def get_random_products_with_key(self, prefix: str) -> list[tuple[str, Product]]:
        prefix = f"{prefix}:"
        keys: list[str] = []

        async for key in self.redis.scan_iter(match=f"{prefix}*"):
            keys.append(key)

        if not keys:
            return []

        random.shuffle(keys)

        result: list[tuple[str, Product]] = []
        for key in keys:
            product = await self.get(key)
            if product:
                result.append((key, product))

        return result

    async def get_random_products(self, prefix: str) -> list[Product]:
        prefix = f"{prefix}:"
        keys: list[str] = []

        async for key in self.redis.scan_iter(match=f"{prefix}*"):
            keys.append(key)

        if not keys:
            return []

        random.shuffle(keys)

        products: list[Product] = []
        for key in keys:
            product = await self.get(key)
            if product:
                products.append(product)

        return products

    async def get_products_by_prefix(self, prefix: str) -> list[Product]:
        prefix = f"{prefix}:"
        keys = await self.redis.keys(f"{prefix}*")
        products = []

        for key in keys:
            data = await self.get(key)
            if data:
                products.append(data)

        return products

    async def get_products_by_prefix_with_keys(
        self, prefix: str
    ) -> list[tuple[str, Product]]:
        prefix = f"{prefix}:"
        keys = await self.redis.keys(f"{prefix}*")
        products = []

        for key in keys:
            data = await self.get(key)
            if data:
                products.append((key, data))

        return products
