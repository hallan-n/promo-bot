import asyncio

from consts import MESSAGE_DELAY, REDIS_CONN, WORK_SECONDS
from services.cache import RedisCache
from webdriver.amazon import Amazon
from webdriver.base import Base
from webdriver.whatsapp import Whatsapp

redis = RedisCache(REDIS_CONN)


async def ingestion(group_name_id: str, stores: list[Base], sem: asyncio.Semaphore):
    async def process_store(store: Base):
        async with sem:
            products = await store.exec()
            for index, product in enumerate(products):
                key = f"{group_name_id}:{store.departament_code}:{index}"
                await redis.add(key, product, WORK_SECONDS)

    await asyncio.gather(*(process_store(store) for store in stores))


groups = [
    {
        "name": "RAPOSA KIDS 1",
        "name_id": "RAPOSA_KIDS_1",
        "stores": [
            Amazon(
                "Brinquedos e Jogos",
                20,
                15,
                "Brinquedos para Bebês e Crianças Pequenas",
            ),
            Amazon("Brinquedos e Jogos", 20, 15, "Esportes e Brincadeiras ao Ar Livre"),
            Amazon("Bebês", 30, 10),
        ],
    },
    {
        "name": "RAPOSA CASA 1",
        "name_id": "RAPOSA_CASA_1",
        "stores": [
            Amazon("Casa", 30, 15),
            Amazon("Cozinha", 30, 15),
            Amazon("Eletrodomésticos", 30, 10),
        ],
    },
    {
        "name": "RAPOSA BELEZA 1",
        "name_id": "RAPOSA_BELEZA_1",
        "stores": [
            Amazon("Beleza", 30, 15, "Cuidados com o Cabelo"),
            Amazon("Beleza", 30, 15, "Manicure e Pedicure"),
            Amazon("Beleza", 30, 15, "Maquiagem"),
            Amazon("Beleza", 30, 15, "Pele"),
            Amazon("Beleza", 30, 15, "Perfumes"),
            Amazon("Beleza", 30, 15, "Utensílios e Acessórios"),
        ],
    },
]


async def send_products_group(
    wpp: Whatsapp, group_name: str, name_id: str, sem: asyncio.Semaphore
):
    items = await redis.get_products_by_group_name_id_with_keys(name_id)
    for key, product in items:
        async with sem:
            await wpp.send_message(group_name, product)
            await redis.delete(key)
            await asyncio.sleep(MESSAGE_DELAY)


async def main():
    wpp = Whatsapp()
    await wpp.start()

    # Ingestão primeiro
    ingestion_sem = asyncio.Semaphore(4)  # até 4 stores simultâneos
    tasks = [
        ingestion(group["name_id"], group["stores"], ingestion_sem) for group in groups
    ]
    await asyncio.gather(*tasks)

    sem = asyncio.Semaphore(1)  # 1 produto por vez

    # Envio para cada grupo
    send_tasks = [
        send_products_group(wpp, group["name"], group["name_id"], sem)
        for group in groups
    ]
    await asyncio.gather(*send_tasks)

    await asyncio.Event().wait()


asyncio.run(main())
