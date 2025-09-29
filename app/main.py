import asyncio
from silver.mercadolivre import MercadolivreSilver

if __name__ == "__main__":
    mercadolivre = asyncio.run(MercadolivreSilver().exec())