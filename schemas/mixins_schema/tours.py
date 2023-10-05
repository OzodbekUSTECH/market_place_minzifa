from pydantic import BaseModel

class TourMixinBaseModel(BaseModel):
    tour_id: int