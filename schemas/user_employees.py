from schemas import CreateBaseModel, UpdateBaseModel, IdResponseSchema
from pydantic import Field, BaseModel
from schemas.users import CreateUserSchema

class CreateUserEmployeeSchema(CreateUserSchema):
    user_id: int = Field(exclude=True)

class CreateUserEmployeeAssociationSchema(BaseModel):
    user_id: int
    employee_id: int

