from schemas import  CreateBaseModel, UpdateBaseModel, IdResponseSchema
from typing import Union


    

class CreateRoleSchema(CreateBaseModel):
    name: Union[dict[str, str], str]

class UpdateRoleSchema(UpdateBaseModel, CreateRoleSchema):
    pass

class RoleSchema(UpdateRoleSchema, IdResponseSchema):
    pass

