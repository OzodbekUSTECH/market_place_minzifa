from schemas import  CreateBaseModel, UpdateBaseModel, IdResponseSchema
from pydantic import Field
from typing import Union
from fastapi import UploadFile
from schemas.countries import CountrySchema
    
class CreateBlogMediaSchema(CreateBaseModel):
    blog_id: int
    filename: str

class BlogMediaSchema(IdResponseSchema, CreateBlogMediaSchema):
    filename: str = Field(exclude=True)
    media_url: str

################################################################
class CreateBlogSchema(CreateBaseModel):
    title: Union[dict[str, str], str]
    meta_description: Union[dict[str, str], str]
    description: Union[dict[str, str], str]
    media: list[UploadFile] = Field(None, exclude=True)
    country_ids: list[int] = Field(exclude=True)

class UpdateBlogSchema(UpdateBaseModel, CreateBlogSchema):
    pass

class BlogSchema(IdResponseSchema, UpdateBlogSchema):
    views: int
    media: list[BlogMediaSchema]
    countries: list[CountrySchema]