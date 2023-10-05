from typing import Annotated
from fastapi import APIRouter, Depends
from services import regions_service
from repositories import Page
from schemas.regions import (
    CreateRegionSchema,
    UpdateRegionSchema,
    RegionSchema
)
from schemas import IdResponseSchema
from utils.locale_handler import LocaleHandler

router = APIRouter(
    prefix="/regions",
    tags=["Regions (for tours)"],
)

@router.post('', response_model=IdResponseSchema)
async def create_region(
    region_data: CreateRegionSchema
):
    return await regions_service.create_region(region_data)

@router.get('/{locale}', response_model=Page[RegionSchema])
@LocaleHandler.serialize_one_all_models_by_locale
async def get_list_of_regions(
    locale: Annotated[LocaleHandler, Depends()]
):
    return await regions_service.get_list_of_regions()

@router.get('/{locale}/{id}', response_model=RegionSchema)
@LocaleHandler.serialize_one_all_models_by_locale
async def get_region_by_id(
    locale: Annotated[LocaleHandler, Depends()],
    id: int
):
    return await regions_service.get_region_by_id(id)

@router.put('/{id}', response_model=IdResponseSchema)
async def update_region(
    id: int,
    region_data: UpdateRegionSchema
):
    return await regions_service.update_region(id, region_data)


@router.delete('/{id}', response_model=IdResponseSchema)
async def delete_region(
    id: int
):
    return await regions_service.delete_region(id)