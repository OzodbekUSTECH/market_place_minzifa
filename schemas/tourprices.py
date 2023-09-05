from pydantic import BaseModel, validator
from typing import Optional


class CreateTourPriceSchema(BaseModel):
    tour_id: int
    currency_id: int
    price: int
    discount_percentage: int = None
    new_price: int = None

    @validator('price', pre=True, always=True)
    def round_price(cls, value):
        return int(round(value))

class UpdateTourPriceSchema(CreateTourPriceSchema):
    pass

class TourPriceSchema(CreateTourPriceSchema):
    id: int
    currency_id: int
