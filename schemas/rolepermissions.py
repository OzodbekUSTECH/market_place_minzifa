from pydantic import BaseModel, EmailStr, field_validator, constr


class CreateRolePermissionsSchema(BaseModel):
    role_id: int
    permission_id: int

    

class UpdateRolePermissionsSchema(CreateRolePermissionsSchema):
    pass

class DeleteRolePermissionsSchema(CreateRolePermissionsSchema):
    pass

class RolePermissionsSchema(CreateRolePermissionsSchema):
    id: int