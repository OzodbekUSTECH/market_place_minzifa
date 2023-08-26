from pydantic import BaseModel, EmailStr, field_validator, constr

class CreateTourActivitySchema(BaseModel):
    tour_id: int
    activity_id: int

class UpdateTourActivitySchema(CreateTourActivitySchema):
    pass

class TourActivitySchema(CreateTourActivitySchema):
    id: int