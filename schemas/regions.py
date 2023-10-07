from schemas import CreateBaseModel, UpdateBaseModel, IdResponseSchema
from typing import Union


class CreateRegionSchema(CreateBaseModel):
    name: Union[dict[str, str], str]


class UpdateRegionSchema(UpdateBaseModel, CreateRegionSchema):
    pass


class RegionSchema(IdResponseSchema, UpdateRegionSchema):
    pass
