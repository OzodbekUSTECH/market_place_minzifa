from pydantic import BaseModel, validator
from typing import Optional


class CreateTourPriceSchema(BaseModel):
    tour_id: int
    currency_id: int
    price: int
    discount_percentage: Optional[float] = None
    new_price: Optional[float] = None

    
    
    
class UpdateTourPriceSchema(CreateTourPriceSchema):
    pass


class TourPriceSchema(CreateTourPriceSchema):
    id: int
    
    @validator('new_price')
    def round_new_price(cls, value):
        if value is not None:
            return round(value)
    
    @validator('discount_percentage')
    def round_discount(cls, value):
        if value is not None:
            return round(value)
    
    # @validator('price', pre=True, always=True)
    # def round_price(cls, value):
    #     return round(value)
    
    
    