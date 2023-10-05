from schemas import  CreateBaseModel, UpdateBaseModel, IdResponseSchema
from typing import Union

class CreateTourActivityLevelSchema(CreateBaseModel):
    name: Union[dict[str, str], str]
    level_number: int

class UpdateTourActivityLevelSchema(CreateTourActivityLevelSchema, UpdateBaseModel):
    pass

class TourActivityLevelSchema(UpdateTourActivityLevelSchema, IdResponseSchema):
    pass