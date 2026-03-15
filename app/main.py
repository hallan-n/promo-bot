import asyncio
from datetime import datetime
import json
import httpx
from services.api.telegram import Telegram
from consts import CHECK_INTERVAL, MESSAGE_DELAY, REDIS_CONN, ROUND_DELAY
from services.cache import RedisCache
from services.image_editor import save_stories
from services.logger import logger
from settings import settings
from utils import clear_dir, create_dir, in_working_hours, wait_until_working_hours
from services.webdriver.browser import BrowserManager
from services.webdriver.instagram import Instagram
from services.api.whatsapp import Whatsapp

redis = RedisCache(REDIS_CONN)


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
                if not product.original_price:
                    continue
                if not product.price_discount:
                    continue
                if not product.url:
                    continue
                if not product.thumbnail:
                    continue

                redis_key = f"{key}:{index_1}-{index_2}"
                await redis.add(redis_key, product, 86400)

    logger.info("✅ Ingestão finalizada")
    await redis.redis.set("last_ingestion", str(datetime.now()))

async def send_products_round_robin(
    whatsapp: Whatsapp | None, telegram: Telegram | None, instagram: Instagram | None
):
    sem = asyncio.Semaphore(1)

    while True:
        if not in_working_hours():
            logger.info("🛑 Expediente encerrado")
            return

        sent_any = False

        for key, value in settings.items():
            groups = value.get("groups", {})

            whatsapp_groups = groups.get("whatsapp", []) if whatsapp else []
            telegram_groups = groups.get("telegram", []) if telegram else []
            instagram_groups = groups.get("instagram", []) if instagram else []

            items = await redis.get_random_products_with_key(key)
            if not items:
                continue

            key_item, product = items[0]

            # WhatsApp
            if whatsapp and whatsapp_groups:
                for group in whatsapp_groups:
                    async with sem:
                        await whatsapp.send_message(group.chat_id, product)
                        await redis.delete(key_item)
                        logger.info(
                            f"✅ Produto '{product.name[:30]}...' enviado para WhatsApp: {group.name}"
                        )
                        sent_any = True
                        await asyncio.sleep(MESSAGE_DELAY)

            # Telegram
            if telegram and telegram_groups:
                for group in telegram_groups:
                    async with sem:
                        await telegram.send_message(group.chat_id, product)
                        await redis.delete(key_item)
                        logger.info(
                            f"✅ Produto '{product.name[:30]}...' enviado para Telegram: {group.name}"
                        )
                        sent_any = True
                        await asyncio.sleep(MESSAGE_DELAY)

            # Instagram
            if instagram and instagram_groups:
                for group in instagram_groups:
                    async with sem:
                        await instagram.send_message(key_item, product)
                        await redis.delete(key_item)
                        logger.info(
                            f"✅ Produto '{product.name[:30]}...' enviado para Instagram: {group.name}"
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

async def process_storie(client, key, product, sem, max_retries=3):
    async with sem:
        for attempt in range(1, max_retries + 1):
            try:
                response = await client.get(product.thumbnail)
                response.raise_for_status()

                if "image" not in response.headers.get("content-type", ""):
                    raise Exception("Não é imagem válida")

                image_path = f"temp/products/{key}.jpg"

                with open(image_path, "wb") as f:
                    f.write(response.content)

                save_stories(product, image_path, f"temp/stories/{key}.png")

                return key

            except Exception as e:
                logger.info(f"[{key}] Tentativa {attempt} falhou: {e}")

                if attempt == max_retries:
                    logger.info(f"[{key}] Ignorado após {max_retries} tentativas")
                    return None

                await asyncio.sleep(1)

async def generate_stories():
    clear_dir("temp")
    create_dir("temp/products")
    create_dir("temp/stories")

    sem = asyncio.Semaphore(10)
    products = await redis.get_products_by_prefix_with_keys("casa")

    logger.info(f"📥 Iniciando processamento de {len(products)} Stories")

    timeout = httpx.Timeout(20.0)
    limits = httpx.Limits(max_connections=20, max_keepalive_connections=10)

    async with httpx.AsyncClient(timeout=timeout, limits=limits) as client:
        tasks = [process_storie(client, key, product, sem) for key, product in products]

        await asyncio.gather(*tasks, return_exceptions=True)

    clear_dir("temp/products")
    logger.info("✅ Stories processados com sucesso!")

async def main():
    await wait_until_working_hours()

    last_ingestion = await redis.redis.get("last_ingestion")
    if not (
        last_ingestion
        and datetime.fromisoformat(last_ingestion).date() == datetime.now().date()
    ):
        await ingestion()
        await generate_stories()

    logger.info("🚀 Iniciando serviços Messengers")

    whatsapp = None
    instagram = None
    telegram = None

    whatsapp = Whatsapp()
    # instagram = Instagram()
    # telegram = Telegram()

    await instagram.start()

    logger.info("📤 Iniciando worker de envio...")

    await send_products_round_robin(whatsapp, telegram, instagram)

    logger.info("🏁 Expediente finalizado")

    await BrowserManager.close()

    clear_dir("temp")

if __name__ == "__main__":
    asyncio.run(main())
