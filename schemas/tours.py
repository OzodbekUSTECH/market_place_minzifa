from pydantic import BaseModel, validator
from typing import Optional
from schemas.tourprices import TourPriceSchema, CreateTourPriceSchema

class CreateTourSchema(BaseModel):
    status_id: int
    name: str
    currency_id: str
    price: int

    @validator('price', pre=True, always=True)
    def round_price(cls, value):
        return int(round(value))
class CreatedTourSchemaResponse(CreateTourSchema):
    id: int

class UpdateTourSchema(CreateTourSchema):
    pass
    

class TourSchema(BaseModel):
    id: int
    status_id: int
    name: str
    prices: list[TourPriceSchema]
    