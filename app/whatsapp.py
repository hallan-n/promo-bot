# from playwright.async_api import async_playwright
# from playwright_stealth import Stealth


# class Whatsapp:
#     async def exec(self):
#         async with Stealth(navigator_languages_override=("pt-BR")).use_async(
#             async_playwright()
#         ) as p:
#             context = await p.chromium.launch_persistent_context(
#                 user_data_dir="./profile", channel="chrome", headless=False
#             )

#             page = context.pages[0]
#             await page.goto("https://web.whatsapp.com/")

#             await page.wait_for_selector('div:has-text("Protegida com a criptografia de ponta a ponta")', state="detached")

#             await page.wait_for_timeout(2000)

#             lista_conversas = await page.query_selector('div[aria-label="Lista de conversas"]')

#             await page.wait_for_timeout(1000)

#             conversa_alan = await lista_conversas.query_selector('div[role="row"]:has(span:text("Alan"))')

#             await page.wait_for_timeout(1000)

#             await conversa_alan.click()

#             await page.wait_for_timeout(1000)

#             await page.click('button[aria-label="Anexar"]')

#             await page.wait_for_timeout(1000)

#             async with page.expect_file_chooser() as fc:
#                 await page.get_by_label("Fotos e vídeos").click()

#             file_chooser = await fc.value
#             await file_chooser.set_files("/home/neves/Documentos/promo-bot/1.webp")


#             box = page.locator('div[contenteditable="true"][aria-label="Digite uma mensagem"]')

#             await page.wait_for_timeout(1000)

#             await box.click()

#             await page.wait_for_timeout(1000)

#             await box.fill(
# """🧜🏻‍♀️ Notebook Gamer Acer Nitro V15 Core I5 512gb 8gb Linux+ubook

# ~de R$ 4.699~
# por R$ 3.819,00 😱😱

# 💳 ou 10x de R$ 381,90
# 🎟️ Aplique o cupom de R$300 OFF abaixo do preço

# https://mercadolivre.com/sec/1juisjF""")


#             await page.wait_for_timeout(1000)

#             await page.keyboard.press("Enter")

#             await page.wait_for_timeout(1000)

#             breakpoint()


from browser import BrowserManager
from models import Product
from playwright.async_api import async_playwright
from playwright_stealth import Stealth


class Whatsapp:
    def __init__(self):
        self.playwright = None
        self.context = None
        self.page = None

    async def start(self):
        browser = await BrowserManager.get_instance()
        self.page = await browser.new_page()
        await self.page.goto("https://web.whatsapp.com/")
        await self.page.wait_for_selector(
            'div:has-text("Protegida com a criptografia de ponta a ponta")',
            state="detached",
        )

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

        with open("./product.jpg", "wb") as f:
            f.write(content)

        await self.page.click('button[aria-label="Anexar"]')

        await self.page.wait_for_timeout(1000)

        async with self.page.expect_file_chooser() as fc:
            await self.page.get_by_label("Fotos e vídeos").click()

        file_chooser = await fc.value
        await file_chooser.set_files("./product.jpg")

        box = self.page.locator(
            'div[contenteditable="true"][aria-placeholder="Digite uma mensagem"]'
        ).first

        await self.page.wait_for_timeout(1000)

        await box.click()

        await self.page.wait_for_timeout(1000)

        await box.fill(f"""🧜🏻‍♀️ {product.name}

~de R$ {product.original_price}~
por * R$ {product.price_discount} 😱😱 *

🎟️ {product.discount}

{product.url}""")

        await self.page.wait_for_timeout(1000)

        await self.page.keyboard.press("Enter")

    async def close(self):
        await self.context.close()
        await self.playwright.stop()
