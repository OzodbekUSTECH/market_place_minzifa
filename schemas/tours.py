from pydantic import BaseModel
from typing import Optional
from schemas.tourprices import TourPriceSchema
from datetime import date
class CreateTourSchema(BaseModel):
    status_id: int
    user_id: int
    start_date: date = None
    end_date: date = None
    title: str

class UpdateTourSchema(CreateTourSchema):
    pass
    

class TourSchema(CreateTourSchema):
    id: int
    class ConfigDict:
        from_attributes = True


# from schemas.tourprices import TourPriceSchema, CreateTourPriceSchema
# from schemas.tourstatuses import TourStatusSchema
# from schemas.tour_activities import TourActivitySchema
# class TourSchemaDemoTest(BaseModel):
#     id: int
#     name: str
#     status: TourStatusSchema
#     prices: list[TourPriceSchema]
#     activities: list[TourActivitySchema]

# class CreateTourSchemaDemoTest(BaseModel):
#     name: str
#     currency_id: int
#     status_id: int
#     price: int
#     activities_ids: list[int]

#     @validator('price', pre=True, always=True)
#     def round_price(cls, value):
#         return int(round(value))