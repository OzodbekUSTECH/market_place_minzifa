from pydantic import BaseModel
from typing import Optional

class CreateTourPriceSchema(BaseModel):
    tour_id: int
    currency_id: int
    price: float

class UpdateTourPriceSchema(CreateTourPriceSchema):
    pass

class TourPriceSchema(CreateTourPriceSchema):
    id: int


class CreateTourSchema(BaseModel):
    name: str
    price: CreateTourPriceSchema

class UpdateTourSchema(CreateTourSchema):
    pass
    

class TourSchema(BaseModel):
    id: int
    name: str
    prices: list[TourPriceSchema]

    class ConfigDict:
        from_attributes = True