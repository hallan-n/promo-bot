import asyncio
from datetime import datetime

from groups import groups
from services.cache import RedisCache
from services.logger import logger
from webdriver.whatsapp import Whatsapp

MESSAGE_DELAY = 180
REDIS_CONN = "redis://localhost:6379"
START_HOUR = 11
END_HOUR = 18
CHECK_INTERVAL = 5

redis = RedisCache(REDIS_CONN)


def in_working_hours():
    now = datetime.now().hour
    return START_HOUR <= now < END_HOUR


async def wait_until_working_hours():
    while not in_working_hours:
        logger.info("⏳ Aguardando início do expediente...")
        await asyncio.sleep(60)


async def send_products_round_robin(wpp: Whatsapp):
    sem = asyncio.Semaphore(1)
    empty_groups_logged = set()  # evita spam de log

    while True:
        if not in_working_hours():
            logger.info("🛑 Expediente encerrado")
            return

        sent_any = False

        for group in groups:
            group_name = group["name"]
            name_id = group["name_id"]

            items = await redis.get_products_by_group_name_id_with_keys(name_id)

            if not items:
                if name_id not in empty_groups_logged:
                    logger.info(f"📭 Produtos do grupo {group_name} acabaram")
                    empty_groups_logged.add(name_id)
                continue

            # remove do controle se voltou a ter produtos
            empty_groups_logged.discard(name_id)

            key, product = items[0]

            async with sem:
                await wpp.send_message(group_name, product)
                await redis.delete(key)

                logger.info(f"✅ Enviado para {group_name}")
                sent_any = True

        if sent_any:
            logger.info(f"⏳ Aguardando {MESSAGE_DELAY}s para próxima rodada")
            await asyncio.sleep(MESSAGE_DELAY)
        else:
            await asyncio.sleep(CHECK_INTERVAL)


async def ingestion():
    last_ingestion = await redis.redis.get("last_ingestion")

    if last_ingestion and datetime.fromisoformat(last_ingestion).date() == datetime.now().date():
        logger.info("📥 ingestão já realizada hoje")
        return

    logger.info("📥 Iniciando ingestão...")
    await redis.clear()

    for i, group in enumerate(groups):
        for j, store in enumerate(group.get("stores")):
            products = await store.exec()
            logger.info(
                f"Processado {len(products)} produtos para Store {group['name']}"
            )
            for k, product in enumerate(products):
                key = f"{group['name_id']}:{i}-{j}-{k}"
                await redis.add(key, product, 86400)

    logger.info("✅ Ingestão finalizada")
    await redis.redis.set("last_ingestion", str(datetime.now()))


async def main():
    await wait_until_working_hours()

    logger.info("🚀 Iniciando WhatsApp...")
    wpp = Whatsapp()
    await wpp.start()

    await ingestion()

    logger.info("📤 Iniciando worker de envio...")

    await send_products_round_robin(wpp)

    logger.info("🏁 Expediente finalizado")


if __name__ == "__main__":
    asyncio.run(main())
