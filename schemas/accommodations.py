from schemas import  CreateBaseModel, UpdateBaseModel, IdResponseSchema
from typing import Union

class CreateAccommodationSchema(CreateBaseModel):
    name: Union[dict[str, str], str]

class UpdateAccommodationSchema(UpdateBaseModel, CreateAccommodationSchema):
    pass

class AccommodationSchema(IdResponseSchema, UpdateAccommodationSchema):
    pass