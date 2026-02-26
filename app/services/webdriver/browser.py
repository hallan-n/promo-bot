from playwright.async_api import async_playwright
from services.logger import logger

class BrowserManager:
    _instance = None

    def __init__(self):
        self.playwright = None
        self.context = None

    @classmethod
    async def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
            await cls._instance._start()
        return cls._instance

    async def _start(self):
        self.playwright = await async_playwright().start()
        extension_1 = "./extensions/INSSIST"
        extension_2 = "./extensions/Revizap"

        extensions = f"{extension_1},{extension_2}"

        user_data_dir = "./profile"
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
            service_worker = await self.context.wait_for_event("serviceworker")
        else:
            service_worker = self.context.service_workers[0]

    async def new_page(self):
        return await self.context.new_page()

    @classmethod
    async def close(cls):
        """Fecha a instância singleton ativa e limpa a referência"""
        if cls._instance:
            instance = cls._instance
            try:
                if instance.context:
                    await instance.context.close()
                    instance.context = None
            except Exception as e:
                logger.error(f"⚠️ Erro ao fechar o contexto: {e}")
            finally:
                try:
                    if instance.playwright:
                        await instance.playwright.stop()
                        instance.playwright = None
                except Exception as e:
                    logger.error(f"⚠️ Erro ao parar o Playwright: {e}")
                cls._instance = None
