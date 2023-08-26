from typing import Annotated
from fastapi import APIRouter, Depends
from services import ActivitiesService
from utils.dependency import get_activities_services, get_current_user
from repositories.base import Pagination
from schemas.activities import CreateActivitySchema, UpdateActivitySchema, ActivitySchema
from models import User
from security.permissionhandler import PermissionHandler, Permissions

router = APIRouter(
    prefix="/activities",
    tags=["Acitivities"],
)

@router.post('', response_model=ActivitySchema)
async def create_activity(
    activity_data: CreateActivitySchema,
    activities_service: Annotated[ActivitiesService, Depends(get_activities_services)]
) -> ActivitySchema:
    return await activities_service.create_activity(activity_data)

@router.get('', response_model=list[ActivitySchema])
async def get_list_of_activities(
    pagination: Annotated[Pagination, Depends()],
    activities_service: Annotated[ActivitiesService, Depends(get_activities_services)]
) -> list[ActivitySchema]:
    return await activities_service.get_list_of_activities(pagination)

@router.get('/{activity_id}', response_model=ActivitySchema)
async def get_activity_by_id(
    activity_id: int,
    activities_service: Annotated[ActivitiesService, Depends(get_activities_services)]
) -> ActivitySchema:
    return await activities_service.get_activity_by_id(activity_id)

@router.put('/{activity_id}', response_model=ActivitySchema)
async def update_activity(
    activity_id: int,
    activity_data: UpdateActivitySchema,
    activities_service: Annotated[ActivitiesService, Depends(get_activities_services)]
) -> ActivitySchema:
    return await activities_service.update_activity(activity_id, activity_data)

@router.delete('/{activity_id}', response_model=ActivitySchema)
async def delete_activity(
    activity_id: int,
    activities_service: Annotated[ActivitiesService, Depends(get_activities_services)]
) -> ActivitySchema:
    return await activities_service.delete_activity(activity_id)