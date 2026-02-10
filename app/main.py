import asyncio

from amazon import Amazon
from category import AmazonCategory

from models import Product
from whatsapp import Whatsapp


async def ingestion():

    beleza = Amazon(AmazonCategory.BELEZA.value, 10)
    casa = Amazon(AmazonCategory.CASA.value, 10)
    games = Amazon(AmazonCategory.GAMES_E_CONSOLES.value, 10)

    products_beleza = await beleza.exec()
    products_casa = await casa.exec()
    products_games = await games.exec()
    

    await asyncio.Event().wait()


asyncio.run(ingestion())
