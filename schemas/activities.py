from pydantic import BaseModel, EmailStr, field_validator, constr

class CreateActivitySchema(BaseModel):
    name: str

class UpdateActivitySchema(CreateActivitySchema):
    pass

class ActivitySchema(CreateActivitySchema):
    id: int