from typing import Annotated
from fastapi import APIRouter, Depends
from services import tour_excludes_service
from repositories import Page
from schemas.tours_package.excludes import (
    CreateMultipleExcludeInPrice,
    CreateExcludeInPriceSchema,
    UpdateExcludeInPriceSchema,
)
from schemas import IdResponseSchema
from database import UOWDependency

router = APIRouter(
    prefix="/excludes",
    tags=["Excluded in price list"],
)

@router.post('/multiple/{tour_id}')
async def create_multiple_includes_in_price(
    uow: UOWDependency,
    tour_id: int,
    excludes_data: list[CreateMultipleExcludeInPrice]
):
    return await tour_excludes_service.create_multiple_excludes_in_price(uow, tour_id, excludes_data)


@router.post('', response_model=IdResponseSchema)
async def create_exclude_in_price(
    uow: UOWDependency,
    exclude_data: CreateExcludeInPriceSchema,
):
    return await tour_excludes_service.create_exclude_in_price(uow, exclude_data)

@router.put('/{id}', response_model=IdResponseSchema)
async def update_exclude_in_price(
    uow: UOWDependency,
    id: int,
    exclude_data: UpdateExcludeInPriceSchema
):
    return await tour_excludes_service.update_exclude_in_price(uow, id, exclude_data)


@router.delete('/{id}', response_model=IdResponseSchema)
async def delete_exclude_in_price(
    uow: UOWDependency,
    id: int,
):
    return await tour_excludes_service.delete_exclude_in_price(uow, id)