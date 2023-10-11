from schemas import  CreateBaseModel, TourMixinBaseModel, IdResponseSchema, UpdateBaseModel
from typing import Union
from pydantic import Field
from schemas.regions import RegionSchema
from fastapi import UploadFile


class CreateTourDayMediaGroup(CreateBaseModel):
    tour_day_id: int
    filename: str

class TourDayMediaGroup(IdResponseSchema, CreateTourDayMediaGroup):
    photo_url: str

    filename: str = Field(exclude=True)


##########################
class CreateTourDaySchema(TourMixinBaseModel, CreateBaseModel):
    day: int
    name: Union[dict[str, str], str]
    description: Union[dict[str, str], str]
    region_id: int

class UpdateTourDaySchema(UpdateBaseModel, CreateTourDaySchema):
    pass


class TourDaySchema(IdResponseSchema, UpdateTourDaySchema):
    region: RegionSchema
    media: list[TourDayMediaGroup]

    region_id: int = Field(exclude=True)