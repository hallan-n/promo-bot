from models import to_list_dict
from mongo import get_database, find_many, insert_one
from crawlers.amazon import get_products as amazon_get_products
from crawlers.mercadolivre import get_products as mercadolivre_get_products
from crawlers.shopee import get_products as shopee_get_products
from playwright.async_api import async_playwright
from playwright_stealth import Stealth
from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()


def handler_get_products(provider: str):
    match provider:
        case "mercadolivre": return mercadolivre_get_products
        case "amazon": return amazon_get_products
        case _: return None

@app.get("/")
async def main():
    try:
        async with Stealth().use_async(async_playwright()) as p:
            browser = await p.chromium.launch(headless=False)

            db = await get_database()
            groups_db = db["groups"]
            settings = await find_many(groups_db)
            
            for group in settings[0].get("groups"):
                all_products = []
                for product_setting in group.get("products"): 
                    get_products = handler_get_products(product_setting.get("provider"))
                    products = await get_products(
                        browser,
                        product_setting.get("departament"),
                        product_setting.get("product_limit")
                    )
                    all_products = all_products + to_list_dict(products)

                products_db = db["products"]
                await insert_one(products_db, {
                    "name": group.get("name"),
                    "products": all_products
                })

                all_products.clear()
        return {"success": True}
    except:
        raise HTTPException(400, "Erro ao processar arquivos")

if __name__ == "__main__":
    uvicorn.run(app)