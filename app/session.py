import json
from pathlib import Path

from logger import logger
from playwright.async_api import BrowserContext, Page


async def export_session(context: BrowserContext, file_path: str = "session.json"):
    logger.info("Iniciando exportação da sessão")
    pages = context.pages

    storage = {
        "cookies": await context.cookies(),
        "origins": [],
    }

    for page in pages:
        origin = page.url.split("/", 3)

        if len(origin) < 3:
            continue

        origin = f"{origin[0]}//{origin[2]}"

        data = await page.evaluate(
            """
            () => {
                const localStorageData = {}
                const sessionStorageData = {}

                for (let i = 0; i < localStorage.length; i++) {
                    const key = localStorage.key(i)
                    localStorageData[key] = localStorage.getItem(key)
                }

                for (let i = 0; i < sessionStorage.length; i++) {
                    const key = sessionStorage.key(i)
                    sessionStorageData[key] = sessionStorage.getItem(key)
                }

                return {
                    localStorage: localStorageData,
                    sessionStorage: sessionStorageData
                }
            }
            """
        )

        storage["origins"].append(
            {
                "origin": origin,
                "localStorage": data["localStorage"],
                "sessionStorage": data["sessionStorage"],
            }
        )

    Path(file_path).write_text(
        json.dumps(storage, indent=4, ensure_ascii=False),
        encoding="utf-8",
    )
    logger.info(f"Sessão exportada para o path {file_path}")


async def inject_session(
    page: Page,
    file_path: str = "session.json",
):
    logger.info("Iniciando injeção de sessão")
    data = json.loads(Path(file_path).read_text(encoding="utf-8"))

    if data.get("cookies"):
        await page.context.add_cookies(data["cookies"])

    for origin_data in data.get("origins", []):
        origin = origin_data["origin"]

        await page.goto(origin)

        await page.evaluate(
            """
            ({ localStorageData, sessionStorageData }) => {

                for (const [key, value] of Object.entries(localStorageData)) {
                    localStorage.setItem(key, value)
                }

                for (const [key, value] of Object.entries(sessionStorageData)) {
                    sessionStorage.setItem(key, value)
                }
            }
            """,
            {
                "localStorageData": origin_data.get("localStorage", {}),
                "sessionStorageData": origin_data.get("sessionStorage", {}),
            },
        )

    logger.info("Sessão injetada com sucesso")
