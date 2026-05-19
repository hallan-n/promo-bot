import asyncio
import json
import re

from logger import logger
from models import Product
from playwright.async_api import Browser, Page
from session import inject_session


async def _process_product(product: dict, page: Page):
    thumbnail = product.get("image", {}).get("hiRes")
    price = product.get("price", {})
    link = product.get("link")
    payment_condition = None
    cupom = None
    short_url = None

    pdp_response = await page.request.get(f"https://www.amazon.com.br{link}")
    html = await pdp_response.text()

    match = re.search(r"Em até .*? sem juros", html)
    if match:
        payment_condition = match.group(0)

    match = re.search(r"(com o cupom )(\w+).*?", html)
    if match:
        cupom = match.group(2)

    short_response = await page.request.get(
        f"https://www.amazon.com.br/associates/sitestripe/getShortUrl?longUrl=https://www.amazon.com.br{link}"
    )
    short_data = await short_response.json()
    short_url = short_data["shortUrl"]

    return Product(
        name=product.get("title"),
        original_price=float(price.get("basisPrice", {}).get("price", 0.0)),
        price_discount=float(price.get("priceToPay", {}).get("price", 0.0)),
        url=short_url,
        payment_condition=payment_condition,
        cupom=cupom,
        thumbnail=(
            f"{thumbnail.get('baseUrl')}.{thumbnail.get('extension')}"
            if thumbnail
            else None
        ),
        discount=product.get("dealBadge", {})
        .get("label", {})
        .get("content", {})
        .get("fragments", [{}])[0]
        .get("text", ""),
    )


async def get_products(
    browser: Browser,
    departament_code: str,
    product_limit: int,
    min_discount: int,
    max_discount: int,
) -> list[Product]:

    page = await browser.new_page()
    await inject_session(page, "session.json")
    await page.goto("https://www.amazon.com.br")

    def compact(obj):
        return json.dumps(obj, separators=(",", ":"))

    params = {
        "pageSize": str(product_limit),
        "startIndex": "0",
        "calculateRefinements": "false",
        "rankingContext": compact({"pageTypeId": "deals", "rankGroup": "DEFAULT"}),
        "filters": compact(
            {
                "includedDepartments": [],
                "excludedDepartments": [],
                "includedTags": [],
                "excludedTags": ["EINKBF25"],
                "promotionTypes": [],
                "accessTypes": [],
                "brandIds": [],
                "unifiedIds": [],
            }
        ),
        "refinementFilters": compact(
            [{"id": "departments", "value": [departament_code]}]
        ),
        "rangeRefinementFilters": compact(
            [{"id": "percentOff", "min": min_discount, "max": max_discount}]
        ),
        "pinningConfiguration": compact({"pinnedPromotionsLayoutGroup": "default"}),
    }

    response = await page.request.get(
        "https://www.amazon.com.br/d2b/api/v1/products/search", params=params
    )

    if not response.ok:
        await page.close()
        return []

    data = await response.json()

    semaphore = asyncio.Semaphore(4)

    async def process_with_limit(product, page):
        async with semaphore:
            return await _process_product(product, page)

    tasks = [process_with_limit(product, page) for product in data["products"]]

    results = await asyncio.gather(*tasks, return_exceptions=True)

    products = [r for r in results if not isinstance(r, Exception)]

    await page.close()
    logger.info(f"{len(products)} produtos capturados")

    return products
