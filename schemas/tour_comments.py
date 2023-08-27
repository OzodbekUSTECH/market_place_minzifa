from pydantic import BaseModel

class CreateTourCommentSchema(BaseModel):
    user_id: int
    tour_id: int
    comment_text: str

class UpdateTourCommentSchema(CreateTourCommentSchema):
    pass

class TourCommentSchema(CreateTourCommentSchema):
    id: int