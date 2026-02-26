from abc import ABC, abstractmethod
from models import Product



class BaseStore(ABC):
    @abstractmethod
    async def exec(self) -> list[Product]:
        pass


class BaseMessenger(ABC):
    @abstractmethod
    async def send_message(self):
        pass
