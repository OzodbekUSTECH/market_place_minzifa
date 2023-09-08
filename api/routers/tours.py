from typing import Annotated
from fastapi import APIRouter, Depends, Query, Request
from services import ToursService
from utils.dependency import get_tours_services, get_current_user
from repositories import Pagination
from schemas.tours import CreateTourSchema, UpdateTourSchema, TourSchema, CreatedTourResponseSchema
from models import User
from datetime import date
from security.permissionhandler import PermissionHandler, Permissions
from utils.filter_tours import FilterTours
from utils.locale_handler import LocaleHandler

router = APIRouter(
    prefix="/tours",
    tags=["Tours"],
)

@router.get('/search')
async def search_tours(
    locale: Annotated[LocaleHandler, Depends()],
    pagination: Annotated[Pagination, Depends()],
    tours_service: Annotated[ToursService, Depends(get_tours_services)],
    filters: Annotated[FilterTours, Depends()]
) -> list[TourSchema]:
    return await tours_service.search_tours(
        filters,
        pagination,
        locale,
    )


@router.post('', response_model=CreatedTourResponseSchema)
async def create_tour(
    tour_data: CreateTourSchema,
    tours_service: Annotated[ToursService, Depends(get_tours_services)]
) -> TourSchema:
    return await tours_service.create_tour(tour_data)

@router.get('')
async def get_list_of_tours(
    locale: Annotated[LocaleHandler, Depends()],
    pagination: Annotated[Pagination, Depends()],
    tours_service: Annotated[ToursService, Depends(get_tours_services)]
) -> list[TourSchema]:
    return await tours_service.get_list_of_tours(locale, pagination)

@router.get('/user/{user_id}', response_model=list[TourSchema])
async def get_list_of_tours_of_user(
    locale: Annotated[LocaleHandler, Depends()],
    pagination: Annotated[Pagination, Depends()],
    user_id: int,
    tours_service: Annotated[ToursService, Depends(get_tours_services)]
):
    return await tours_service.get_list_of_tours_of_user(user_id, locale, pagination)

@router.get('/{id}', response_model=TourSchema)
async def get_tour_by_id(
    locale: Annotated[LocaleHandler, Depends()],
    id: int,
    request: Request,
    tours_service: Annotated[ToursService, Depends(get_tours_services)]
) -> TourSchema:
    return await tours_service.get_tour_by_id(id, request, locale)

@router.put('/{id}', response_model=TourSchema)
async def update_tour(
    id: int,
    tour_data: UpdateTourSchema,
    tours_service: Annotated[ToursService, Depends(get_tours_services)]
) -> TourSchema:
    return await tours_service.update_tour(id, tour_data)


@router.delete('/{id}', response_model=TourSchema)
async def delete_tour(
    id: int,
    tours_service: Annotated[ToursService, Depends(get_tours_services)]
) -> TourSchema:
    return await tours_service.delete_tour(id)