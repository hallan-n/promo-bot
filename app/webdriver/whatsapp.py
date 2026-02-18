from base import BaseMessenger
from models import Product
from utils import format_brl
from webdriver.browser import BrowserManager


class Whatsapp(BaseMessenger):
    def __init__(self):
        self.page = None

    async def start(self):
        browser = await BrowserManager.get_instance()
        self.page = await browser.new_page()
        await self.page.goto("https://web.whatsapp.com/")
        await self.page.wait_for_selector(
            'div:has-text("Protegida com a criptografia de ponta a ponta")',
            state="detached",
        )

    def get_template_message(self, product: Product) -> str:
        lines = [
            f"🦊 {product.name}\n",
            f"~de R$ {format_brl(product.original_price)}~",
            f"*por R$ {format_brl(product.price_discount)} 😱😱*\n",
        ]

        if product.payment_condition:
            lines.append(f"💳 {product.payment_condition}")

        if product.cupom:
            lines.append(f"🎟️ Use o cupom: {product.cupom}")

        if product.payment_condition or product.cupom:
            lines.append("")

        if product.url:
            lines.append(product.url)

        return "\n".join(lines)

    async def send_message(self, group_name, product: Product):

        message_list = await self.page.query_selector(
            'div[aria-label="Lista de conversas"]'
        )

        await self.page.wait_for_timeout(1000)

        chat = await message_list.query_selector(
            f'div[role="row"]:has(span:text("{group_name}"))'
        )

        await self.page.wait_for_timeout(1000)

        await chat.click()

        response = await self.page.request.get(product.thumbnail)

        content = await response.body()

        with open("./assets/product.jpg", "wb") as f:
            f.write(content)

        await self.page.click('button[aria-label="Anexar"]')

        await self.page.wait_for_timeout(1000)

        async with self.page.expect_file_chooser() as fc:
            await self.page.get_by_label("Fotos e vídeos").click()

        file_chooser = await fc.value
        await file_chooser.set_files("./assets/product.jpg")

        box = self.page.locator(
            'div[contenteditable="true"][aria-placeholder="Digite uma mensagem"]'
        ).first

        await self.page.wait_for_timeout(1000)

        await box.click()

        await self.page.wait_for_timeout(1000)

        await box.fill(self.get_template_message(product))

        await self.page.wait_for_timeout(1000)

        await self.page.keyboard.press("Enter")
