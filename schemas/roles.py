from pydantic import BaseModel, EmailStr, field_validator, constr
from typing import Union


    

class CreateRoleSchema(BaseModel):
    name: Union[dict[str, str], str]

class UpdateRoleSchema(CreateRoleSchema):
    pass

class RoleSchema(CreateRoleSchema):
    id: int

class RolePermissionsSchema(BaseModel):
    id: int
    role_id: int
    name: str
    endpoint: str

    class ConfigDict:
        from_attributes = True
