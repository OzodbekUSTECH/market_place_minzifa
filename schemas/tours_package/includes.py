from schemas import  CreateBaseModel, UpdateBaseModel, IdResponseSchema, TourMixinBaseModel
from typing import Union

class CreateMultipleIncludeInPrice(CreateBaseModel):
    name: Union[dict[str, str], str]


class CreateIncludeInPriceSchema(TourMixinBaseModel, CreateBaseModel):
    name: Union[dict[str, str], str]

class UpdateIncludeInPriceSchema(UpdateBaseModel, CreateIncludeInPriceSchema):
    pass

class IncludeInPriceSchema(IdResponseSchema, UpdateIncludeInPriceSchema):
    pass