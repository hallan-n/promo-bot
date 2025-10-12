from models import Product, Session
from cache import get, add
import json
import asyncio
import re
from playwright.async_api import async_playwright, Page
from domain import BaseWebDriver



class Mercadolivre(BaseWebDriver):
    def __init__(self):
        self.products_raw = ''

    async def _handle_target_response(self, response):
        if response.url.startswith("https://www.mercadolivre.com.br/ofertas"):
            content_type = response.headers.get("content-type", "")
            if (
                content_type.strip().lower().replace(" ", "")
                == "text/html;charset=utf-8"
            ):
                text = await response.text()
                pattern = r"(?<=window\.__PRELOADED_STATE__ = ).+(?=;)"
                match = re.search(pattern, text)
                if match:
                    self.products_raw = match.group()

    async def _extract_products(self, page: Page):

            page.on(
                "response",
                lambda response: asyncio.create_task(
                    self._handle_target_response(response)
                ),
            )
            await page.goto("https://www.mercadolivre.com.br/ofertas")
            return self.products_raw
        

    def _extract_product(self, item):
        card = item.get("card", {})
        components = card.get("components", [])
        metadata = card.get("metadata", [])

        title = next(
            (comp["title"]["text"] for comp in components if "title" in comp.keys()),
            None,
        )
        price = next(
            (comp["price"] for comp in components if "price" in comp.keys()), None
        )
        original_price = price["previous_price"]["value"]
        price_discount = price["current_price"]["value"]
        discount = round((1 - (price_discount / original_price)) * 100, 2)

        installments = price.get("installments", {})
        values = {}
        for v in installments.get("values", []):
            if v.get("type") == "label":
                values[v["key"]] = v["label"]["text"]
            elif v.get("type") == "price":
                val = v["price"]["value"]
                values[v["key"]] = (
                    f"R$ {val:,.2f}".replace(",", "X")
                    .replace(".", ",")
                    .replace("X", ".")
                )

        payment_condition = installments.get("text", "").format(**values)

        url = metadata.get("url", "")
        thumbnail = f"https://http2.mlstatic.com/D_NQ_NP_{card['pictures']['pictures'][0]['id']}-O.webp"

        return Product(
            name=title,
            original_price=original_price,
            price_discount=price_discount,
            payment_condition=payment_condition,
            discount=discount,
            url=url,
            thumbnail=thumbnail,
        )
        
    async def exec(self):
        async with async_playwright() as p:
            browser = await p.chromium.launch(
                headless=False,
                args=[
                    "--disable-blink-features=AutomationControlled",
                    "--no-sandbox",
                    "--disable-dev-shm-usage",
                    "--ignore-certificate-errors",
                ],
            )
            page = await self.get_stealth_page(browser)

            session_raw = await get('session_mercadolivre')
            if not session_raw:
                await page.goto("https://www.mercadolivre.com/jms/mlb/lgz/msl/login")
                input('Digite qualquer coisa ao finalizar o login: ')
                await page.wait_for_load_state("domcontentloaded")
                session = await self.get_session(page)
                await add('session_mercadolivre', json.dumps(session.dict()))
            else:
                session = Session(**json.loads(session_raw))

            await self.inject_session(page, session)
            
            values_raw = await self._extract_products(page)

            items = json.loads(values_raw).get("data").get("items", [])

            products = {}
            for item in items:
                product = self._extract_product(item)
                products.update({product.url: product.dict()})

            
            await page.goto('https://www.mercadolivre.com.br/afiliados/hub#menu-user')
            await page.click('#AFFILIATES_LINK_BUILDER')
            await page.wait_for_timeout(2000)
            
            request = await page.context.request.post(
                'https://www.mercadolivre.com.br/affiliate-program/api/v2/affiliates/createLink',
                data={
                    "urls": list(products.keys()),
                    "tag": "nh20250617120350"
                }                   
            )
            content = await request.json()

            breakpoint()
            return products
