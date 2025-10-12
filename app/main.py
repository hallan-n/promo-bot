import asyncio
from stores.amazon import Amazon
from stores.mercadolivre import Mercadolivre

if __name__ == "__main__":
    asyncio.run(Mercadolivre().exec())
    # print(mercadolivre)
    # amazon = asyncio.run(Amazon().exec())
    # print(amazon)