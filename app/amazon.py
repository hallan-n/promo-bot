from models import Product
from playwright.async_api import async_playwright
from playwright_stealth import Stealth


class Amazon:
    async def exec(self):
        async with Stealth(navigator_languages_override=("pt-BR")).use_async(
            async_playwright()
        ) as p:
            context = await p.chromium.launch_persistent_context(
                user_data_dir="./profile", channel="chrome", headless=False
            )

            page = await context.new_page()

            response = await page.request.get(
                'https://www.amazon.com.br/d2b/api/v1/products/search?pageSize=30&startIndex=0&calculateRefinements=false&rankingContext={"pageTypeId":"deals","rankGroup":"DEFAULT"}'
            )
            if response.ok:
                data = await response.json()

            products = []
            for product in data["products"]:
                thumbnail = product.get("image", {}).get("hiRes")
                price = product.get("price", {})

                response = await page.request.get(
                    f"https://www.amazon.com.br/associates/sitestripe/getShortUrl?longUrl=https://www.amazon.com.br{product.get('link', {})}"
                )

                if response.ok:
                    data = await response.json()

                url = data.get("shortUrl")

                products.append(
                    Product(
                        name=product.get("title"),
                        original_price=float(
                            price.get("basisPrice", {}).get("price", 0.0)
                        ),
                        price_discount=float(
                            price.get("priceToPay", {}).get("price", 0.0)
                        ),
                        url=url
                        or f"https://www.amazon.com.br{product.get('link', {})}",
                        thumbnail=f"{thumbnail.get("baseUrl")}.{thumbnail.get("extension")}",
                        discount=product.get("dealBadge", {})
                        .get("label", {})
                        .get("content", {})
                        .get("fragments", [{}])[0]
                        .get("text", ""),
                    ).dict()
                )

            return products
