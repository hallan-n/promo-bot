from redis.asyncio import Redis
import json
from contextlib import asynccontextmanager


@asynccontextmanager
async def get_redis():
    redis = Redis(host="localhost", port=6379, decode_responses=True)
    try:
        yield redis
    finally:
        await redis.aclose()

async def add(key: str, value: dict, ttl: int = None):
    async with get_redis() as redis:
        return await redis.set(key, json.dumps(value), ex=ttl)

async def get(key: str):
    async with get_redis() as redis:
        value = await redis.get(key)
        return json.loads(value)

async def get_all():
    async with get_redis() as redis:
        keys = await redis.keys("*")
        result = {}
        for key in keys:
            value = await redis.get(key)
            result[key] = json.loads(value)
        return result
