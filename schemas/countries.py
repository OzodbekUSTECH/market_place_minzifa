from schemas import CreateBaseModel, UpdateBaseModel, IdResponseSchema
from typing import Union


class CreateCountrySchema(CreateBaseModel):
    name: Union[dict[str, str], str]


class UpdateCountrySchema(CreateCountrySchema, UpdateBaseModel):
    pass


class CountrySchema(UpdateCountrySchema, IdResponseSchema):
    pass
