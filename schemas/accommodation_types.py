from schemas import  CreateBaseModel, UpdateBaseModel, IdResponseSchema
from typing import Union


class CreateAccommodationTypeSchema(CreateBaseModel):
    name: Union[dict[str, str], str]

class UpdateAccommodationTypeSchema(UpdateBaseModel, CreateAccommodationTypeSchema):
    pass

class AccommodationTypeSchema(IdResponseSchema, UpdateAccommodationTypeSchema):
    pass