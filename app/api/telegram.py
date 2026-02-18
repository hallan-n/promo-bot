import httpx
from base import BaseMessenger
from models import Product
from utils import format_brl
from consts import TOKEN_TELEGRAM

class Telegram(BaseMessenger):

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
        async with httpx.AsyncClient() as client:
            caption = self.get_template_message(product)

            await client.post(
                f"https://api.telegram.org/bot{TOKEN_TELEGRAM}/sendPhoto",
                json={
                    "chat_id": channel_id,
                    "parse_mode": "HTML",
                    "photo": product.thumbnail,
                    "caption": caption,
                },
            )
