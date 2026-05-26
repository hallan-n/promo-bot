from logger import logger
from mongo import find_one, get_database, insert_one, update_one
from playwright.async_api import BrowserContext, Page


async def export_session(context: BrowserContext, provider: str):
    logger.info("Salvando sessão em banco")
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
    db = await get_database()
    sessions = db["sessions"]

    has_session = await find_one(sessions, {"provider": provider})

    if has_session:
        await update_one(
            sessions, has_session, {"provider": provider, "session": storage}
        )
        return

    await insert_one(sessions, has_session, {"provider": provider, "session": storage})

    logger.info(f"Sessão atualizada no banco")


async def inject_session(page: Page, provider: str):
    logger.info("Iniciando injeção de sessão")
    db = await get_database()
    sessions = db["sessions"]

    session = await find_one(sessions, {"provider": provider})
    data = session.get("session")

    if data.get("cookies"):
        await page.context.add_cookies(data["cookies"])

    for origin_data in data.get("origins", []):
        origin = origin_data["origin"]

        await page.goto(origin, wait_until="domcontentloaded")

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
