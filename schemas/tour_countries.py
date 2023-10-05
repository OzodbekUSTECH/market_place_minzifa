from schemas import  CreateBaseModel, TourMixinBaseModel

class CreateTourCountrySchema(TourMixinBaseModel, CreateBaseModel):
    country_id: int

