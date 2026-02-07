import asyncio

from amazon import Amazon
from whatsapp import Whatsapp

asyncio.run(Whatsapp().exec())
