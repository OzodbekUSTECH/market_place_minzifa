from typing import Annotated
from fastapi import APIRouter, Depends
from services import types_service
from repositories import Page
from schemas.types import CreateTypeSchema, UpdateTypeSchema, TypeSchema
from schemas import IdResponseSchema
from utils.locale_handler import LocaleHandler


router = APIRouter(
    prefix="/types",
    tags=["Types (for tours)"],
)


@router.post("", response_model=IdResponseSchema)
async def create_type(type_data: CreateTypeSchema):
    """
    - name: dict[str, str]\n
    for example:\n
    name: {\n
        "ru": "Осмотр достопримечательностей",\n
        "en": "Sightseeing"\n
    }
    """
    return await types_service.create_type(type_data)


@router.get("/{locale}", response_model=Page[TypeSchema])
@LocaleHandler.serialize_one_all_models_by_locale
async def get_list_of_types(locale: Annotated[LocaleHandler, Depends()]):
    return await types_service.get_list_of_types()


@router.get("/{locale}/{id}", response_model=TypeSchema)
async def get_type_by_id(locale: Annotated[LocaleHandler, Depends()], id: int):
    return await types_service.get_type_by_id(id)


@router.put("/{id}", response_model=IdResponseSchema)
async def update_type(id: int, type_data: UpdateTypeSchema):
    """
    - name: dict[str, str]\n
    for example:\n
    name: {\n
        "ru": "Осмотр достопримечательностей",\n
        "en": "Sightseeing"\n
    }
    """
    return await types_service.update_type(id, type_data)


@router.delete("/{id}", response_model=IdResponseSchema)
async def delete_type(id: int):
    return await types_service.delete_type(id)
