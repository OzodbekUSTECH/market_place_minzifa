from schemas import  CreateBaseModel, UpdateBaseModel, IdResponseSchema, TourMixinBaseModel
from typing import Union
from schemas.tours import CustomTypeSchema, CustomCountrySchema, CustomTourPriceSchema

class CustomTourSchema(IdResponseSchema):
    title: Union[dict[str, str], str]
    main_type: CustomTypeSchema
    prices: list[CustomTourPriceSchema]
    countries: list[CustomCountrySchema]


class CreateFavoriteTourSchema(CreateBaseModel):
    user_id: int
    tour_id: int

class FavoriteTourSchema(IdResponseSchema, CreateFavoriteTourSchema):
    tour: CustomTourSchema