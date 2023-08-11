from pydantic import BaseModel, EmailStr, field_validator, constr

class RoleSchema(BaseModel):
    id: int
    name: str

    class ConfigDict:
        from_attributes = True

class CreateRoleSchema(BaseModel):
    name: str

class UpdateRoleSchema(CreateRoleSchema):
    pass

class RolePermissionsSchema(BaseModel):
    id: int
    role_id: int
    name: str
    endpoint: str

    class ConfigDict:
        from_attributes = True
