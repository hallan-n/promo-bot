from abc import ABC, abstractmethod

from models import Product


class Base(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    async def exec(self) -> list[Product]:
        pass
