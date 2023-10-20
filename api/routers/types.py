from typing import Annotated
from fastapi import APIRouter, Depends, Form, UploadFile, File
from services import types_service
from repositories import Page
from schemas.types import CreateTypeSchema, UpdateTypeSchema, TypeSchema
from schemas import IdResponseSchema
from utils.locale_handler import LocaleHandler
from database import UOWDependency
import json
from utils.exceptions import CustomExceptions


router = APIRouter(
    prefix="/types",
    tags=["Types (for tours)"],
)


@router.post("", response_model=IdResponseSchema)
async def create_type(
    uow: UOWDependency,
    name: str = Form(),
    description: str | None = Form(None),
    meta_description: str | None = Form(None),
    photo: UploadFile  = File(None)

):
    """
    - name: dict[str, str]\n
    for example:\n
    name: {\n
        "ru": "Осмотр достопримечательностей",\n
        "en": "Sightseeing"\n
    }
    """
    try:
        name_dict = json.loads(name)
        
        meta_description_dict = json.loads(meta_description) if meta_description else None
        description_dict = json.loads(description) if description else None
    except:
        raise CustomExceptions.conflict("Invalid JSON format for title or description field, should be dict") 
    
    type_data = CreateTypeSchema(
        name=name_dict,
        description=description_dict,
        meta_description=meta_description_dict,
        filename=photo
    )
    return await types_service.create_type(uow, type_data)


@router.get("/{locale}", response_model=Page[TypeSchema])
@LocaleHandler.serialize_one_all_models_by_locale
async def get_list_of_types(uow: UOWDependency, locale: Annotated[LocaleHandler, Depends()]):
    return await types_service.get_list_of_types(uow)


@router.get("/{locale}/{id}", response_model=TypeSchema)
async def get_type_by_id(uow: UOWDependency,locale: Annotated[LocaleHandler, Depends()], id: int):
    return await types_service.get_type_by_id(uow, id)


@router.put("/{id}", response_model=IdResponseSchema)
async def update_type(
    uow: UOWDependency,
    id: int,
    name: str = Form(),
    description: str | None = Form(None),
    meta_description: str | None = Form(None),
    photo: UploadFile  = File(None)

):
    """
    - name: dict[str, str]\n
    for example:\n
    name: {\n
        "ru": "Осмотр достопримечательностей",\n
        "en": "Sightseeing"\n
    }
    """
    try:
        name_dict = json.loads(name)
        
        meta_description_dict = json.loads(meta_description) if meta_description else None
        description_dict = json.loads(description) if description else None
    except:
        raise CustomExceptions.conflict("Invalid JSON format for title or description field, should be dict") 
    
    type_data = UpdateTypeSchema(
        name=name_dict,
        description=description_dict,
        meta_description=meta_description_dict,
        filename=photo
    )
    return await types_service.update_type(uow, id, type_data)


@router.delete("/{id}", response_model=IdResponseSchema)
async def delete_type(uow: UOWDependency, id: int):
    return await types_service.delete_type(uow, id)
