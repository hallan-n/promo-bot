import asyncio
import json
import re

from session import inject_session
from models import Product, to_brl
from playwright.async_api import Browser, Page
from logger import logger
import math

MAX_PRODUCTS_PER_PAGE = 47




async def _process_products(product_data: dict, page: Page):
    items: list[dict] = product_data.get("appProps", {}).get("pageProps", {}).get("data").get("items", [])
    products = []
    for item in items:
        _image_id = item.get("card", {}).get("pictures", {}).get("pictures", [{}])[0].get("id", "")

        current_url = item.get("card", {}).get("metadata", {}).get("url", "")


        response_short_url = await page.request.post(
            "https://www.mercadolivre.com.br/affiliate-program/api/v2/affiliates/createLink",
            headers={"x-csrf-token": product_data["csrfToken"]},
            data={"urls": [current_url], "tag":"hn20260209112139"}
        )
        data_short_url = await response_short_url.json()
        short_url = data_short_url.get("urls")[0].get("short_url")


        name = ""
        original_price = 0.0
        price_discount = 0.0
        payment_condition = ""
        discount = ""
        url = short_url
        thumbnail = f"https://http2.mlstatic.com/D_NQ_NP_{_image_id}-O.webp"


        
        components = item.get("card", {}).get("components")
    
        for component in components:
            comp_type = component.get("type")
            match comp_type:
                case "title":
                    name = component.get("title", {}).get("text")
                case "price":
                    original_price = component.get("price", {}).get("previous_price", {}).get("value")
                    price_discount = component.get("price", {}).get("current_price", {}).get("value")
                    discount = component.get("price", {}).get("discount_label", {}).get("text", "")
                    
                    _payment_condition = {}
                    for _value_installment in component.get("price", {}).get("installments", {}).get("values", []):
                        key = _value_installment.get("key")
                        value = ""

                        match _value_installment.get("type"):
                            case "label": value = _value_installment.get("label", {}).get("text", "")
                            case "price": value = to_brl(_value_installment.get("price", {}).get("value"))
                        _payment_condition.update({key: value})
                    payment_condition = component.get("price", {}).get("installments", {}).get("text", "").format(**_payment_condition)

        products.append(
            Product(
                name=name,
                original_price=original_price,
                price_discount=price_discount,
                payment_condition=payment_condition,
                cupom="",
                discount=discount,
                url=url,
                thumbnail=thumbnail,
            )
        )
    return products        

async def get_dict_response(page: Page) -> dict:
    html = await page.content()
    json_match = re.search(r"(_n\.ctx\.r\s{0,}=\s{0,})(.*)(;_n\.ctx\.r\.assets\.manifest)", html).group(2)
    return json.loads(json_match)


async def get_products(browser: Browser, departament_code: str, product_limit: int) -> list[Product]:
    max_pages = math.ceil(product_limit / MAX_PRODUCTS_PER_PAGE)

    async def open_page(browser, departament_code: str, page_number: int):
        page = await browser.new_page()
        await inject_session(page, "mercadolivre.json")
        await page.goto(f"https://www.mercadolivre.com.br/ofertas?category={departament_code}&page={page_number}")
        return page


    tasks = [
        open_page(browser, departament_code, i+1)
        for i in range(max_pages)
    ]

    pages: list[Page] = await asyncio.gather(*tasks)
    responses = [(await get_dict_response(page), page) for page in pages]
    open("saida.json", "w").write(json.dumps(responses[0][0]))
    semaphore = asyncio.Semaphore(2)

    async def process_products(response, page):
        async with semaphore:
            return await _process_products(response, page)


    products: list[Product] = await asyncio.gather(
        *[
            process_products(response, page)
            for response, page in responses
        ]
    )

    return products
