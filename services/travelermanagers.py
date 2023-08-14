from repositories.travelermanagers import TravelerManagersRepository
from repositories.base import Pagination
from fastapi import HTTPException, status
from schemas.travelermanagers import ManagersSchema, TravelersSchema, CreateTravelerAndManagerSchema, DeleteTravelerAndManagerSchema, UpdateTravelerAndManagerSchema, AssociationTravelAndManagerSchema

class TravelerManagersService:
    def __init__(self, travelermanagers_repo: TravelerManagersRepository):
        self.travelermanagers_repo: TravelerManagersRepository = travelermanagers_repo

    async def get_all_associations_travel_and_manager(self, pagination: Pagination):
        return await self.travelermanagers_repo.get_all(pagination)


    async def get_associations_travel_and_manager_by_id(self, association_id: int):
        return await self.travelermanagers_repo.get_by_id(association_id)


    async def get_travelers_of_manager(self, manager_id: int, pagination: Pagination) -> list[TravelersSchema]:
        return await self.travelermanagers_repo.get_travelers(manager_id, pagination)
        
    
    async def get_managers_of_traveler(self, traveler_id: int, pagination: Pagination) -> list[ManagersSchema]:
        return await self.travelermanagers_repo.get_managers(traveler_id, pagination)
    
    async def connect_traveler_to_manager(self, travel_manager_data: CreateTravelerAndManagerSchema) -> AssociationTravelAndManagerSchema:
        travel_manager_dict = travel_manager_data.model_dump()
        return await self.travelermanagers_repo.create(travel_manager_dict)
    
    async def update_manager_of_traveler_or_traveler_of_manager(self, association_id: int, travel_manager_data: UpdateTravelerAndManagerSchema) -> AssociationTravelAndManagerSchema:
        travel_manager_dict = travel_manager_data.model_dump()
        return await self.travelermanagers_repo.update(association_id, travel_manager_dict)


    async def delete_traveler_and_manager(self, association_id: int) -> AssociationTravelAndManagerSchema:
        return await self.travelermanagers_repo.delete(association_id)