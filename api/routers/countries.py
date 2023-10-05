from typing import Annotated
from fastapi import APIRouter, Depends
from services import countries_service
from repositories import Page
from schemas.countries import CreateCountrySchema, UpdateCountrySchema, CountrySchema
from schemas import IdResponseSchema
from utils.locale_handler import LocaleHandler

router = APIRouter(
    prefix="/countries",
    tags=["Countries (for tours)"],
)


@router.post("", response_model=IdResponseSchema)
async def create_country(country_data: CreateCountrySchema):
    return await countries_service.create_country(country_data)


@router.get("/{locale}", response_model=Page[CountrySchema])
@LocaleHandler.serialize_one_all_models_by_locale
async def get_list_of_countries(locale: Annotated[LocaleHandler, Depends()]):
    return await countries_service.get_list_of_countries()


@router.get("/{locale}/{id}", response_model=CountrySchema)
@LocaleHandler.serialize_one_all_models_by_locale
async def get_country_by_id(locale: Annotated[LocaleHandler, Depends()], id: int):
    return await countries_service.get_country_by_id(id)


@router.put("/{id}", response_model=IdResponseSchema)
async def update_country(id: int, country_data: UpdateCountrySchema):
    return await countries_service.update_country(id, country_data)


@router.delete("/{id}", response_model=IdResponseSchema)
async def delete_country(id: int):
    return await countries_service.delete_country(id)
