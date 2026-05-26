import asyncio
from datetime import datetime
from uuid import uuid4

import uvicorn
from crawlers.amazon import get_products as amazon_get_products
from crawlers.mercadolivre import get_products as mercadolivre_get_products
from crawlers.shopee import get_products as shopee_get_products
from fastapi import FastAPI
from models import to_list_dict
from mongo import find_many, find_one, get_database, insert_one, update_one
from playwright.async_api import async_playwright
from playwright_stealth import Stealth
from logger import logger

app = FastAPI()


def handler_get_products(provider: str):
    match provider:
        case "mercadolivre":
            return mercadolivre_get_products

        case "amazon":
            return amazon_get_products

        case "shopee":
            return shopee_get_products

        case _:
            return None


async def scrape_products():
    async with Stealth().use_async(async_playwright()) as p:
        browser = await p.chromium.launch(headless=False)

        try:
            db = await get_database()

            groups_db = db["groups"]
            products_db = db["products"]

            settings = await find_many(groups_db)

            if not settings:
                return

            for group in settings[0].get("groups", []):

                all_products = []

                for product_setting in group.get("products", []):

                    get_products = handler_get_products(product_setting.get("provider"))

                    if not get_products:
                        continue

                    products = await get_products(
                        browser,
                        product_setting.get("departament"),
                        product_setting.get("product_limit"),
                    )

                    all_products.extend(to_list_dict(products))

                has_products = await find_one(products_db, {"name": group.get("name")})

                if has_products:
                    await update_one(
                        products_db,
                        {"name": group.get("name")},
                        {"products": all_products, "updated_at": datetime.utcnow()},
                    )

                else:
                    await insert_one(
                        products_db,
                        {
                            "name": group.get("name"),
                            "products": all_products,
                            "created_at": datetime.utcnow(),
                        },
                    )

        finally:
            await browser.close()


async def run_scrape(job_id: str):
    db = await get_database()
    jobs_db = db["jobs"]

    try:
        await scrape_products()

        await update_one(
            jobs_db,
            {"_id": job_id},
            {"status": "success", "finished_at": datetime.utcnow(), "message": None},
        )
        logger.info(f"Sucesso ao raspar produtos pro JobID {job_id}")
    except Exception as e:
        await update_one(
            jobs_db,
            {"_id": job_id},
            {"status": "error", "message": str(e), "finished_at": datetime.utcnow()},
        )


@app.post("/scrape")
async def trigger_scrape():
    db = await get_database()
    jobs_db = db["jobs"]

    job_id = str(uuid4())

    await insert_one(
        jobs_db,
        {
            "_id": job_id,
            "status": "running",
            "started_at": datetime.utcnow(),
            "finished_at": None,
            "message": None,
        },
    )

    asyncio.create_task(run_scrape(job_id))
    logger.info(f"Iniciando raspagem de produtos para o JobID {job_id}")
    return {"job_id": job_id, "status": "running"}


@app.get("/scrape/{job_id}")
async def get_status(job_id: str):
    db = await get_database()
    jobs_db = db["jobs"]

    job = await find_one(jobs_db, {"_id": job_id})

    if not job:
        logger.error(f"Erro ao consultar o JobID {job_id}")
        return {"error": "job not found"}
    
    logger.info(f"Consulta realizada para o JobID {job_id}")
    return job


@app.get("/products")
async def get_products(created_at: str = None, group_name: str = None):
    if created_at and group_name:
        filters = {"name": group_name, "created_at": created_at}
    elif not created_at and group_name:
        filters = {"name": group_name}
    elif created_at and not group_name:
        filters = {"created_at": created_at}
    else:
        filters = None

    db = await get_database()
    products_db = db["products"]
    logger.info(f"Consulta de produtos realizada com sucesso")
    return await find_many(products_db, filters)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
