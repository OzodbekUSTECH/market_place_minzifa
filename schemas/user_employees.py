from schemas import CreateBaseModel, UpdateBaseModel, IdResponseSchema
from pydantic import Field, BaseModel
from schemas.users import CreateUserSchema

class CreateEmployeeSchema(CreateUserSchema):
    travel_expert_id: int = Field(exclude=True)

class CreateEmployeeAssociationSchema(BaseModel):
    travel_expert_id: int
    employee_id: int

class EmployeeSchema(IdResponseSchema, CreateEmployeeAssociationSchema):
    ...

