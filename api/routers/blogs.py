from typing import Annotated
from fastapi import APIRouter, Depends, Form, UploadFile, File
from services import blogs_service
from repositories import Page
import json
from schemas.blogs import (
    CreateBlogSchema,
    UpdateBlogSchema,
    BlogSchema,
)
from schemas import IdResponseSchema
from utils.exceptions import CustomExceptions
from utils.locale_handler import LocaleHandler

router = APIRouter(
    prefix="/blogs",
    tags=["Blogs"],
)


@router.post('', response_model=IdResponseSchema)
async def create_blog(
    title: str = Form(),
    meta_description: str = Form(),
    description: str = Form(),
    media: list[UploadFile] = File(),
    country_ids: str = Form()
):
    """
    For example:
    - form data title: {"en": "string", "ru": "string"}
    - form data meta_description: {"en": "string", "ru": "string"}
    - form data description: {"en": "string", "ru": "string"}
    - form data country_ids: 1, 2 and etc (with comma)
    """
    country_ids = [int(c_id) for c_id in country_ids.split(',')]
    
    try:
        title_dict = json.loads(title)
        meta_description_dict = json.loads(meta_description)
        description_dict = json.loads(description)
    except:
        raise CustomExceptions.conflict("Invalid JSON format for title or description field, should be dict") 
    
    blog_data = CreateBlogSchema(
        title=title_dict,
        meta_description=meta_description_dict,
        description=description_dict,
        media=media,
        country_ids=country_ids
    )
    return await blogs_service.create_blog(blog_data)

@router.post('/media/{id}')
async def create_media_for_blog(
    id: int,
    media: list[UploadFile] = File()
):
    """
    - params id: the id of the blog
    """
    return await blogs_service.create_media(id, media)


@router.get('', response_model=Page[BlogSchema])
@LocaleHandler.serialize_one_all_models_by_locale
async def get_list_of_blogs(
    locale: Annotated[LocaleHandler, Depends()]
):
    return await blogs_service.get_list_of_blogs()

@router.get('/{id}', response_model=BlogSchema)
@LocaleHandler.serialize_one_all_models_by_locale
async def get_blog_by_id(
    locale: Annotated[LocaleHandler, Depends()],
    id: int
):
    return await blogs_service.get_blog_by_id(id)

@router.put('/{id}', response_model=IdResponseSchema)
async def update_blog(
    id: int,
    title: str = Form(),
    meta_description: str = Form(),
    description: str = Form(),
    country_ids: str = Form()
):
    """
    For example:
    - form data title: {"en": "string", "ru": "string"}
    - form data meta_description: {"en": "string", "ru": "string"}
    - form data description: {"en": "string", "ru": "string"}
    - form data country_ids: 1, 2 and etc (with comma)
    """
    country_ids = [int(c_id) for c_id in country_ids.split(',')]
    
    try:
        title_dict = json.loads(title)
        meta_description_dict = json.loads(meta_description)
        description_dict = json.loads(description)
    except:
        raise CustomExceptions.conflict("Invalid JSON format for title or description field, should be dict") 
    
    blog_data = UpdateBlogSchema(
        title=title_dict,
        meta_description=meta_description_dict,
        description=description_dict,
        country_ids=country_ids
    )
    return await blogs_service.update_blog(id, blog_data)

@router.delete('/media/{id}', response_model=IdResponseSchema)
async def delete_media(
    id: int
):
    """
    - params id: the id of the media to be deleted
    """
    return await blogs_service.delete_media(id)


@router.delete('/{id}', response_model=IdResponseSchema)
async def delete_blog(
    id: int
):
    return await blogs_service.delete_blog(id)