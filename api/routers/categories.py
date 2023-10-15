from typing import Annotated
from fastapi import APIRouter, Depends
from services import categories_service
from repositories import Page
from schemas.categories import (
    CreateCategorySchema,
    UpdateCategorySchema,
    CategorySchema
)
from schemas import IdResponseSchema
from utils.locale_handler import LocaleHandler
from database import UOWDependency
router = APIRouter(
    prefix="/categories",
    tags=["Categories (for tours)"],
)


@router.post("", response_model=IdResponseSchema)
async def create_category(
    uow: UOWDependency,
    category_data: CreateCategorySchema
):
    """
    - name: dict[str, str]\n
    for example:\n
    name: {\n
        "ru": "Индивидуальный тур",\n
        "en": "Individual tour"\n
    }
    
    """
    return await categories_service.create_category(uow, category_data)


@router.get("/{locale}", response_model=Page[CategorySchema])
@LocaleHandler.serialize_one_all_models_by_locale
async def get_list_of_categories(
    uow: UOWDependency,
    locale: Annotated[LocaleHandler, Depends()]
):
    return await categories_service.get_list_of_categories(uow)


@router.get("/{locale}/{id}", response_model=CategorySchema)
@LocaleHandler.serialize_one_all_models_by_locale
async def get_category_by_id(
    uow: UOWDependency,
    locale: Annotated[LocaleHandler, Depends()], 
    id: int
):
    return await categories_service.get_category_by_id(uow, id)


@router.put("/{id}", response_model=IdResponseSchema)
async def update_category(
    uow: UOWDependency,
    id: int, 
    type_data: UpdateCategorySchema
):
    """
    - name: dict[str, str]\n
    for example:\n
    name: {\n
        "ru": "Индивидуальный тур",\n
        "en": "Individual tour"\n
    }
    
    """
    return await categories_service.update_category(uow, id, type_data)


@router.delete("/{id}", response_model=IdResponseSchema)
async def delete_category(
    uow: UOWDependency,
    id: int
):
    return await categories_service.delete_category(uow, id)
