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