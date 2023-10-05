from schemas import CreateBaseModel, UpdateBaseModel, IdResponseSchema
from typing import Union


class CreateRegionSchema(CreateBaseModel):
    name: Union[dict[str, str], str]


class UpdateRegionSchema(CreateRegionSchema, UpdateBaseModel):
    pass


class RegionSchema(UpdateRegionSchema, IdResponseSchema):
    pass
