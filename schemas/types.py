from schemas import CreateBaseModel, UpdateBaseModel, IdResponseSchema
from typing import Union
from fastapi import UploadFile
from pydantic import Field


class CreateTypeSchema(CreateBaseModel):
    filename: UploadFile | None | str
    name: Union[dict[str, str], str]
    description: Union[dict[str, str], str, None]
    meta_description: Union[dict[str, str], str, None]

class UpdateTypeSchema(UpdateBaseModel, CreateTypeSchema):
    pass

class TypeSchema(IdResponseSchema, UpdateTypeSchema):
    photo_url: str | None
    
    filename: str | None = Field(None, exclude=True)