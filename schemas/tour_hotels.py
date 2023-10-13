from schemas import  CreateBaseModel, TourMixinBaseModel, IdResponseSchema, UpdateBaseModel
from typing import Union
from pydantic import Field
from schemas.regions import RegionSchema
from fastapi import UploadFile


class CreateTourHotelMediaGroup(CreateBaseModel):
    tour_hotel_id: int
    filename: str

class TourHotelMediaGroup(IdResponseSchema, CreateTourHotelMediaGroup):
    photo_url: str

    filename: str = Field(exclude=True)
##################################

class CreateTourHotelTypeSchema(CreateBaseModel):
    name: Union[dict[str, str], str]
    
class UpdateTourHotelTypeSchema(UpdateBaseModel, CreateTourHotelTypeSchema):
    pass

class TourHotelTypeSchema(IdResponseSchema, UpdateTourHotelTypeSchema):
    pass

##########################
class CreateTourHotelSchema(TourMixinBaseModel, CreateBaseModel):
    name: Union[dict[str, str], str]
    short_description: Union[dict[str, str], str, None]
    stars: int | None
    hotel_type_id: int

class UpdateTourHotelSchema(UpdateBaseModel, CreateTourHotelSchema):
    pass


class TourHotelSchema(IdResponseSchema, UpdateTourHotelSchema):
    media: list[TourHotelMediaGroup]
    hotel_type: TourHotelTypeSchema

    hotel_type_id: int = Field(exclude=True)
    
