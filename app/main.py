import asyncio

from services.cache import RedisCache
from category import AmazonDepartament
from consts import REDIS_CONN, WORK_SECONDS
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


groups = [
    {
        "name": "LOBÃO CASA 1",
        "products": [
            Amazon(AmazonDepartament.CASA.value, AmazonDepartament.CASA.name, 30, 0),
            Amazon(AmazonDepartament.ELETRODOMESTICOS.value, AmazonDepartament.ELETRODOMESTICOS.name, 30, 0),
            Amazon(AmazonDepartament.COZINHA.value, AmazonDepartament.COZINHA.name, 30, 0)
        ]
    }
]

