import asyncio
from models import Product
from whatsapp import Whatsapp

async def main():
    zap = Whatsapp()

    await zap.start()
    await asyncio.sleep(1)

    await zap.send_message(
        "Alan",
        Product(
            name="bosta",
            original_price=100,
            price_discount=300,
            discount="30%",
            url="https://producoto.com",
            thumbnail="https://wallpapers.com/images/featured/imagens-incriveis-k287z98ruunquo28.jpg")
    )

    await asyncio.Event().wait()


asyncio.run(main())
