import asyncio

from cache import RedisCache
from category import AmazonCategory
from config import REDIS_CONN, WORK_END, WORK_SECONDS, WORK_START
from stores.amazon import Amazon
from stores.base import Base


async def process_store(store: Base, redis: RedisCache):
    products = await store.exec()
    for index, product in enumerate(products):
        key = f"{store.name()}:{store.departament}:{index}"
        await redis.add(key, product.dict(), WORK_SECONDS)


async def ingestion(stores: list[Base]):
    redis = RedisCache(REDIS_CONN)
    await asyncio.gather(*(process_store(store, redis) for store in stores))
    await asyncio.Event().wait()


beleza = Amazon(AmazonCategory.BELEZA.value, 100, 10)
games = Amazon(AmazonCategory.GAMES_E_CONSOLES.value, 100, 10)
eletro = Amazon(AmazonCategory.ELETRODOMESTICOS.value, 100, 10)
tech = Amazon(AmazonCategory.ELETRONICOS_E_TECNOLOGIA.value, 100, 10)
pet = Amazon(AmazonCategory.PET_SHOP.value, 100, 10)

asyncio.run(ingestion([beleza, games, eletro, tech, pet]))
