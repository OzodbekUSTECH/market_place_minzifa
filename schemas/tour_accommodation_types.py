from schemas import CreateBaseModel, TourMixinBaseModel

class CreateTourAccommodationTypeSchema(TourMixinBaseModel, CreateBaseModel):

    accommodation_type_id: int

