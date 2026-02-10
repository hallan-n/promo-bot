import asyncio

from services.cache import RedisCache
from category import AmazonDepartament
from config import REDIS_CONN, WORK_SECONDS
from webdriver.amazon import Amazon
from webdriver.base import Base


async def process_store(store: Base, redis: RedisCache):
    products = await store.exec()
    for index, product in enumerate(products):
        key = f"{store.name()}:{store.departament_name}:{index}"
        await redis.add(key, product.dict(), WORK_SECONDS)


async def ingestion(stores: list[Base]):
    redis = RedisCache(REDIS_CONN)
    await asyncio.gather(*(process_store(store, redis) for store in stores))
    await asyncio.Event().wait()


casa = Amazon(AmazonDepartament.LIVROS.value, AmazonDepartament.LIVROS.name, 10, 0)

asyncio.run(ingestion([casa]))
