from schemas import  CreateBaseModel, UpdateBaseModel, IdResponseSchema
from typing import Union

class CreateTourChildrenAgeSchema(CreateBaseModel):
    name: Union[dict[str, str], str]

class UpdateTourChildrenAgeSchema(CreateTourChildrenAgeSchema, UpdateBaseModel):
    pass


class TourChildrenAgeSchema(UpdateTourChildrenAgeSchema, IdResponseSchema):
    pass