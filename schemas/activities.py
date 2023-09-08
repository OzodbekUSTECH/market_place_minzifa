from pydantic import BaseModel, EmailStr, field_validator, constr
from typing import Union
class CreateActivitySchema(BaseModel):
    name: Union[dict[str, str], str]

class UpdateActivitySchema(CreateActivitySchema):
    pass

class ActivitySchema(CreateActivitySchema):
    id: int