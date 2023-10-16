from schemas import CreateBaseModel, UpdateBaseModel, IdResponseSchema
from pydantic import EmailStr, Field, BaseModel

class CustomTourSchema(BaseModel):
    id: int
    title: str

class CustomUserSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
##############################################
class CreateOrderSchema(CreateBaseModel):
    tour_id: int
    user_id: int | None
    name: str | None
    email: EmailStr | None
    phone_number: str | None
    start_date: str | None
    end_date: str | None
    amount_of_participants: int = Field(ge=1)
    is_private_request: bool
    wishes: str | None

class UpdateOrderSchema(UpdateBaseModel, CreateOrderSchema):
    pass

class OrderSchema(IdResponseSchema, UpdateOrderSchema):
    user: CustomUserSchema | None
    tour: CustomTourSchema

    user_id: int | None = Field(exclude=True)
    tour_id: int = Field(exclude=True)