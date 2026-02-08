from playwright.async_api import async_playwright
from playwright_stealth import Stealth


class Whatsapp:
    async def exec(self):
        async with Stealth(navigator_languages_override=("pt-BR")).use_async(
            async_playwright()
        ) as p:
            context = await p.chromium.launch_persistent_context(
                user_data_dir="./profile", channel="chrome", headless=False
            )

            page = context.pages[0]
            await page.goto("https://web.whatsapp.com/")

            await page.wait_for_selector('div:has-text("Protegida com a criptografia de ponta a ponta")', state="detached")

            await page.wait_for_timeout(2000)

            lista_conversas = await page.query_selector('div[aria-label="Lista de conversas"]')

            await page.wait_for_timeout(1000)

            conversa_alan = await lista_conversas.query_selector('div[role="row"]:has(span:text("Alan"))')

            await page.wait_for_timeout(1000)

            await conversa_alan.click()

            await page.wait_for_timeout(1000)

            await page.click('button[aria-label="Anexar"]')

            await page.wait_for_timeout(1000)

            async with page.expect_file_chooser() as fc:
                await page.get_by_label("Fotos e vídeos").click()

            file_chooser = await fc.value
            await file_chooser.set_files("/home/neves/Documentos/promo-bot/1.png")


            box = page.locator('div[contenteditable="true"][aria-label="Digite uma mensagem"]')

            await page.wait_for_timeout(1000)

            await box.click()

            await page.wait_for_timeout(1000)

            await box.fill(
"""🧜🏻‍♀️ Notebook Gamer Acer Nitro V15 Core I5 512gb 8gb Linux+ubook

~de R$ 4.699~
por R$ 3.819,00 😱😱

💳 ou 10x de R$ 381,90
🎟️ Aplique o cupom de R$300 OFF abaixo do preço

https://mercadolivre.com/sec/1juisjF""")


            
            await page.wait_for_timeout(1000)

            await page.keyboard.press("Enter")
            breakpoint()