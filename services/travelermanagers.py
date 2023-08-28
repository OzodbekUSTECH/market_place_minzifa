from repositories import Pagination
from schemas.travelermanagers import ManagersSchema, TravelersSchema, CreateTravelerAndManagerSchema, DeleteTravelerAndManagerSchema, UpdateTravelerAndManagerSchema, AssociationTravelAndManagerSchema
from database.unitofwork import UnitOfWork
from utils.exceptions import CustomExceptions

class TravelerManagersService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def get_all_associations_travel_and_manager(self, pagination: Pagination):
        async with self.uow:
            associations = await self.uow.travelers_managers.get_all(pagination)
            return associations


    async def get_associations_travel_and_manager_by_id(self, association_id: int):
        async with self.uow:
            association = await self.uow.travelers_managers.get_by_id(association_id)
            
            return association

    async def get_travelers_of_manager_second_way(self, manager_id: int) -> AssociationTravelAndManagerSchema:
        async with self.uow:
            manager = await self.uow.users.get_by_id(manager_id)
            return manager.travelers
        
    async def get_managers_of_traveler_second_way(self, traveler_id: int) -> AssociationTravelAndManagerSchema:
        async with self.uow:
            traveler = await self.uow.users.get_by_id(traveler_id)
            return traveler.managers

    async def get_travelers_of_manager(self, manager_id: int, pagination: Pagination) -> list[TravelersSchema]:
        async with self.uow:
            return await self.uow.travelers_managers.get_travelers(manager_id, pagination)
        
    
    async def get_managers_of_traveler(self, traveler_id: int, pagination: Pagination) -> list[ManagersSchema]:
        async with self.uow:
            return await self.uow.travelers_managers.get_managers(traveler_id, pagination)
    
    async def connect_traveler_to_manager(self, travel_manager_data: CreateTravelerAndManagerSchema) -> AssociationTravelAndManagerSchema:
        travel_manager_dict = travel_manager_data.model_dump()
        async with self.uow:
            created_association = await self.uow.travelers_managers.create(travel_manager_dict)
            
            return created_association
    
    async def update_manager_of_traveler_or_traveler_of_manager(self, association_id: int, travel_manager_data: UpdateTravelerAndManagerSchema) -> AssociationTravelAndManagerSchema:
        travel_manager_dict = travel_manager_data.model_dump()
        async with self.uow:
            updated_association = await self.uow.travelers_managers.update(association_id, travel_manager_dict)
            
            return updated_association


    async def delete_traveler_and_manager(self, association_id: int) -> AssociationTravelAndManagerSchema:
        async with self.uow:
            deleted_association = await self.uow.travelers_managers.delete(association_id)
            
            return deleted_association