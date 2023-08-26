from typing import Annotated
from fastapi import APIRouter, Depends
from services import TourStatusesService
from utils.dependency import get_tour_statuses_services, get_current_user
from repositories import Pagination
from schemas.tourstatuses import CreateTourStatusSchema, UpdateTourStatusSchema, TourStatusSchema
from models import User
from security.permissionhandler import PermissionHandler, Permissions

router = APIRouter(
    prefix="/status",
    tags=["Statuses"],
)

@router.post('', response_model=TourStatusSchema)
async def create_status(
    tour_status_data: CreateTourStatusSchema,
    tour_status_service: Annotated[TourStatusesService, Depends(get_tour_statuses_services)]
) -> TourStatusSchema:
    return await tour_status_service.create_status(tour_status_data)
    


@router.get('', response_model=list[TourStatusSchema])
async def get_list_of_statuses(
    pagination: Annotated[Pagination, Depends()],
    tour_status_service: Annotated[TourStatusesService, Depends(get_tour_statuses_services)]
) -> list[TourStatusSchema]:
    return await tour_status_service.get_list_of_statuses(pagination)
    

@router.get('/{tour_status_id}', response_model=TourStatusSchema)
async def get_status_by_id(
    tour_status_id: int,
    tour_status_service: Annotated[TourStatusesService, Depends(get_tour_statuses_services)]
) -> TourStatusSchema:
    return await tour_status_service.get_status_by_id(tour_status_id)
    

@router.put('/{tour_status_id}', response_model=TourStatusSchema)
async def update_status(
    tour_status_id: int,
    tour_status_data: UpdateTourStatusSchema,
    tour_status_service: Annotated[TourStatusesService, Depends(get_tour_statuses_services)]
) -> TourStatusSchema:
    return await tour_status_service.update_status(tour_status_id, tour_status_data)
    

@router.delete('/{tour_status_id}', response_model=TourStatusSchema)
async def delete_status(
    tour_status_id: int,
    tour_status_service: Annotated[TourStatusesService, Depends(get_tour_statuses_services)]
) -> TourStatusSchema:
    return await tour_status_service.delete_status(tour_status_id)