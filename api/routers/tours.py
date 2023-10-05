from typing import Annotated
from fastapi import APIRouter, Depends
from services import tours_service
from repositories import Page
from schemas.tours import CreateTourSchema, UpdateTourSchema, TourSchema
from schemas import IdResponseSchema
from utils.locale_handler import LocaleHandler
from utils.filters.filter_tours import FilterToursParams

router = APIRouter(
    prefix="/tours",
    tags=["Tours"],
)


@router.post("", response_model=IdResponseSchema)
async def create_tour(
    tour_data: CreateTourSchema,
):
    return await tours_service.create_tour(tour_data)


@router.get("", response_model=Page[TourSchema])
@LocaleHandler.serialize_one_all_models_by_locale
async def get_list_of_tours(
    locale: Annotated[LocaleHandler, Depends()],
    filter_params: Annotated[FilterToursParams, Depends()]
):
    return await tours_service.get_list_of_tours(filter_params, locale)


@router.get("/{locale}/{id}", response_model=TourSchema)
@LocaleHandler.serialize_one_all_models_by_locale
async def get_tour_by_id(
    locale: Annotated[LocaleHandler, Depends()],
    id: int,
):
    return await tours_service.get_tour_by_id(
        id,
    )


@router.put("/{id}", response_model=IdResponseSchema)
async def update_tour(
    id: int,
    tour_data: UpdateTourSchema,
):
    return await tours_service.update_tour(id, tour_data)


@router.delete("/{id}", response_model=IdResponseSchema)
async def delete_tour(id: int):
    return await tours_service.delete_tour(id)
