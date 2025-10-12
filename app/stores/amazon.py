import json
from logging import info
from cache import get, add
import asyncio
import re
from playwright.async_api import async_playwright
from domain import BaseWebDriver
from logging import info

class Amazon(BaseWebDriver):
    def __init__(self):
        self.products_raw = ''

    async def _handle_target_response(self, response):
        if response.url.startswith(
            "https://www.amazon.com/-/pt/gp/goldbox?ref_=nav_cs_gb"
        ):
            content_type = response.headers.get("content-type", "")
            if content_type.strip().lower().replace(" ", "") == "text/html;charset=utf-8":
                text = await response.text()

                pattern = r"assets\.mountWidget.*"
                match = re.search(pattern, text)
                if match:
                    self.products_raw = f"[{match.group()[30:-1]}]"
    
    async def _extract_products(self):
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

            page.on(
                "response",
                lambda response: asyncio.create_task(
                    self._handle_target_response(response)
                ),
            )

            await page.goto("https://www.amazon.com/-/pt/gp/goldbox?ref_=nav_cs_gb")
            info('Produtos Amazon capturados no site')
            return self.products_raw
        
    async def exec(self):

        values_raw = await get('amazon')
        if not values_raw:
            values_raw = await self._extract_products()
            await add('amazon', values_raw, 86400)
    
        
        # items = json.loads(values_raw).get("data").get("items", [])

        # products = []
        # for item in items:
        #     products.append(self._extract_product(item))
        # return products


