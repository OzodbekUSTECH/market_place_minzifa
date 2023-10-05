from schemas import CreateBaseModel, TourMixinBaseModel

class CreateTourLanguageSchema(TourMixinBaseModel, CreateBaseModel):
    language_id: int
