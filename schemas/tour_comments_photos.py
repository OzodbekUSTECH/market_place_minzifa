from pydantic import BaseModel

class TourCommentPhotoSchema(BaseModel):
    id: int
    tour_comment_id: int
    photo_url: str