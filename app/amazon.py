import os
from playwright.async_api import async_playwright
from playwright_stealth import Stealth
from base import WebDriver
from models import Product
from consts import SESSION_PATH


class Amazon(WebDriver):
    name = "amazon"
    session_path = f"{SESSION_PATH}/{name}.json"

    async def amazon_save_session(self):
        async with Stealth(navigator_languages_override=("pt-BR")).use_async(
            async_playwright()
        ) as p:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            await page.goto("https://www.amazon.com.br/")
            input("Click em qualquer tecla ao finalizar o login.")
            session = await self.get_session(page)

            with open(self.session_path, "w") as doc:
                doc.write(session.json())

    async def amazon_save_deals(self):
        async with Stealth(navigator_languages_override=("pt-BR")).use_async(
            async_playwright()
        ) as p:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            await self.inject_session(page, self.session_path)


            response = await page.request.get(
                'https://www.amazon.com.br/d2b/api/v1/products/search?pageSize=30&startIndex=0&calculateRefinements=false&rankingContext={"pageTypeId":"deals","rankGroup":"DEFAULT"}'
            )
            if response.ok:
                data = await response.json()

            products = []
            for product in data['products']:
                thumbnail = product.get("image", {}).get("hiRes")
                price = product.get('price', {})
                
                response = await page.request.get(
                    f"https://www.amazon.com.br/associates/sitestripe/getShortUrl?longUrl=https://www.amazon.com.br{product.get('link', {})}"
                )

                if response.ok:
                    data = await response.json()
                    
                url = data.get("shortUrl")

                products.append(
                    Product(
                        name=product.get('title'),
                        original_price=float(price.get("basisPrice", {}).get("price", 0.0)),
                        price_discount=float(price.get("priceToPay", {}).get("price", 0.0)),
                        url=url or f"https://www.amazon.com.br{product.get('link', {})}",
                        thumbnail=f"{thumbnail.get("baseUrl")}.{thumbnail.get("extension")}",
                        discount=product.get("dealBadge", {}).get("label", {}).get("content", {}).get("fragments", [{}])[0].get("text", "")
                    ).dict()
                )
            
            return products
        

    async def exec(self):
        if not os.path.exists("app/sessions/amazon.json"):
            await self.amazon_save_session()

        return await self.amazon_save_deals()