import asyncio
import os
import shutil
from datetime import datetime

from consts import END_HOUR, START_HOUR
from services.logger import logger


def format_brl(value: float) -> str:
    return f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def in_working_hours():
    now = datetime.now().hour
    return START_HOUR <= now < END_HOUR


async def wait_until_working_hours():
    while not in_working_hours:
        logger.info("⏳ Aguardando início do expediente...")
        await asyncio.sleep(60)


def clear_dir(path_dir: str):
    if os.path.exists(path_dir):
        shutil.rmtree(path_dir)
    os.makedirs(path_dir)


def create_dir(path_dir: str):
    os.makedirs(path_dir, exist_ok=True)
