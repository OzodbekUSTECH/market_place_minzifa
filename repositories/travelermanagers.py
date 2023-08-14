from repositories.base import BaseRepository, Pagination
from schemas.travelermanagers import TravelersSchema, ManagersSchema, CreateTravelerAndManagerSchema

class TravelerManagersRepository(BaseRepository):
    async def get_travelers(self, manager_id: int, pagination: Pagination) -> list[TravelersSchema]:
        manager = self.session.query(self.model).filter(self.model.manager_id == manager_id).offset(pagination.offset).limit(pagination.limit).all()
        travelers = [data.to_read_model_of_traveler() for data in manager]
        return travelers
        
        
    async def get_managers(self, traveler_id: int, pagination: Pagination) -> list[ManagersSchema]:
        traveler = self.session.query(self.model).filter(self.model.traveler_id == traveler_id).offset(pagination.offset).limit(pagination.limit).all()
        managers = [data.to_read_model_of_manager() for data in traveler] 
        return managers
        
    async def create_traveler_and_manager_association(self, travel_manager_dict: dict) -> TravelersSchema:
        created_association = await self.create(travel_manager_dict)
        return created_association.to_read_model_of_traveler()
    

    async def delete_traveler_and_manager_association(self, travel_manager_dict: dict) -> TravelersSchema:
        created_association = await self.delete(travel_manager_dict)
        return created_association.to_read_model_of_traveler()

    