from typing import Union
from schemas import CreateBaseModel, UpdateBaseModel, IdResponseSchema


class CreateTourStatusSchema(CreateBaseModel):
    name: Union[dict[str, str], str]


class UpdateTourStatusSchema(UpdateBaseModel, CreateTourStatusSchema):
    pass


class TourStatusSchema(IdResponseSchema, UpdateTourStatusSchema):
    pass
