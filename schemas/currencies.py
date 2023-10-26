from schemas import CreateBaseModel, UpdateBaseModel, IdResponseSchema
from typing import Union

class CreateCurrencySchema(CreateBaseModel):
    name: str
    symbol: str
    exchange_rate: float | None

class UpdateCurrencySchema(UpdateBaseModel, CreateCurrencySchema):
    pass

class CurrencySchema(IdResponseSchema, UpdateCurrencySchema):
    pass