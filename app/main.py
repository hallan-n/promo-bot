import asyncio
# from bot.mercado_livre import run
from bot.amazon import run

if __name__ == "__main__":
    session = asyncio.run(run())