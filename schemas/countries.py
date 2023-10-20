from schemas import CreateBaseModel, UpdateBaseModel, IdResponseSchema
from typing import Union
from pydantic import Field
from fastapi import UploadFile

class CreateCountrySchema(CreateBaseModel):
    name: Union[dict[str, str], str]
    title: Union[dict[str, str], str]
    meta_description: Union[dict[str, str], str, None]
    description: Union[dict[str, str], str, None]
    filename: UploadFile | None | str


class UpdateCountrySchema(UpdateBaseModel, CreateCountrySchema):
    pass



class CountrySchema(IdResponseSchema, UpdateCountrySchema):
    photo_url: str

    filename: str = Field(exclude=True)
