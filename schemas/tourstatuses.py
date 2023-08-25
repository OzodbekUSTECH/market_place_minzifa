from pydantic import BaseModel
from typing import Optional


class CreateTourStatusSchema(BaseModel):
    name: str

class UpdateTourStatusSchema(CreateTourStatusSchema):
    pass
    

class TourStatusSchema(CreateTourStatusSchema):
    id: int

   