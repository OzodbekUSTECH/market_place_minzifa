from pydantic import BaseModel
from typing import Optional
from schemas.tourprices import TourPriceSchema
from schemas.tour_activities import TourActivitySchema
from schemas.tourstatuses import TourStatusSchema

class CreateTourSchema(BaseModel):
    status_id: int
    name: str

class CreatedTourSchemaResponse(CreateTourSchema):
    id: int

class UpdateTourSchema(CreateTourSchema):
    pass
    

class TourSchema(CreateTourSchema):
    id: int
    prices: list[TourPriceSchema]
    activities: list[TourActivitySchema]
    status: TourStatusSchema
   