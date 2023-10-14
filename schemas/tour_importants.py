from schemas import  CreateBaseModel, TourMixinBaseModel, IdResponseSchema, UpdateBaseModel
from typing import Union

class CreateTourImportantSchema(TourMixinBaseModel, CreateBaseModel):
    question: Union[dict[str, str], str]
    answer: Union[dict[str, str], str]

class UpdateTourImportantSchema(UpdateBaseModel, CreateTourImportantSchema):
    pass

class TourImportantSchema(IdResponseSchema, UpdateTourImportantSchema):
    pass