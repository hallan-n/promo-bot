import asyncio
import json
import re
from playwright.async_api import async_playwright
from domain import BaseProcessor


class AmazonBronze(BaseProcessor):
    _dict_product_raw = {}

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
                    self.dict_product_raw = (
                        json.loads(f"[{match.group()[30:-1]}]")[0]
                        .get("prefetchedData")
                        .get("entity")
                        .get("rankedPromotions")
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

            page.on(
                "response",
                lambda response: asyncio.create_task(
                    self.handle_target_response(response)
                ),
            )

            await page.goto("https://www.amazon.com/-/pt/gp/goldbox?ref_=nav_cs_gb")

            return self._dict_product_raw
