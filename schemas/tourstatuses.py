from pydantic import BaseModel, field_validator
from typing import Optional, Union
from enum import Enum



class CreateTourStatusSchema(BaseModel):
    name: Union[dict[str, str], str]

    


class UpdateTourStatusSchema(CreateTourStatusSchema):
    pass
    

class TourStatusSchema(CreateTourStatusSchema):
    id: int

   