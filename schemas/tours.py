from pydantic import BaseModel
from typing import Optional
from schemas.tourprices import TourPriceSchema

class CreateTourSchema(BaseModel):
    status_id: int
    name: str

class UpdateTourSchema(CreateTourSchema):
    pass
    

class TourSchema(CreateTourSchema):
    id: int
    prices: list[TourPriceSchema]
    class ConfigDict:
        from_attributes = True