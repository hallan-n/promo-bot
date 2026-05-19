from crawlers.amazon import get_products as amazon_get_products
from crawlers.mercadolivre import get_products as mercadolivre_get_products
from crawlers.shopee import get_products as shopee_get_products
from playwright.async_api import async_playwright
from playwright_stealth import Stealth
import asyncio


groups = [
    {
        "groups": [
            {"provider": "whatsapp", "id": "wp_32cq2e2"},
            {"provider": "whatsapp", "id": "wp_2ty5s2s"},
            {"provider": "telegram", "id": "tl_vvseqss"}
        ],
        "products": [
            {"provider": "amazon", "departament": "DF2EXFG", "product_limit": 50},
            {"provider": "mercadolivre", "departament": "3DXS32S", "product_limit": 50},
        ]
    }
]


async def main():
    async with Stealth().use_async(async_playwright()) as p:
        browser = await p.chromium.launch(headless=False)
        amazon_products = await amazon_get_products(browser, "18991080011", 5)
        mercadolivre_products = await mercadolivre_get_products(browser, "MLB1000", 15)

asyncio.run(main())
