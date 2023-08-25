from pydantic import BaseModel
from typing import Optional


class CreateTourSchema(BaseModel):
    name: str

class UpdateTourSchema(CreateTourSchema):
    pass
    

class TourSchema(CreateTourSchema):
    id: int

    class ConfigDict:
        from_attributes = True