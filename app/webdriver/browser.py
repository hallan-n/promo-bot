from playwright.async_api import async_playwright


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

        self.context = await self.playwright.chromium.launch_persistent_context(
            user_data_dir="./profile", channel="chrome", headless=False
        )

    async def new_page(self):
        return await self.context.new_page()
