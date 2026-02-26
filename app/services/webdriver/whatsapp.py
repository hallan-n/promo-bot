from services.webdriver.base import BaseMessenger
from models import Product
from services.logger import logger
from utils import format_brl
from services.webdriver.browser import BrowserManager
import asyncio
from playwright.async_api import TimeoutError


class Whatsapp(BaseMessenger):
    def __init__(self):
        self.page = None

    async def start(self, tab: str = None):
        browser = await BrowserManager.get_instance()
        self.page = await browser.new_page()
        await self.page.goto("https://web.whatsapp.com/")
        if tab == "chat":
            asyncio.create_task(self.auto_click_ok())
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

    async def choose_chat(self, chat_name: str):
        message_list = await self.page.query_selector(
            'div[aria-label="Lista de conversas"]'
        )
        chat = await message_list.query_selector(
            f'div[role="row"]:has(span:text("{chat_name}"))'
        )
        await chat.click()
        await self.page.wait_for_timeout(200)

    async def extra_contacts(self, group_name) -> list:
        await self.choose_chat(group_name)
        await self.page.click("#main > header")
        button = self.page.locator('div[role="button"]', has_text="Ver tudo")
        await button.wait_for(state="visible")
        await button.first.click()

        scroll_containers = await self.page.query_selector_all(
            'div[aria-label="Pesquisar membros"] div.copyable-area > div'
        )

        if not scroll_containers:
            return

        scroll_container = scroll_containers[-1]

        if not scroll_containers:
            return

        previous = -1
        numbers = set()

        while True:
            current = await scroll_container.evaluate("el => el.scrollTop")

            if current == previous:
                break

            previous = current

            await scroll_container.evaluate("""
                el => el.scrollBy(0, el.clientHeight)
            """)

            spans = await scroll_container.query_selector_all(
                'div[role="listitem"] span[title^="+"]'
            )

            for span in spans:
                number = await span.inner_text()
                numbers.add(number)

        await self.page.click('button[aria-label="Fechar"]')
        return list(numbers)

    async def auto_click_ok(self):
        while True:
            try:
                button = self.page.locator('button:has-text("OK")')
                await button.wait_for(state="visible", timeout=2000)
                await button.click()
                logger.info("Botão OK clicado")
            except TimeoutError:
                pass  # não apareceu ainda

            await asyncio.sleep(1)  # evita loop muito agressivo

    async def send_chat(self, number: str, message: str, image_path: str = None):
        await self.page.click('button[aria-label="Conversas"]')

        await self.page.click('button[aria-label="Nova conversa"]')

        await self.page.fill('input[aria-label="Pesquisar nome ou número"]', number)

        await self.page.click('div.copyable-area div[role="button"]')

        if image_path:
            await self.page.click('button[aria-label="Anexar"]')

            await self.page.wait_for_timeout(1000)

            async with self.page.expect_file_chooser() as fc:
                await self.page.get_by_label("Fotos e vídeos").click()

            file_chooser = await fc.value
            await file_chooser.set_files(image_path)
            await self.page.wait_for_timeout(500)

        box = self.page.locator(
            'div[contenteditable="true"][aria-placeholder="Digite uma mensagem"]'
        ).first

        if not box:
            logger.error(f"❌ Erro ao enviar a mensagem")
            await self.page.reload()
            await self.page.wait_for_timeout(1000)
            return

        await self.page.wait_for_timeout(500)

        await box.click()

        await box.fill(message)

        await self.page.keyboard.press("Enter")

        await self.page.click('button[aria-label="Conversas"]')

        await self.page.wait_for_timeout(300)

        await self.page.keyboard.press("Escape")

    async def send_message(self, group_name, product: Product):

        await self.choose_chat(group_name)

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

        if not box:
            logger.error(f"❌ Erro ao enviar a mensagem")
            await self.page.reload()
            await self.page.wait_for_timeout(1000)
            return

        await self.page.wait_for_timeout(1000)

        await box.click()

        await self.page.wait_for_timeout(1000)

        await box.fill(self.get_template_message(product))

        await self.page.wait_for_timeout(1000)

        await self.page.keyboard.press("Enter")
