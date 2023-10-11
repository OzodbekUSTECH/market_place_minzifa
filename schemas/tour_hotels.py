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


##########################
class CreateTourHotelSchema(TourMixinBaseModel, CreateBaseModel):
    name: Union[dict[str, str], str]
    

class UpdateTourHotelSchema(UpdateBaseModel, CreateTourHotelSchema):
    pass


class TourHotelSchema(IdResponseSchema, UpdateTourHotelSchema):
    media: list[TourHotelMediaGroup]
    