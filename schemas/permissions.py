from pydantic import BaseModel, EmailStr, field_validator, constr


class PermissionSchema(BaseModel):
    id: int
    name: str
    endpoint: str

    class ConfigDict:
        from_attributes = True
        
class CreatePermissionSchema(BaseModel):
    name: str
    endpoint: str

class UpdatePermissionSchema(CreatePermissionSchema):
    pass