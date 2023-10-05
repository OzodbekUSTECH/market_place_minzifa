from schemas import  CreateBaseModel, UpdateBaseModel, IdResponseSchema
from typing import Union

class CreateActivitySchema(CreateBaseModel):
    name: Union[dict[str, str], str]


class UpdateActivitySchema(CreateActivitySchema, UpdateBaseModel):
    pass

class ActivitySchema(UpdateActivitySchema, IdResponseSchema):
    pass