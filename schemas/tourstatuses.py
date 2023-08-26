from pydantic import BaseModel, field_validator
from typing import Optional
from enum import Enum

class AllowedStatuses(Enum):
    PUBLISHED = "опубликован"
    ARCHIVED = "черновик"
    DELETED = "удален"
    OUTDATED = "прошли даты"
    CHECKING = "на модерации"
    UNPUBLISHED = "Снято с публикации"
    
allowed_statuses_list = [status.value.lower().replace(" ", "") for status in AllowedStatuses]

class CreateTourStatusSchema(BaseModel):
    name: str

    @field_validator("name")
    def validate_name(cls, v):
        if v.lower().replace(" ", "") not in allowed_statuses_list:
            raise ValueError("This status is not allowed to be created")
        return v


class UpdateTourStatusSchema(CreateTourStatusSchema):
    pass
    

class TourStatusSchema(CreateTourStatusSchema):
    id: int

   