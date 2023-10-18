from schemas import  CreateBaseModel, UpdateBaseModel, IdResponseSchema, TourMixinBaseModel
from typing import Union

class CreateExcludeInPriceSchema(TourMixinBaseModel, CreateBaseModel):
    name: Union[dict[str, str], str]

class UpdateExcludeInPriceSchema(UpdateBaseModel, CreateExcludeInPriceSchema):
    pass

class ExcludeInPriceSchema(IdResponseSchema, UpdateExcludeInPriceSchema):
    pass