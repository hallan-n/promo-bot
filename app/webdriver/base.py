from abc import ABC, abstractmethod

from models import Product


class Base(ABC):

    @abstractmethod
    async def exec(self) -> list[Product]:
        pass
