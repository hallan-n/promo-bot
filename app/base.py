from playwright.async_api import Page
from models import Session
import json
from abc import abstractmethod


class WebDriver:
    async def get_session(self, page: Page) -> Session:
        state = await page.context.storage_state()
        cookies = await page.context.cookies()
        local_storage = await page.evaluate("() => JSON.stringify(window.localStorage)")
        session_storage = await page.evaluate(
            "() => JSON.stringify(window.sessionStorage)"
        )
        return Session(
            state=state,
            cookies=cookies,
            local_storage=json.loads(local_storage),
            session_storage=json.loads(session_storage),
        )

    async def inject_session(self, page: Page, path: str):
        with open(path, "r") as doc:
            session = Session(**json.loads(doc.read()))

        await page.add_init_script(
            f"""() => {{
                const data = {json.dumps(session.local_storage)};
                for (const [key, value] of Object.entries(data)) {{
                    localStorage.setItem(key, value);
                }}
            }}"""
        )

        await page.add_init_script(
            f"""() => {{
                const data = {json.dumps(session.session_storage)};
                for (const [key, value] of Object.entries(data)) {{
                    sessionStorage.setItem(key, value);
                }}
            }}"""
        )
        await page.context.clear_cookies()
        await page.context.add_cookies(session.cookies)

    @abstractmethod
    async def exec(self): ...
