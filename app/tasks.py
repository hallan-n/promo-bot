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
from services.webdriver.whatsapp import Whatsapp

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


async def extract_all_contacts(whatsapp: Whatsapp, group_names: list) -> list:
    numbers = set()

    for group_name in group_names:
        nums = await whatsapp.extra_contacts(group_name)

        for number in nums:
            numbers.add(number)

    return list(numbers)


async def main():
    # await wait_until_working_hours()

    # last_ingestion = await redis.redis.get("last_ingestion")
    # if not (
    #     last_ingestion
    #     and datetime.fromisoformat(last_ingestion).date() == datetime.now().date()
    # ):
    #     await ingestion()
    #     await generate_stories()

    # logger.info("🚀 Iniciando serviços Messengers")

    whatsapp = Whatsapp()
    # instagram = Instagram()
    # telegram = Telegram()

    # await instagram.start()
    await whatsapp.start()

    await asyncio.Event().wait()

    logger.info("📤 Iniciando worker de envio...")

    # await send_products_round_robin(whatsapp, telegram, instagram)
    # await send_products_round_robin(None, None, instagram)

    logger.info("🏁 Expediente finalizado")

    await BrowserManager.close()

    clear_dir("temp")



async def invite_to_group():
    insta_contacts = []
    wpp_contacts = []
    wpp_message = """
Olá! Tudo bem? 😊
Para economizar de verdade nas comprinhas para casa, criei o *Raposa Casa* 🏡 para compartilhar as melhores promoções, achadinhos e cupons exclusivos, tudo para o lar! 🛍️

Se quiser acompanhar as ofertas, é só entrar no *Grupo Vip* aqui abaixo: ⬇️
🔗 https://chat.whatsapp.com/ENCVj8nvoNwCOFR1sj3raK
"""

    insta_message = [
"""
Olá! Tudo bem? 😊
Para economizar de verdade nas comprinhas para casa, criei o Raposa Casa 🏡 para compartilhar as melhores promoções, achadinhos e cupons exclusivos, tudo para o lar! 🛍️

Se quiser acompanhar as ofertas, é só entrar no Grupo Vip aqui abaixo: ⬇️""", "🔗 https://chat.whatsapp.com/ENCVj8nvoNwCOFR1sj3raK"]
    
    with open("followers1.json", "r") as doc:
        insta_contacts: list = json.loads(doc.read())

    with open("contatos1.json", "r") as doc:
        wpp_contacts: list = json.loads(doc.read())
    

    instagram = Instagram()
    # whatsapp = Whatsapp()

    await instagram.start("chat")
    # await whatsapp.start("chat")
    
    try:
        while insta_contacts or wpp_contacts:
            first_insta = insta_contacts.pop(0) if insta_contacts else None
            # first_wpp = wpp_contacts.pop(0) if wpp_contacts else None

            if first_insta:
                await instagram.send_chat(first_insta.get("Username"), insta_message[0])
                await instagram.send_chat(first_insta.get("Username"), insta_message[1])

            # if first_wpp:
            #     await whatsapp.send_chat(first_wpp, wpp_message, "assets/invite.png")

            logger.info(f"Faltam {len(insta_contacts)} perfis pro Instagram")
            # logger.info(f"Faltam {len(wpp_contacts)} contatos pro Whatsapp")
            logger.info("Dormindo 20s")

            with open("followers1.json", "w") as doc:
                doc.write(json.dumps(insta_contacts, indent=4))

            # with open("contatos1.json", "w") as doc:
            #     doc.write(json.dumps(wpp_contacts, indent=4))
            await asyncio.sleep(20)
    except Exception as e:

        with open("followers1.json", "w") as doc:
            doc.write(json.dumps(insta_contacts, indent=4))

        # with open("contatos1.json", "w") as doc:
        #     doc.write(json.dumps(wpp_contacts, indent=4))
        raise
    
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
