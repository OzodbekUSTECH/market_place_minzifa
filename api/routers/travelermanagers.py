from typing import Annotated

from fastapi import APIRouter, Depends
from services.travelermanagers import TravelerManagersService
from utils.dependency import get_travelermanagers_services, get_current_user
from database.mail import EmailSender
from repositories.base import Pagination
from schemas.travelermanagers import ManagersSchema, TravelersSchema, CreateTravelerAndManagerSchema, UpdateTravelerAndManagerSchema, AssociationTravelAndManagerSchema

router = APIRouter(
    prefix="/travelermanagers",
    tags=["Travel and Managers"],
)



@router.get('', name="get all associations manager and traveler", response_model=list[AssociationTravelAndManagerSchema])
async def get_all_associations_data(
    pagination: Annotated[Pagination, Depends()],
    travelermanagers_service: Annotated[TravelerManagersService, Depends(get_travelermanagers_services)]
) -> list[AssociationTravelAndManagerSchema]:
    return await travelermanagers_service.get_all_associations_travel_and_manager(pagination)

@router.get("/{id}", name="get association by ID", response_model=AssociationTravelAndManagerSchema)
async def get_association_by_id(
    id: int,
    travelermanagers_service: Annotated[TravelerManagersService, Depends(get_travelermanagers_services)]
) -> AssociationTravelAndManagerSchema:
    return await travelermanagers_service.get_associations_travel_and_manager_by_id(id)

@router.get('/{manager_id}/travelers', name="get travelers of manager", response_model=list[TravelersSchema])
async def get_travelers_data_of_manager(
    manager_id: int,
    pagination: Annotated[Pagination, Depends()],
    travelermanagers_service: Annotated[TravelerManagersService, Depends(get_travelermanagers_services)]
) -> list[TravelersSchema]:
    return await travelermanagers_service.get_travelers_of_manager(manager_id, pagination)


@router.get('/{traveler_id}/managers', response_model=list[ManagersSchema])
async def get_managers_data_of_traveler(
    traveler_id: int,
    pagination: Annotated[Pagination, Depends()],
    travelermanagers_service: Annotated[TravelerManagersService, Depends(get_travelermanagers_services)]
) -> list[ManagersSchema]:
    return await travelermanagers_service.get_managers_of_traveler(traveler_id, pagination)


@router.post('', name="choose association traveler and manager", response_model=AssociationTravelAndManagerSchema)
async def choose_managers_for_traveler(
    travel_manager_data: CreateTravelerAndManagerSchema,
    travelermanagers_service: Annotated[TravelerManagersService, Depends(get_travelermanagers_services)]
) -> AssociationTravelAndManagerSchema:
    return await travelermanagers_service.connect_traveler_to_manager(travel_manager_data)

@router.put('/{id}', name="update manager of traveler or traveler of manager", response_model=AssociationTravelAndManagerSchema)
async def update_manager_of_traveler_or_traveler_of_manager_data(
    id: int,
    travel_manager_data: UpdateTravelerAndManagerSchema,
    travelermanagers_service: Annotated[TravelerManagersService, Depends(get_travelermanagers_services)]
) -> AssociationTravelAndManagerSchema:
    return await travelermanagers_service.update_manager_of_traveler_or_traveler_of_manager(id, travel_manager_data)

@router.delete('/{id}', name="delete association travel and manager", response_model=AssociationTravelAndManagerSchema)
async def delete_association_travel_and_manager_data(
    id: int,
    travelermanagers_service: Annotated[TravelerManagersService, Depends(get_travelermanagers_services)]
) -> AssociationTravelAndManagerSchema:
    return await travelermanagers_service.delete_traveler_and_manager(id)