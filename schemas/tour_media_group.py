from schemas import IdResponseSchema, TourMixinBaseModel

class TourMediaSchema(TourMixinBaseModel, IdResponseSchema):
    media_url: str