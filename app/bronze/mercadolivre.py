import asyncio
from logging import info
import re
from playwright.async_api import async_playwright
from domain import BaseProcessor, BaseWebDriver


class MercadolivreBronze(BaseWebDriver, BaseProcessor):
    def __init__(self):
        self.products_raw = ''
    
    async def handle_target_response(self, response):
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

            page.on(
                "response",
                lambda response: asyncio.create_task(
                    self.handle_target_response(response)
                ),
            )

            await page.goto("https://www.mercadolivre.com.br/ofertas")
            info('Produtos MercadoLivre capturados no site')
            return self.products_raw
