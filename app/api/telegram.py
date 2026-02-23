import asyncio

import httpx
from base import BaseMessenger
from consts import TOKEN_TELEGRAM
from models import Product
from utils import format_brl


class Telegram(BaseMessenger):
    def __init__(self):
        timeout = httpx.Timeout(20.0)
        limits = httpx.Limits(max_connections=20, max_keepalive_connections=10)
        self.client = httpx.AsyncClient(timeout=timeout, limits=limits)

    def get_template_message(self, product: Product) -> str:
        lines = [
            f"<b>🦊 {product.name}</b>\n",
            f"<s>de R$ {format_brl(product.original_price)}</s>",
            f"<b>por R$ {format_brl(product.price_discount)} 😱😱</b>\n",
        ]

        if product.payment_condition:
            lines.append(f"💳 {product.payment_condition}")

        if product.cupom:
            lines.append(f"🎟️ <b>Use o cupom: {product.cupom}</b>")

        if product.payment_condition or product.cupom:
            lines.append("")

        if product.url:
            lines.append(f'👉 <a href="{product.url}">{product.url}</a>')

        return "\n".join(lines)

    async def send_message(self, channel_id, product: Product):
        caption = self.get_template_message(product)

        for attempt in range(3):
            try:
                response = await self.client.post(
                    f"https://api.telegram.org/bot{TOKEN_TELEGRAM}/sendPhoto",
                    json={
                        "chat_id": channel_id,
                        "parse_mode": "HTML",
                        "photo": product.thumbnail,
                        "caption": caption,
                    },
                )
                response.raise_for_status()
                return
            except httpx.HTTPStatusError as e:
                if e.response.status_code == 429:
                    retry_after = (
                        e.response.json().get("parameters", {}).get("retry_after", 5)
                    )
                    await asyncio.sleep(int(retry_after))
                    continue
                if 500 <= e.response.status_code < 600:
                    await asyncio.sleep(2**attempt)
                    continue
                raise
            except httpx.ReadTimeout:
                await asyncio.sleep(2**attempt)

        raise RuntimeError("Failed to send message after retries")

    async def close(self):
        await self.client.aclose()
