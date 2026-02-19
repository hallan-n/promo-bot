from models import Product
from base import BaseMessenger
from webdriver.browser import BrowserManager
from urllib.parse import urlparse



class Instagram(BaseMessenger):
    def __init__(self):
        self.page = None

    async def start(self):
        browser = await BrowserManager.get_instance()
        self.page = await browser.new_page()
        await self.page.goto("https://www.instagram.com/promoraposa/")
        await self.page.reload()
        await self.page.click("div.EmbedInssistMenuButton")
        await self.page.click('div[data-id="story"]')

    async def send_message(self, key: str, product: Product):
        async with self.page.expect_file_chooser() as fc:
            await self.page.click("div.UploadCard")

        file_chooser = await fc.value
        await file_chooser.set_files(f"temp/stories/{key}.png")

        await self.page.wait_for_timeout(500)
        await self.page.click("div.clickable-inversed:has-text('Link')")
        await self.page.wait_for_timeout(500)
        await self.page.fill('input[placeholder="inssist.com"]', product.url)
        await self.page.wait_for_timeout(500)
        await self.page.fill(f'input[placeholder="{str(urlparse(product.url).netloc).upper()}"]', "Conferir ❤️")
        div_locator = self.page.locator(
            "div.absolute.opacity-0:has(div.cursor-crosshair)"
        )
        await div_locator.wait_for(timeout=5000)
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
