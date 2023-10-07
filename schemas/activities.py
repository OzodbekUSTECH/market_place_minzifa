from schemas import  CreateBaseModel, UpdateBaseModel, IdResponseSchema
from typing import Union

class CreateActivitySchema(CreateBaseModel):
    name: Union[dict[str, str], str]


class UpdateActivitySchema(UpdateBaseModel, CreateActivitySchema):
    pass

class ActivitySchema(IdResponseSchema, UpdateActivitySchema):
    pass