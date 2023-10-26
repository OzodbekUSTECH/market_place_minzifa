from typing import Annotated
from fastapi import APIRouter, Depends
from services import tours_service
from repositories import Page
from schemas.tours import CreateTourSchema, UpdateTourSchema, TourSchema, OneTourSchema
from schemas import IdResponseSchema
from utils.locale_handler import LocaleHandler
from utils.filters.filter_tours import FilterToursParams
from database import UOWDependency

router = APIRouter(
    prefix="/tours",
    tags=["Tours"],
)


@router.post("", response_model=IdResponseSchema)
async def create_tour(
    uow: UOWDependency,
    tour_data: CreateTourSchema,
):
    return await tours_service.create_tour(uow, tour_data)


@router.get("", response_model=Page[TourSchema])
@LocaleHandler.serialize_one_all_models_by_locale
async def get_list_of_tours(
    uow: UOWDependency,
    locale: Annotated[LocaleHandler, Depends()],
    filter_params: Annotated[FilterToursParams, Depends()]
):
    return await tours_service.get_list_of_tours(uow, filter_params, locale)


@router.get("/{locale}/{id}", response_model=TourSchema)
@LocaleHandler.serialize_one_all_models_by_locale
async def get_tour_by_id(
    uow: UOWDependency,
    locale: Annotated[LocaleHandler, Depends()],
    id: int,
):
    return await tours_service.get_tour_by_id(
        uow, id,
    )


@router.put("/{id}", response_model=IdResponseSchema)
async def update_tour(
    uow: UOWDependency,
    id: int,
    tour_data: UpdateTourSchema,
):
    return await tours_service.update_tour(uow, id, tour_data)


@router.delete("/{id}", response_model=IdResponseSchema)
async def delete_tour(uow: UOWDependency, id: int):
    return await tours_service.delete_tour(uow, id)
