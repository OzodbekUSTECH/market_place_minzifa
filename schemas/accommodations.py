from schemas import  CreateBaseModel, UpdateBaseModel, IdResponseSchema
from typing import Union

class CreateAccommodationSchema(CreateBaseModel):
    name: Union[dict[str, str], str]

class UpdateAccommodationSchema(CreateAccommodationSchema, UpdateBaseModel):
    pass

class AccommodationSchema(UpdateAccommodationSchema, IdResponseSchema):
    pass