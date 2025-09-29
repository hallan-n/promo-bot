import asyncio
import re
from playwright.async_api import async_playwright
from domain import BaseProcessor, BaseWebDriver
from logging import info


class AmazonBronze(BaseWebDriver, BaseProcessor):
    def __init__(self):
        self.products_raw = ''
    
    async def handle_target_response(self, response):
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

            await page.goto("https://www.amazon.com/-/pt/gp/goldbox?ref_=nav_cs_gb")
            info('Produtos Amazon capturados no site')
            return self.products_raw
