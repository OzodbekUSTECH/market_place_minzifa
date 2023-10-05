from schemas.languages import CreateLanguageSchema, UpdateLanguageSchema, LanguageSchema
from typing import Annotated
from fastapi import APIRouter, Depends
from services import languages_service
from repositories import Page
from schemas import IdResponseSchema
from utils.locale_handler import LocaleHandler

router = APIRouter(
    prefix="/languages",
    tags=["Languages"],
)


@router.post("", response_model=IdResponseSchema)
async def create_language(
    language_data: CreateLanguageSchema,
):
    """
    - name: dict[str, str]\n
    for example:\n
    name: {\n
        "ru": "Языка на русском",\n
        "en": "Language in english"\n
    }
    """
    return await languages_service.create_language(language_data)


@router.get("/{locale}", response_model=Page[LanguageSchema])
@LocaleHandler.serialize_one_all_models_by_locale
async def get_list_of_languages(
    locale: Annotated[LocaleHandler, Depends()],
):
    return await languages_service.get_list_of_languages()




@router.get("/{locale}/{id}", response_model=LanguageSchema)
@LocaleHandler.serialize_one_all_models_by_locale
async def get_language_by_id(
    locale: Annotated[LocaleHandler, Depends()],
    id: int,
):
    return  await languages_service.get_language_by_id(id)


@router.put("/{id}", response_model=IdResponseSchema)
async def update_language(
    id: int,
    language_data: UpdateLanguageSchema,
):
    """
    - name: dict[str, str]\n
    for example:\n
    name: {\n
        "ru": "Языка на русском",\n
        "en": "Language in english"\n
    }
    
    """
    return await languages_service.update_language(id, language_data)


@router.delete("/{id}", response_model=IdResponseSchema)
async def delete_language(
    id: int,
):
    return await languages_service.delete_language(id)
