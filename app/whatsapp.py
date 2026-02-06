from playwright.async_api import async_playwright
from playwright_stealth import Stealth
from base import WebDriver
from consts import SESSION_PATH


class Amazon(WebDriver):
    name = "whatsapp"
    session_path = f"{SESSION_PATH}/{name}.json"

    async def amazon_save_session(self):
        async with Stealth(navigator_languages_override=("pt-BR")).use_async(
            async_playwright()
        ) as p:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            await page.goto("https://web.whatsapp.com/")
            input("Click em qualquer tecla ao finalizar o login.")
            session = await self.get_session(page)

            with open(self.session_path, "w") as doc:
                doc.write(session.json())

    async def exec(self):
        ...