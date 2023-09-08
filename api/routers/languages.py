from schemas.languages import CreateLanguageSchema, UpdateLanguageSchema, LanguageSchema
from typing import Annotated
from fastapi import APIRouter, Depends
from services import LanguagesService
from utils.dependency import get_languages_services, get_current_user
from repositories import Pagination
from models import User
from security.permissionhandler import PermissionHandler, Permissions
from utils.locale_handler import LocaleHandler

router = APIRouter(
    prefix="/languages",
    tags=["Languages"],
)


@router.post("", response_model=LanguageSchema)
async def create_language(
    language_data: CreateLanguageSchema,
    languages_service: Annotated[LanguagesService, Depends(get_languages_services)]
):
    return await languages_service.create_language(language_data)

@router.get('/{locale}', response_model=list[LanguageSchema])
async def get_list_of_languages(
    locale: Annotated[LocaleHandler, Depends()],
    pagination: Annotated[Pagination, Depends()],
    languages_service: Annotated[LanguagesService, Depends(get_languages_services)]
):
    return await languages_service.get_list_of_languages(locale, pagination)

@router.get('/{locale}/{id}', response_model=LanguageSchema)
async def get_language_by_id(
    locale: Annotated[LocaleHandler, Depends()],
    id: int, 
    languages_service: Annotated[LanguagesService, Depends(get_languages_services)]
):
    return await languages_service.get_language_by_id(id, locale)

@router.put('/{id}', response_model=LanguageSchema)
async def update_language(
    id: int,
    language_data: UpdateLanguageSchema,
    languages_service: Annotated[LanguagesService, Depends(get_languages_services)]
):
    return await languages_service.update_language(id, language_data)

@router.delete('/{id}', response_model=LanguageSchema)
async def delete_language(
    id: int,
    languages_service: Annotated[LanguagesService, Depends(get_languages_services)]
):
    return await languages_service.delete_language(id)