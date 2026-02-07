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

            await page.wait_for_timeout(10000)
            lista_conversas = await page.query_selector(
                'div[aria-label="Lista de conversas"]'
            )

            await page.wait_for_timeout(1000)
            conversa_alan = await lista_conversas.query_selector(
                'div[role="row"]:has(span:text("Alan"))'
            )
            await page.wait_for_timeout(1000)
            await conversa_alan.click()
            await page.wait_for_timeout(1000)

            await page.add_init_script(
                f"""
                    () => {{
                        const html = "teste";
                        let chat = document.querySelector('div[aria-placeholder="Digite uma mensagem"]')
                        
                    }}
                """
            )

