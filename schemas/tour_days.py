from schemas import  CreateBaseModel, TourMixinBaseModel, IdResponseSchema, UpdateBaseModel
from typing import Union
class CreateTourDaySchema(TourMixinBaseModel, CreateBaseModel):
    day: int
    name: Union[dict[str, str], str]
    description: Union[dict[str, str], str]

class UpdateTourDaySchema(UpdateBaseModel, CreateTourDaySchema):
    pass


class TourDaySchema(IdResponseSchema, UpdateTourDaySchema):
    pass