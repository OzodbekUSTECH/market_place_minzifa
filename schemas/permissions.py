from pydantic import BaseModel, EmailStr, field_validator, constr
from security.permissionhandler import permissions_list
class CreatePermissionSchema(BaseModel):
    name: str
    endpoint: str

    @field_validator("endpoint")
    def validate_endpoint(cls, v):
        if v.lower() not in permissions_list:
            raise ValueError("Not allowed endpoint to be created")
        return v
    
class PermissionSchema(CreatePermissionSchema):
    id: int
    

    class ConfigDict:
        from_attributes = True
        


class UpdatePermissionSchema(CreatePermissionSchema):
    pass