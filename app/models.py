import json
from dataclasses import asdict, dataclass
from datetime import datetime
from pydantic import BaseModel, Field

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


@dataclass
class Group(Base):
    name: str
    chat_id: str


class SubCategory(BaseModel):
    name: str = Field(examples=["Cuidados Automotivos"])
    code: str = Field(examples=["19701930011"])

class Category(BaseModel):
    name: str = Field(examples=["Automotivo"])
    code: str = Field(examples=["18914210011"])
    product_limit: int = Field(lt=99, examples=[30])
    min_discount: int = Field(gt=1, examples=[20])
    max_discount: int = Field(lt=100, examples=[60])
    sub_categories: list[SubCategory] = Field(examples=[[{"name": "Cuidados Automotivos", "code": "19701930011"}, {"name": "Cuidados com o Interior", "code": "19701933011"}]])

class Ingestion(BaseModel):
    id: str = Field(examples=["automoveis"])
    store_name: str = Field(examples=["amazon"])
    categories: list[Category]

