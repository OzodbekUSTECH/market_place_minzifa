from pydantic import BaseModel
from typing import Optional

class CreateCurrencySchema(BaseModel):
    name: str
    symbol: str
    exchange_rate: float

class UpdateCurrencySchema(CreateCurrencySchema):
    pass

class CurrencySchema(CreateCurrencySchema):
    id: int