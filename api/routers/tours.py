from typing import Annotated
from fastapi import APIRouter, Depends
from services import ToursService
from utils.dependency import get_tours_services, get_current_user
from repositories import Pagination
from schemas.tours import CreateTourSchema, UpdateTourSchema, TourSchema, CreatedTourSchemaResponse
from models import User
from security.permissionhandler import PermissionHandler, Permissions

router = APIRouter(
    prefix="/tours",
    tags=["Tours"],
)


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

@router.get('/published', response_model=list[TourSchema])
async def  get_list_of_published_tours(
    pagination: Annotated[Pagination, Depends()],
    tours_service: Annotated[ToursService, Depends(get_tours_services)]
) -> list[TourSchema]:
    return await tours_service.get_list_of_published_tours(pagination)

@router.get('/archived', response_model=list[TourSchema])
async def  get_list_of_archived_tours(
    pagination: Annotated[Pagination, Depends()],
    tours_service: Annotated[ToursService, Depends(get_tours_services)]
) -> list[TourSchema]:
    return await tours_service.get_list_of_archived_tours(pagination)

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