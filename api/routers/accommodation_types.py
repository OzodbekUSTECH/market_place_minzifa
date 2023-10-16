from schemas import IdResponseSchema
from typing import Annotated
from fastapi import APIRouter, Depends
from repositories import Page
from services import accommodation_types_service
from schemas.accommodation_types import (
    CreateAccommodationTypeSchema,
    UpdateAccommodationTypeSchema,
    AccommodationTypeSchema,
)
from utils.locale_handler import LocaleHandler

from database import UOWDependency

router = APIRouter(
    prefix="/accommodation-types",
    tags=["Accommodation Types (single, double room ... etc)"],
)


@router.post('', response_model=IdResponseSchema)
async def create_accommodation_type(
    uow: UOWDependency,
    type_data: CreateAccommodationTypeSchema
):
    return await accommodation_types_service.create_type(uow, type_data)

@router.get('/{locale}', response_model=Page[AccommodationTypeSchema])
@LocaleHandler.serialize_one_all_models_by_locale
async def get_accommodation_types(
    uow: UOWDependency,
    locale: Annotated[LocaleHandler, Depends()]
):
    return await accommodation_types_service.get_types(uow)

@router.get("/{locale}/{id}", response_model=AccommodationTypeSchema)
@LocaleHandler.serialize_one_all_models_by_locale
async def get_accommodation_type_by_id(
    uow: UOWDependency, 
    id: int,
    locale: Annotated[LocaleHandler, Depends()]
):
    return await accommodation_types_service.get_type_by_id(uow, id)

@router.put('/{id}', response_model=IdResponseSchema)
async def update_accommodation_type(
    uow: UOWDependency,
    id: int,
    type_data: UpdateAccommodationTypeSchema
):
    return await accommodation_types_service.update_type(uow, id, type_data)

@router.delete('/{id}', response_model=IdResponseSchema)
async def delete_accommodation_type(
    uow: UOWDependency,
    id: int
):
    return await accommodation_types_service.delete_type(uow, id)
    

