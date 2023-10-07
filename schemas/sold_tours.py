from schemas import  CreateBaseModel, UpdateBaseModel, IdResponseSchema
from pydantic import Field
from schemas.users import UserSchema

class CreateSoldTourSchema(CreateBaseModel):
    tour_id: int
    buyer_id: int
    seller_id: int
    price: int | float

class UpdateSoldTourSchema(UpdateBaseModel, CreateSoldTourSchema):
    pass

class SoldTourSchema(IdResponseSchema, UpdateSoldTourSchema):
    buyer: UserSchema
    seller: UserSchema
    
    buyer_id: int = Field(exclude=True)
    seller_id: int = Field(exclude=True)