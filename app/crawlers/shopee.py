import asyncio
import json
import math
import re

from logger import logger
from models import Product, to_brl
from playwright.async_api import Browser, Page
from session import inject_session, export_session
from urllib.parse import urlencode



def build_pdp_url(data: dict) -> str:
    item = data["customised_item_card"]["item_data"]

    params = {
        "display_model_id": item["item_card_display_price"]["model_id"],
        "item_id": item["itemid"],
        "shop_id": item["shopid"],

        # parâmetros praticamente fixos
        "tz_offset_in_minutes": -180,
        "detail_level": 0,
        "incoming_pdp_page_source": 0,
        "incoming_pdp_page_scenario": 0
    }

    return (
        "https://shopee.com.br/api/v4/pdp/get_pc?"
        + urlencode(params)
    )

def build_product(data: dict) -> "Product":
    data = data["data"]

    item = data["item"]
    product_price = data["product_price"]
    installment = data["promotion_info"]["installment"]

    item_id = item["item_id"]
    shop_id = item["shop_id"]

    original_price = product_price["price_before_discount"]["single_value"] / 100000      
    price_discount = product_price["price"]["single_value"] / 100000
    payment_condition = f'em até {installment["month"]}x sem juros'

    url = f"https://shopee.com.br/product/{shop_id}/{item_id}"

    return Product(
        name=item["title"],
        original_price=original_price,
        price_discount=price_discount,
        payment_condition=payment_condition,
        cupom="",  # não encontrei no retorno
        discount=f'{product_price["discount"]}% OFF',
        url=url,
        thumbnail=f"https://cf.shopee.com.br/file/{item['image']}"
    )


async def get_affiliate_link(page: Page, product_url: str):
    return await page.evaluate(
        """
        async (productUrl) => {
            const response = await fetch(
                "https://affiliate.shopee.com.br/api/v3/gql?q=batchCustomLink",
                {
                    method: "POST",
                    credentials: "include",
                    headers: {
                        "accept": "application/json, text/plain, */*",
                        "affiliate-program-type": "1",
                        "content-type": "application/json; charset=UTF-8"
                    },
                    body: JSON.stringify({
                        operationName: "batchGetCustomLink",
                        query: `
                            query batchGetCustomLink(
                                $linkParams: [CustomLinkParam!],
                                $sourceCaller: SourceCaller
                            ) {
                                batchCustomLink(
                                    linkParams: $linkParams,
                                    sourceCaller: $sourceCaller
                                ) {
                                    shortLink
                                    longLink
                                    failCode
                                }
                            }
                        `,
                        variables: {
                            linkParams: [
                                {
                                    originalLink: productUrl,
                                    advancedLinkParams: {}
                                }
                            ],
                            sourceCaller: "CUSTOM_LINK_CALLER"
                        }
                    })
                }
            );

            return await response.json();
        }
        """,
        product_url
    )

async def get_product_details(page: Page, url: str):
    return await page.evaluate("""
        async (url) => {
            const response = await fetch(url,
                {
                    method: "GET",
                    credentials: "include",
                    headers: {
                        "accept": "application/json",
                        "x-api-source": "pc",
                        "x-requested-with": "XMLHttpRequest"
                    }
                }
            );

            return await response.json();
        }
        """, url)
    
async def get_products(browser: Browser) -> list[Product]:
    page = await browser.new_page()
    await inject_session(page, "shopee.json")

    result = None

    async def capture(response):
        nonlocal result

        if "/api/v4/collection/get_items" in response.url:
            try:
                result = await response.json()
            except:
                pass

    page.on("response", capture)

    await page.goto(
        "https://shopee.com.br/collections/18482320",
        wait_until="networkidle"
    )

    while result is None:
        await asyncio.sleep(0.1)

    products = []

    for item in result.get("data", {}).get("items", []):
        pdp_url = build_pdp_url(item)
        product_details = await get_product_details(page, pdp_url)
        product = build_product(product_details)
        products.append(product)

    return products
