from schemas import CreateBaseModel, UpdateBaseModel, IdResponseSchema
from typing import Union

class CreateCurrencySchema(CreateBaseModel):
    name: Union[dict[str, str], str]
    symbol: str
    exchange_rate: float | None

class UpdateCurrencySchema(CreateCurrencySchema, UpdateBaseModel):
    pass

class CurrencySchema(UpdateCurrencySchema, IdResponseSchema):
    pass