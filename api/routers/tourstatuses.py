from typing import Annotated
from fastapi import APIRouter, Depends
from services import TourStatusesService
from utils.dependency import get_tour_statuses_services, get_current_user
from repositories import Pagination
from schemas.tourstatuses import CreateTourStatusSchema, UpdateTourStatusSchema, TourStatusSchema
from models import User
from security.permissionhandler import PermissionHandler, Permissions
from utils.locale_handler import LocaleHandler

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
    


@router.get('/{locale}', response_model=list[TourStatusSchema])
async def get_list_of_statuses(
    locale: Annotated[LocaleHandler, Depends()],
    pagination: Annotated[Pagination, Depends()],
    tour_status_service: Annotated[TourStatusesService, Depends(get_tour_statuses_services)]
) -> list[TourStatusSchema]:
    return await tour_status_service.get_list_of_statuses(locale, pagination)
    

@router.get('/{locale}/{id}', response_model=TourStatusSchema)
async def get_status_by_id(
    locale: Annotated[LocaleHandler, Depends()],
    id: int,
    tour_status_service: Annotated[TourStatusesService, Depends(get_tour_statuses_services)]
) -> TourStatusSchema:
    return await tour_status_service.get_status_by_id(id, locale)
    

@router.put('/{id}', response_model=TourStatusSchema)
async def update_status(
    id: int,
    tour_status_data: UpdateTourStatusSchema,
    tour_status_service: Annotated[TourStatusesService, Depends(get_tour_statuses_services)]
) -> TourStatusSchema:
    return await tour_status_service.update_status(id, tour_status_data)
    

@router.delete('/{id}', response_model=TourStatusSchema)
async def delete_status(
    id: int,
    tour_status_service: Annotated[TourStatusesService, Depends(get_tour_statuses_services)]
) -> TourStatusSchema:
    return await tour_status_service.delete_status(id)