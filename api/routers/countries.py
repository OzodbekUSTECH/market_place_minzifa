from typing import Annotated
from fastapi import APIRouter, Depends, Form, UploadFile, File
from services import countries_service
from repositories import Page
from schemas.countries import CreateCountrySchema, UpdateCountrySchema, CountrySchema
from schemas import IdResponseSchema
from utils.locale_handler import LocaleHandler
import json
from utils.exceptions import CustomExceptions
from database import UOWDependency

router = APIRouter(
    prefix="/countries",
    tags=["Countries (for tours)"],
)

# @router.post('/parser')
# async def parse_all_countries():
#     return await countries_service.parse_all_countries()

@router.post("", response_model=IdResponseSchema)
async def create_country(
    uow: UOWDependency,
    name: str = Form(),
    title: str = Form(),
    meta_description: str | None = Form(None),
    description: str | None = Form(None),
    photo: UploadFile = File(),
):
    """
    For example:
    - form data name: {"en": "string", "ru": "string"}
    - form data meta_description: {"en": "string", "ru": "string"}
    - form data description: {"en": "string", "ru": "string"}
    """
    try:
        name_dict = json.loads(name)
        title_dict = json.loads(title)
        
        meta_description_dict = json.loads(meta_description) if meta_description else None
        description_dict = json.loads(description) if description else None
    except:
        raise CustomExceptions.conflict("Invalid JSON format for title or description field, should be dict") 
    

    country_data = CreateCountrySchema(
        name = name_dict,
        title=title_dict,
        meta_description = meta_description_dict,
        description=description_dict,
        filename=photo
    )
    return await countries_service.create_country(uow, country_data)


@router.get("/{locale}", response_model=Page[CountrySchema])
@LocaleHandler.serialize_one_all_models_by_locale
async def get_list_of_countries(
    uow: UOWDependency,
    locale: Annotated[LocaleHandler, Depends()]
):
    return await countries_service.get_list_of_countries(uow)


@router.get("/{locale}/{id}", response_model=CountrySchema)
@LocaleHandler.serialize_one_all_models_by_locale
async def get_country_by_id(
    uow: UOWDependency, 
    locale: Annotated[LocaleHandler, Depends()], 
    id: int
):
    return await countries_service.get_country_by_id(uow,  id)


@router.put("/{id}", response_model=IdResponseSchema)
async def update_country(
    uow: UOWDependency,
    id: int,
    name: str = Form(),
    title: str = Form(),
    meta_description: str | None = Form(None),
    description: str | None = Form(None),
    photo: UploadFile = File(None),
):
    """
    For example:
    - form data name: {"en": "string", "ru": "string"}
    - form data meta_description: {"en": "string", "ru": "string"}
    - form data description: {"en": "string", "ru": "string"}
    """
    try:
        name_dict = json.loads(name)
        title_dict = json.loads(title)
        meta_description_dict = json.loads(meta_description) if meta_description else None
        description_dict = json.loads(description) if description else None
    except:
        raise CustomExceptions.conflict("Invalid JSON format for title or description field, should be dict") 
    

    country_data = UpdateCountrySchema(
        name = name_dict,
        title=title_dict,
        meta_description = meta_description_dict,
        description=description_dict,
        filename=photo
    )
    return await countries_service.update_country(uow, id, country_data)


@router.delete("/{id}", response_model=IdResponseSchema)
async def delete_country(uow: UOWDependency, id: int):
    return await countries_service.delete_country(uow, id)
