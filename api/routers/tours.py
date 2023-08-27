from typing import Annotated
from fastapi import APIRouter, Depends, Query
from services import ToursService
from utils.dependency import get_tours_services, get_current_user
from repositories import Pagination
from schemas.tours import CreateTourSchema, UpdateTourSchema, TourSchema
from models import User
from security.permissionhandler import PermissionHandler, Permissions

router = APIRouter(
    prefix="/tours",
    tags=["Tours"],
)

@router.get('/search', response_model=list[TourSchema])
async def search_tours(
    pagination: Annotated[Pagination, Depends()],
    tours_service: Annotated[ToursService, Depends(get_tours_services)],
    query: str = Query(default=""),
    status_id: int = Query(None),
    tour_rating: int = Query(None),
) -> list[TourSchema]:
    return await tours_service.search_tours(query, status_id, tour_rating, pagination)


@router.post('', response_model=TourSchema)
async def create_tour(
    tour_data: CreateTourSchema,
    tours_service: Annotated[ToursService, Depends(get_tours_services)]
) -> TourSchema:
    return await tours_service.create_tour(tour_data)

@router.get('')
async def get_list_of_tours(
    pagination: Annotated[Pagination, Depends()],
    tours_service: Annotated[ToursService, Depends(get_tours_services)]
) -> list[TourSchema]:
    return await tours_service.get_list_of_tours(pagination)


@router.get('/{tour_id}', response_model=TourSchema)
async def get_tour_by_id(
    tour_id: int,
    tours_service: Annotated[ToursService, Depends(get_tours_services)]
) -> TourSchema:
    return await tours_service.get_tour_by_id(tour_id)

@router.put('/{tour_id}', response_model=TourSchema)
async def update_tour(
    tour_id: int,
    tour_data: UpdateTourSchema,
    tours_service: Annotated[ToursService, Depends(get_tours_services)]
) -> TourSchema:
    return await tours_service.update_tour(tour_id, tour_data)


@router.delete('/{tour_id}', response_model=TourSchema)
async def delete_tour(
    tour_id: int,
    tours_service: Annotated[ToursService, Depends(get_tours_services)]
) -> TourSchema:
    return await tours_service.delete_tour(tour_id)