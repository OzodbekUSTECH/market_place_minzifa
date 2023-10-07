from schemas import  CreateBaseModel, UpdateBaseModel, IdResponseSchema
from typing import Union

class CreateTourChildrenAgeSchema(CreateBaseModel):
    name: Union[dict[str, str], str]

class UpdateTourChildrenAgeSchema(UpdateBaseModel, CreateTourChildrenAgeSchema):
    pass


class TourChildrenAgeSchema(IdResponseSchema, UpdateTourChildrenAgeSchema):
    pass