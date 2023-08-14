from pydantic import BaseModel, EmailStr, field_validator, constr
from typing import Optional

class TravelersSchema(BaseModel):
    id: int
    manager_id: int
    email: str
    company_name: Optional[str]
    phone_number: Optional[str]
    is_traveler_expert: bool
    is_traveler: bool
    role_id: int

    class ConfigDict:
        from_attributes = True

class ManagersSchema(BaseModel):
    id: int
    traveler_id: int
    email: str
    company_name: Optional[str]
    phone_number: Optional[str]
    role_id: int

    class ConfigDict:
        from_attributes = True


class CreateTravelerAndManagerSchema(BaseModel):
    traveler_id: int
    manager_id: int

class DeleteTravelerAndManagerSchema(CreateTravelerAndManagerSchema):
    ...

class UpdateTravelerAndManagerSchema(CreateTravelerAndManagerSchema):
    ...


class AssociationTravelAndManagerSchema(BaseModel):
    id: int
    traveler_id: int
    manager_id: int