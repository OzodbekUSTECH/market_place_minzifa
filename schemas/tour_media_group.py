from schemas import IdResponseSchema, TourMixinBaseModel, CreateBaseModel

class CreateTourMediaSchema(TourMixinBaseModel, CreateBaseModel):
    filename: str

class TourMediaSchema(TourMixinBaseModel, IdResponseSchema):
    media_url: str