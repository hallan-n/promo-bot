import asyncio
from bronze.amazon import AmazonBronze
from bronze.mercadolivre import MercadolivreBronze

if __name__ == "__main__":
    amazon = AmazonBronze()
    mercadolivre = MercadolivreBronze()
    amazon = asyncio.run(amazon.exec())
    # mercadolivre = asyncio.run(mercadolivre.exec())