from typing import Annotated
from fastapi import APIRouter, Depends
from services import tour_includes_service
from repositories import Page
from schemas.tours_package.includes import (
    CreateMultipleIncludeInPrice,
    CreateIncludeInPriceSchema,
    UpdateIncludeInPriceSchema,
)
from schemas import IdResponseSchema
from database import UOWDependency

router = APIRouter(
    prefix="/includes",
    tags=["Included in price list"],
)

@router.post('/multiple/{tour_id}')
async def create_multiple_includes_in_price(
    uow: UOWDependency,
    tour_id: int,
    includes_data: list[CreateMultipleIncludeInPrice]
):
    return await tour_includes_service.create_multiple_includes_in_price(uow, tour_id, includes_data)

@router.post('', response_model=IdResponseSchema)
async def create_include_in_price(
    uow: UOWDependency,
    include_data: CreateIncludeInPriceSchema,
):
    return await tour_includes_service.create_include_in_price(uow, include_data)

@router.put('/{id}', response_model=IdResponseSchema)
async def update_include_in_price(
    uow: UOWDependency,
    id: int,
    include_data: UpdateIncludeInPriceSchema
):
    return await tour_includes_service.update_include_in_price(uow, id, include_data)


@router.delete('/{id}', response_model=IdResponseSchema)
async def delete_include_in_price(
    uow: UOWDependency,
    id: int,
):
    return await tour_includes_service.delete_include_in_price(uow, id)