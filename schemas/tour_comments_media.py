from pydantic import BaseModel

class TourCommentMediaSchema(BaseModel):
    id: int
    tour_comment_id: int
    media_url: str