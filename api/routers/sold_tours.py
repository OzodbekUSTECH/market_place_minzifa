from typing import Annotated
from fastapi import APIRouter, Depends
from services import sold_tours_service
from schemas.sold_tours import (
    CreateSoldTourSchema,
    UpdateSoldTourSchema,
    SoldTourSchema,
)
from schemas import IdResponseSchema
from repositories import Page
from utils.locale_handler import LocaleHandler

router = APIRouter(
    prefix="/sold-tours",
    tags=["Sold Tours (sell tours)"],
)


@router.post('', response_model=IdResponseSchema)
async def sell_tour(
    sold_tour_data: CreateSoldTourSchema,
):
    return await sold_tours_service.sell_tour(sold_tour_data)

@router.get('', response_model=Page[SoldTourSchema])
@LocaleHandler.serialize_one_all_models_by_locale
async def get_list_of_sold_tours(
    locale: Annotated[LocaleHandler, Depends()],
):
    return await sold_tours_service.get_list_of_sold_tours()

@router.get('/{id}', response_model=SoldTourSchema)
@LocaleHandler.serialize_one_all_models_by_locale
async def get_sold_tour_by_id(
    locale: Annotated[LocaleHandler, Depends()],
    id: int
):
    return await sold_tours_service.get_sold_tour_by_id(id)

@router.put('/{id}', response_model=IdResponseSchema)
async def update_sold_tour(
    id: int,
    sold_tour_data: UpdateSoldTourSchema
):
    return await sold_tours_service.update_sold_tour(id, sold_tour_data)

@router.delete('/{id}', response_model=IdResponseSchema)
async def delete_sold_tour(
    id: int
):
    return await sold_tours_service.delete_sold_tour(id)