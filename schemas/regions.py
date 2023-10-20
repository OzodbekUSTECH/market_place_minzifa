from schemas import CreateBaseModel, UpdateBaseModel, IdResponseSchema
from typing import Union


class CreateRegionSchema(CreateBaseModel):
    name: Union[dict[str, str], str]
    country_id: int
    description: Union[dict[str, str], str, None]
    meta_description: Union[dict[str, str], str, None]

class UpdateRegionSchema(UpdateBaseModel, CreateRegionSchema):
    pass


class RegionSchema(IdResponseSchema, UpdateRegionSchema):
    pass
