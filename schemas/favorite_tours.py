from pydantic import BaseModel, EmailStr
from typing import Optional

class CreateFavoriteTourSchema(BaseModel):
    user_id: int
    tour_id: int

class UpdateFavoriteTourSchema(CreateFavoriteTourSchema):
    pass

class FavoriteTourSchema(CreateFavoriteTourSchema):
    id: int