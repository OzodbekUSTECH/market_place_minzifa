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

@router.get('', response_model=list[TourSchema])
async def search_tours_by_title(
    tours_service: Annotated[ToursService, Depends(get_tours_services)],
    query: str = Query(default="")
) -> list[TourSchema]:
    return await tours_service.serach_tours_by_title(query)


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

@router.get('/status/{status_id}', response_model=list[TourSchema])
async def  get_list_of_tours_by_status_id(
    status_id: int,
    pagination: Annotated[Pagination, Depends()],
    tours_service: Annotated[ToursService, Depends(get_tours_services)]
) -> list[TourSchema]:
    return await tours_service.get_list_of_tours_by_status(status_id, pagination)


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