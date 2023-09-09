from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import Optional
class CreateTourCommentSchema(BaseModel):
    user_id: int
    tour_id: int
    title: str
    comment_text: str
    rating: int

    @field_validator("rating")
    def validate_rating(cls, v):
        if v < 1 or v > 5:
            raise ValueError('Rating must be between 1 and 5')
        return v


class UpdateTourCommentSchema(CreateTourCommentSchema):
    updated_at: datetime = None

class TourCommentSchema(CreateTourCommentSchema):
    id: int
    updated_at: Optional[datetime]