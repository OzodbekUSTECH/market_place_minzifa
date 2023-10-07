from schemas import CreateBaseModel, UpdateBaseModel, IdResponseSchema
from typing import Union

class CreateTypeSchema(CreateBaseModel):
    name: Union[dict[str, str], str]

class UpdateTypeSchema(UpdateBaseModel, CreateTypeSchema):
    pass

class TypeSchema(IdResponseSchema, UpdateTypeSchema):
    pass