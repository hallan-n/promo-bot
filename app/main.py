import asyncio
from datetime import datetime

from groups import groups
from services.cache import RedisCache
from webdriver.base import Base
from webdriver.whatsapp import Whatsapp

MESSAGE_DELAY = 60
REDIS_CONN = "redis://localhost:6379"
START_HOUR = 11
END_HOUR = 18
CHECK_INTERVAL = 5

redis = RedisCache(REDIS_CONN)


def in_working_hours():
    now = datetime.now().hour
    return START_HOUR <= now < END_HOUR


async def wait_until_working_hours():
    while not in_working_hours():
        print("⏳ Aguardando início do expediente...")
        await asyncio.sleep(60)


async def _ingestion(group_name_id: str, stores: list[Base], sem: asyncio.Semaphore):
    async def process_store(store: Base):
        async with sem:
            products = await store.exec()
            for index, product in enumerate(products):
                key = f"{group_name_id}:{store.departament_code}:{index}"
                await redis.add(key, product)

    await asyncio.gather(*(process_store(store) for store in stores))


async def ingestion():
    print("📥 Iniciando ingestão...")
    await redis.clear()

    ingestion_sem = asyncio.Semaphore(4)

    tasks = [
        _ingestion(group["name_id"], group["stores"], ingestion_sem) for group in groups
    ]

    await asyncio.gather(*tasks)
    print("✅ Ingestão finalizada")


async def send_products_group(
    wpp: Whatsapp, group_name: str, name_id: str, sem: asyncio.Semaphore
):
    while True:
        if not in_working_hours():
            print(f"🛑 Expediente encerrado para grupo {group_name}")
            return

        items = await redis.get_products_by_group_name_id_with_keys(name_id)

        if not items:
            await asyncio.sleep(CHECK_INTERVAL)
            continue

        for key, product in items:
            if not in_working_hours():
                print(f"🛑 Expediente encerrado durante envio ({group_name})")
                return

            async with sem:
                await wpp.send_message(group_name, product)
                await redis.delete(key)
                await asyncio.sleep(MESSAGE_DELAY)


async def main():
    await wait_until_working_hours()

    print("🚀 Iniciando WhatsApp...")
    wpp = Whatsapp()
    await wpp.start()

    await ingestion()

    print("📤 Iniciando worker de envio...")

    sem = asyncio.Semaphore(1)

    send_tasks = [
        send_products_group(wpp, group["name"], group["name_id"], sem)
        for group in groups
    ]

    await asyncio.gather(*send_tasks)

    print("🏁 Expediente finalizado")


if __name__ == "__main__":
    asyncio.run(main())
