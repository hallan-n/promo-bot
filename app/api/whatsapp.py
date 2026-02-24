

import httpx
import asyncio
from base import BaseMessenger
from models import Product
from utils import format_brl


class Whatsapp(BaseMessenger):
    def __init__(self):
        timeout = httpx.Timeout(20.0)
        limits = httpx.Limits(max_connections=20, max_keepalive_connections=10)
        self.client = httpx.AsyncClient(timeout=timeout, limits=limits)

    def get_template_message(self, product: Product) -> str:
        lines = [
            f"🦊 {product.name}\n",
            f"~de R$ {format_brl(product.original_price)}~",
            f"*por R$ {format_brl(product.price_discount)} 😱😱*\n",
        ]

        if product.payment_condition:
            lines.append(f"💳 {product.payment_condition}")

        if product.cupom:
            lines.append(f"🎟️ Use o cupom: {product.cupom}")

        if product.payment_condition or product.cupom:
            lines.append("")

        if product.url:
            lines.append(product.url)

        return "\n".join(lines)



    async def send_message(self, chat_id, product: Product):
        url = "http://localhost:3000/send"
        caption = self.get_template_message(product)

        for attempt in range(3):
            try:

                thumbnail_response = await self.client.get(product.thumbnail)
                image_bytes = thumbnail_response.read()
                data = {
                    "number": chat_id,
                    "text": caption
                }
                files = {
                    "image": ("image.jpg", image_bytes, "image/jpg")
                }

                response = await self.client.post(url, data=data, files=files)

                print(response.status_code)
                print(response.json())

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
