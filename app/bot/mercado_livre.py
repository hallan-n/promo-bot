import asyncio
import json
import re
from cache import add
from playwright.async_api import async_playwright
from models import Product
from bot.stealth import get_stealth_page


def extract_data(json_original) -> Product:
    card = json_original.get("card", {})
    metadata = card.get("metadata", {})
    components = card.get("components", [])
    pictures = card.get("pictures", {})
    picture_list = pictures.get("pictures", [])

    image_url = ""
    if picture_list:
        picture_id = picture_list[0].get("id")
        if picture_id:
            image_url = f"https://http2.mlstatic.com/D_{picture_id}-O.jpg"

    title = ""
    original_price = 0.0
    price_discount = 0.0
    description = ""
    url = metadata.get("url", "").replace("\\u002F", "/")
    if url.startswith("click1"):
        return None

    parcelas_text = None

    for componente in components:
        tipo = componente.get("type")
        if tipo == "title":
            title = componente.get("title", {}).get("text", "")
        elif tipo == "price":
            preco = componente.get("price", {})
            original_price = float(preco.get("previous_price", {}).get("value", 0))
            price_discount = float(preco.get("current_price", {}).get("value", 0))

            installments = preco.get("installments", {})
            if installments:
                no_interest = installments.get("no_interest", False)
                values = installments.get("values", [])
                if no_interest and values:
                    raw_text = installments.get("text", "")
                    match = re.search(r"(\d+)x", raw_text)
                    if match:
                        parcelas = int(match.group(1))
                        valor_parcela = values[0].get("price", {}).get("value", 0)
                        if valor_parcela > 0:
                            valor_formatado = f"R${valor_parcela:,.2f}".replace(".", ",")
                            parcelas_text = f"{parcelas}x de {valor_formatado} sem juros"
                        else:
                            parcelas_text = None
                else:
                    parcelas_text = None
        elif tipo == "highlight":
            description = (
                componente.get("highlight", {})
                .get("text", "")
                .replace("{}", "")
                .strip()
            )

    return Product(
        name=title,
        description=description,
        original_price=original_price,
        price_discount=price_discount,
        payment_condition=parcelas_text,
        url=url,
        thumbnail=image_url,
    )


dict_product_raw = {}


async def handle_target_response(response):
    global dict_product_raw
    if response.url.startswith("https://www.mercadolivre.com.br/ofertas"):
        content_type = response.headers.get("content-type", "")
        if content_type.strip().lower() == "text/html; charset=utf-8":
            text = await response.text()
            pattern = r"(?<=window\.__PRELOADED_STATE__ = ).+(?=;)"
            match = re.search(pattern, text)
            if match:
                print("Interceptando requisição aos produtos")
                dict_product_raw = json.loads(match.group())


async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--ignore-certificate-errors",
            ],
        )
        page = await get_stealth_page(browser)
        page.on(
            "response",
            lambda response: asyncio.create_task(handle_target_response(response)),
        )

        await page.goto("https://www.mercadolivre.com.br/ofertas")

        if dict_product_raw:
            index = 1
            for item in dict_product_raw.get("data").get("items"):
                product = extract_data(item)
                if not product:
                    continue
                await add(f"mercadolivre-{index}", product.dict())
                index += 1
        await browser.close()
