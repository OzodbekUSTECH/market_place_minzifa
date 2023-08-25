from pydantic import BaseModel
from typing import Optional

class CreateTourPriceSchema(BaseModel):
    tour_id: int
    price: float

class UpdateTourPriceSchema(CreateTourPriceSchema):
    pass

class TourPriceSchema(CreateTourPriceSchema):
    id: int
    currency_id: int
