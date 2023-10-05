from typing import Union
from schemas import CreateBaseModel, UpdateBaseModel, IdResponseSchema


class CreateTourStatusSchema(CreateBaseModel):
    name: Union[dict[str, str], str]


class UpdateTourStatusSchema(CreateTourStatusSchema, UpdateBaseModel):
    pass


class TourStatusSchema(UpdateTourStatusSchema, IdResponseSchema):
    pass
