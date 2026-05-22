import json
from dataclasses import asdict, dataclass
from datetime import datetime


@dataclass
class Base:
    def dict(self):
        return asdict(self)

    def json(self):
        return json.dumps(asdict(self))


def to_brl(value: float) -> str:
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


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


def to_list_dict(products: list[Product]):
    return [p.dict() for p in products]