from pydantic import BaseModel, EmailStr, field_validator, constr


class RolePermissionsSchema(BaseModel):
    role_id: int
    permission_id: int

    

class CreateRolePermissionsSchema(RolePermissionsSchema):
    pass

class DeleteRolePermissionsSchema(RolePermissionsSchema):
    pass