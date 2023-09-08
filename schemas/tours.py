from pydantic import BaseModel, validator
from typing import Optional, Union
from schemas.tourprices import TourPriceSchema
from datetime import date, datetime
class CreateTourSchema(BaseModel):
    status_id: int
    user_id: int
    start_date: date = None
    end_date: date = None
    title: Union[dict[str, str], str]
    description: Union[dict[str, str], str] 
    country: Union[dict[str, str], str]
    region: Union[dict[str, str], str]
    total_places: int
    free_places: int
    age_group: str
    children_age: str
    level_of_activity: Union[dict[str, str], str]

class CreatedTourResponseSchema(BaseModel):
    id: int
class UpdateTourSchema(CreateTourSchema):
    pass
    

class TourSchema(CreateTourSchema):
    id: int
    amount_comments: int
    amount_views: int
    created_at: datetime
    updated_at: datetime
    


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