from pydantic import BaseModel, validator
from typing import Optional
from schemas.tourprices import TourPriceSchema, CreateTourPriceSchema
from schemas.tourstatuses import TourStatusSchema

class CreateTourSchema(BaseModel):
    name: str
    currency_id: int
    status_id: int
    price: int
    activities_ids: list[int]

    @validator('price', pre=True, always=True)
    def round_price(cls, value):
        return int(round(value))
class CreatedTourSchemaResponse(CreateTourSchema):
    id: int

class UpdateTourSchema(CreateTourSchema):
    pass
    

class TourSchema(BaseModel):
    id: int
    name: str
    status: TourStatusSchema
    prices: list[TourPriceSchema]
    