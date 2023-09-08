from typing import Annotated
from fastapi import APIRouter, Depends
from services import TourActivitiesService
from utils.dependency import get_tour_activities_services, get_current_user
from repositories.base import Pagination
from schemas.tour_activities import CreateTourActivitySchema, UpdateTourActivitySchema, TourActivitySchema
from models import User
from security.permissionhandler import PermissionHandler, Permissions

router = APIRouter(
    prefix="/tour/activities",
    tags=["Tour Acitivities"],
)

@router.post('', response_model=TourActivitySchema)
async def create_tour_activity(
    tour_activity_data: CreateTourActivitySchema,
    tour_activities_service: Annotated[TourActivitiesService, Depends(get_tour_activities_services)]
) -> TourActivitySchema:
    return await tour_activities_service.create_tour_activity(tour_activity_data)

@router.get('', response_model=list[TourActivitySchema])
async def get_list_of_tours_and_activities(
    pagination: Annotated[Pagination, Depends()],
    tour_activities_service: Annotated[TourActivitiesService, Depends(get_tour_activities_services)]
) -> list[TourActivitySchema]:
    return await tour_activities_service.get_list_of_tours_and_activities(pagination)

@router.get('/{id}', response_model=TourActivitySchema)
async def get_tour_and_activity_by_id(
    id: int,
    tour_activities_service: Annotated[TourActivitiesService, Depends(get_tour_activities_services)]
) -> TourActivitySchema:
    return await tour_activities_service.get_tour_and_activity_by_id(id)

@router.get('/tour/{tour_id}', response_model=list[TourActivitySchema])
async def get_list_of_activities_of_tour(
    tour_id: int,
    tour_activities_service: Annotated[TourActivitiesService, Depends(get_tour_activities_services)]
) -> list[TourActivitySchema]:
    return await tour_activities_service.get_list_of_activities_of_tour(tour_id)

@router.put('/{id}', response_model=TourActivitySchema)
async def update_tour_activity(
    id: int,
    tour_activity_data: UpdateTourActivitySchema,
    tour_activities_service: Annotated[TourActivitiesService, Depends(get_tour_activities_services)]
) -> TourActivitySchema:
    return await tour_activities_service.update_tour_activity(id, tour_activity_data)

@router.delete('/{id}', response_model=TourActivitySchema)
async def delete_tour_activity(
    id: int,
    tour_activities_service: Annotated[TourActivitiesService, Depends(get_tour_activities_services)]
) -> TourActivitySchema:
    return await tour_activities_service.delete_tour_activity(id)