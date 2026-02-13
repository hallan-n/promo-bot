import json
from dataclasses import asdict, dataclass, field
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
    payment_condition: str
    cupom: str
    discount: str
    url: str
    thumbnail: str
    fetched_at: str = datetime.now().isoformat()
