import asyncio
import json
import re
from cache import get, add
from datetime import datetime, timedelta
from consts import DAYS_TO_EXPIRE_SESSION

from models import Product, Session
from bot.stealth import get_stealth_page, inject_session

from playwright.async_api import async_playwright


async def _get_amazon_session() -> Session:
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
        page = await get_stealth_page(browser)

        await page.goto("https://www.amazon.com/gp/sign-in.html")

        skip = await page.query_selector('button[alt="Continuar comprando"]')
        if skip:
            await skip.click()

        await page.wait_for_selector("input#ap_email_login")
        await page.fill("input#ap_email_login", "")
        await page.click('input[type="submit"]')

        await page.wait_for_timeout(2000)
        user_fail = await page.query_selector("text=Parece que você é novo na Amazon")
        if user_fail:
            raise Exception("Login incorreto")

        await page.fill("input#ap_password", "")
        await page.click('input[type="submit"]')

        await page.wait_for_timeout(2000)
        pwd_fail = await page.query_selector("text=Houve um problema")
        if pwd_fail:
            raise Exception("Senha incorreta")

        verify_code = input("Insira o código de verificação")

        await page.fill('input[name="otpCode"]', verify_code)
        await page.click('input[type="submit"]')
        success_el = await page.wait_for_selector('text="Contas e Listas"')
        if not success_el:
            raise Exception("Elemento sucesso não encontrado")

        state = await page.context.storage_state()
        cookies = await page.context.cookies()
        local_storage = await page.evaluate("() => JSON.stringify(window.localStorage)")
        session_storage = await page.evaluate(
            "() => JSON.stringify(window.sessionStorage)"
        )

        return Session(
            state=state,
            cookies=cookies,
            local_storage=json.loads(local_storage),
            session_storage=json.loads(session_storage),
            login_at=datetime.now().isoformat(),
        )
dict_product_raw = {}
async def handle_target_response(response):
    global dict_product_raw
    if response.url.startswith("https://www.amazon.com/-/pt/gp/goldbox?ref_=nav_cs_gb"):
        content_type = response.headers.get("content-type", "")
        if content_type.strip().lower().replace(' ','') == "text/html;charset=utf-8":
            text = await response.text()
            
            pattern = r"assets\.mountWidget.*"
            match = re.search(pattern, text)
            
            if match:

                dict_product_raw = json.loads(f'[{match.group()[30:-1]}]')[0]['productSearchResponse']['products']





async def run():
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

        page = await get_stealth_page(browser)
        
        session = await get("amazon")

        if not session:
            session = await _get_amazon_session()
            await add('amazon', session.dict(), DAYS_TO_EXPIRE_SESSION * 86400)

        await inject_session(page, Session(**session))
        
        
        page.on(
            "response",
            lambda response: asyncio.create_task(handle_target_response(response)),
        )
                
        await page.goto("https://www.amazon.com/-/pt/gp/goldbox?ref_=nav_cs_gb")
        index = 1
        def safe_get(d, path, default=None):
            """Acessa valores aninhados com segurança usando uma lista de chaves."""
            for key in path:
                if isinstance(d, dict):
                    d = d.get(key)
                else:
                    return default
            return d if d is not None else default
        for item in dict_product_raw:
            product = Product(
                name=item.get('title'),
                description=safe_get(item, ['messaging', 'content', 'fragments', 0, 'text']),
                original_price=safe_get(item, ['price', 'basisPrice', 'price']),
                price_discount=safe_get(item, ['price', 'priceToPay', 'price']),
                payment_condition="asdasd",
                url=f"https://www.amazon.com{item.get('link')}",
                thumbnail=f"{safe_get(item, ['image', 'hiRes', 'baseUrl'])}.jpg"
            )
            await add(f'amazon-{index}', product.dict())
            index+=1

        
