from schemas import CreateBaseModel, TourMixinBaseModel

class CreateTourAccommodationSchema(TourMixinBaseModel, CreateBaseModel):

    accommodation_id: int

