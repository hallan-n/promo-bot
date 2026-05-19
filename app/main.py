import asyncio

from amazon import get_products as amazon_get_products
from mercadolivre import get_products as mercadolivre_get_products
from playwright.async_api import async_playwright
from session import export_session, inject_session
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def main():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--disable-dev-shm-usage",
                "--no-sandbox",
                "--disable-infobars",
                "--start-maximized",
            ],
        )
        # products = await get_products(browser, "18991080011", 5, 1, 100)
        products = await get_products(browser, "MLB1000", 15)
        # await export_session(page.context)

        # am = Amazon(browser, 'session.json')
        # await am.get_products("asd", 1, 2, 3)


import uvicorn

uvicorn.run(app, "0.0.0.0")