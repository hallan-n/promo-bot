import asyncio
from datetime import datetime

from api.telegram import Telegram
from services.cache import RedisCache
from services.logger import logger
from settings import settings
from webdriver.browser import BrowserManager
from webdriver.whatsapp import Whatsapp

REDIS_CONN = "redis://localhost:6379"
redis = RedisCache(REDIS_CONN)


MESSAGE_DELAY = 1  # delay entre grupos de mesma rodada
ROUND_DELAY = 180  # delay após enviar para todas as categorias/grupos
CHECK_INTERVAL = 10  # espera se não tiver produtos
START_HOUR = 1
END_HOUR = 18


def in_working_hours():
    now = datetime.now().hour
    return START_HOUR <= now < END_HOUR


async def wait_until_working_hours():
    while not in_working_hours:
        logger.info("⏳ Aguardando início do expediente...")
        await asyncio.sleep(60)


async def ingestion():
    last_ingestion = await redis.redis.get("last_ingestion")
    if (
        last_ingestion
        and datetime.fromisoformat(last_ingestion).date() == datetime.now().date()
    ):
        logger.info("✅ ingestão já realizada hoje")
        return

    logger.info("📥 Iniciando ingestão...")
    await redis.clear()

    for key, value in settings.items():
        stores = value["stores"]
        for index_1, store in enumerate(stores):
            products = await store.exec()
            for index_2, product in enumerate(products):
                redis_key = f"{key}:{index_1}-{index_2}"
                await redis.add(redis_key, product, 86400)

    logger.info("✅ Ingestão finalizada")
    await redis.redis.set("last_ingestion", str(datetime.now()))


async def send_products_round_robin(whatsapp: Whatsapp, telegram: Telegram):
    sem = asyncio.Semaphore(1)
    empty_groups_logged = set()

    while True:
        if not in_working_hours():
            logger.info("🛑 Expediente encerrado")
            return

        sent_any = False

        for key, value in settings.items():
            whatsapp_groups = value["groups"]["whatsapp"]
            telegram_groups = value["groups"]["telegram"]

            items = await redis.get_products_by_prefix_with_keys(key)
            if not items:
                continue

            key_item, product = items[0]

            for group in whatsapp_groups:
                async with sem:
                    await whatsapp.send_message(group.chat_id, product)
                    await redis.delete(key_item)
                    logger.info(
                        f"✅ Produto '{product}' enviado para WhatsApp: {group.chat_id}"
                    )
                    sent_any = True
                    await asyncio.sleep(MESSAGE_DELAY)

            for group in telegram_groups:
                async with sem:
                    await telegram.send_message(group.chat_id, product)
                    await redis.delete(key_item)
                    logger.info(
                        f"✅ Produto '{product}' enviado para Telegram: {group.chat_id}"
                    )
                    sent_any = True
                    await asyncio.sleep(MESSAGE_DELAY)

        if sent_any:
            logger.info(
                f"⏱ Rodada completa de envios concluída. Aguardando {ROUND_DELAY}s..."
            )
            await asyncio.sleep(ROUND_DELAY)
        else:
            await asyncio.sleep(CHECK_INTERVAL)


async def main():
    await wait_until_working_hours()

    logger.info("🚀 Iniciando WhatsApp...")

    whatsapp = Whatsapp()

    telegram = Telegram()

    await whatsapp.start()

    await ingestion()

    logger.info("📤 Iniciando worker de envio...")

    await send_products_round_robin(whatsapp, telegram)

    logger.info("🏁 Expediente finalizado")

    await BrowserManager.close()


if __name__ == "__main__":
    asyncio.run(main())
