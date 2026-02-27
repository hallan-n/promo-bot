from playwright.async_api import async_playwright
from services.logger import logger


class BrowserManagerSimple:

    def __init__(self, profile_dir=None):
        self.playwright = None
        self.context = None
        self.profile_dir = f"./profiles/{profile_dir}"

    async def start(self):
        await self._start()

    async def _start(self):
        self.playwright = await async_playwright().start()
        # extension_1 = "./extensions/INSSIST"
        extension_2 = "./extensions/Revizap"

        extensions = f"{extension_2}"

        user_data_dir = self.profile_dir if self.profile_dir else "./profile"
        self.context = await self.playwright.chromium.launch_persistent_context(
            user_data_dir,
            headless=False,
            channel="chromium",
            args=[
                f"--disable-extensions-except={extensions}",
                f"--load-extension={extensions}",
            ],
        )
        self.context.set_default_timeout(30000)

        if len(self.context.service_workers) == 0:
            await self.context.wait_for_event("serviceworker")
        else:
            _ = self.context.service_workers[0]

    async def new_page(self):
        return await self.context.new_page()

    async def close(self):
        try:
            if self.context:
                await self.context.close()
                self.context = None
        except Exception as e:
            logger.error(f"⚠️ Erro ao fechar o contexto: {e}")
        finally:
            try:
                if self.playwright:
                    await self.playwright.stop()
                    self.playwright = None
            except Exception as e:
                logger.error(f"⚠️ Erro ao parar o Playwright: {e}")