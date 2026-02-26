import os
from urllib.parse import urlparse

from services.webdriver.base import BaseMessenger
from models import Product
from services.logger import logger
from services.webdriver.browser import BrowserManager


class Instagram(BaseMessenger):
    def __init__(self):
        self.page = None

    async def start(self, tab: str = None):
        browser = await BrowserManager.get_instance()
        self.page = await browser.new_page()
        await self.page.goto("https://www.instagram.com/promoraposa/")
        await self.page.wait_for_load_state("domcontentloaded")

        await self.page.reload()
        if tab == "chat":
            await self.page.locator('div.HeroInteractionIgnoreWithDiv:has(a[href="/direct/inbox/"])').click()
        else:
            await self.page.click("div.EmbedInssistMenuButton")
            await self.page.click('div[data-id="story"]')

    async def send_chat(self, username: str, message: str, image_path: str = None):
        try:
            await self.page.fill('input[name="searchInput"]', "")
            await self.page.locator('input[name="searchInput"]').type(username)
            await self.page.locator(f'div.WebPressable[role="button"]:has-text("{username}") >> nth=0').click(timeout=6000)

            if image_path:
                async with self.page.expect_file_chooser() as fc:
                    await self.page.locator('div.PressableText:has(svg[aria-label="Adicionar foto ou vídeo"])').click()

                file_chooser = await fc.value
                await file_chooser.set_files(image_path)
                await self.page.wait_for_timeout(500)
                await self.page.locator(f'div[role="button"]:has-text("Enviar")').click()

            await self.page.fill('div.LexicalContentEditable_prod[aria-label="Mensagem"][contenteditable="true"]', message)
            await self.page.locator(f'div[role="button"]:has-text("Enviar")').click()
            await self.page.wait_for_timeout(300)
            await self.page.locator('div.HeroInteractionIgnoreWithDiv:has(a[href="/direct/inbox/"])').click()
        except:
            logger.info(f"{username} não encontrado!")
            await self.page.wait_for_timeout(300)
            await self.page.locator('div.HeroInteractionIgnoreWithDiv:has(a[href="/direct/inbox/"])').click()
        
    async def send_message(self, key: str, product: Product):
        if not os.path.exists(f"temp/stories/{key}.png"):
            logger.error(
                f"❌ O Storie temp/stories/{key}.png não foi gerado corretamente."
            )
            return

        async with self.page.expect_file_chooser() as fc:
            await self.page.click("div.UploadCard")

        file_chooser = await fc.value
        await file_chooser.set_files(f"temp/stories/{key}.png")

        await self.page.wait_for_timeout(500)
        await self.page.click("div.clickable-inversed:has-text('Link')")
        await self.page.wait_for_timeout(500)
        await self.page.fill('input[placeholder="inssist.com"]', product.url)
        await self.page.wait_for_timeout(500)
        await self.page.fill(
            f'input[placeholder="{str(urlparse(product.url).netloc).upper()}"]',
            "amazon.com.br",
        )
        div_locator = self.page.locator(
            "div.absolute.opacity-0:has(div.cursor-crosshair)"
        )
        await div_locator.wait_for()
        div = await div_locator.element_handle()
        box = await div.bounding_box()
        center_x = box["x"] + box["width"] / 2
        center_y = box["y"] + box["height"] / 2

        await self.page.mouse.move(center_x, center_y)
        await self.page.mouse.down()
        await self.page.mouse.move(center_x, center_y + 270, steps=10)
        await self.page.mouse.up()

        await self.page.wait_for_timeout(1000)

        await self.page.click("button.ActionButton")

        await self.page.wait_for_selector("div.UploadCard:not([inert])")
