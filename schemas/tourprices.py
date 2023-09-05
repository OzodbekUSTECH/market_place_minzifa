from pydantic import BaseModel, validator
from typing import Optional


class CreateTourPriceSchema(BaseModel):
    tour_id: int
    currency_id: int
    price: float
    discount_percentage: float = 0
    new_price: float = 0

    
    
    
    
class UpdateTourPriceSchema(BaseModel):
    currency_id: int
    price: float
    discount_percentage: float = 0
    new_price: float = 0


class TourPriceSchema(CreateTourPriceSchema):
    id: int
    currency_id: int

    @validator('price', pre=True, always=True)
    def round_price(cls, value):
        return int(round(value))
    
    @validator('new_price', pre=True, always=True)
    def round_price(cls, value):
        return int(round(value))