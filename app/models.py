
import json
from dataclasses import asdict, dataclass
from datetime import datetime

@dataclass
class Base:
    def dict(self):
        return asdict(self)

    def json(self):
        return json.dumps(asdict(self))


@dataclass
class Product(Base):
    name: str
    original_price: float
    price_discount: float
    discount: str
    url: str
    thumbnail: str
    fetched_at: str = datetime.now().isoformat()

@dataclass
class Session(Base):
    state: dict
    cookies: dict
    local_storage: dict
    session_storage: dict
