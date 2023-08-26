from schemas.tour_activities import CreateTourActivitySchema, UpdateTourActivitySchema, TourActivitySchema
from repositories import Pagination
from datetime import datetime
from database.unitofwork import UnitOfWork
from utils.exceptions import CustomExceptions

class TourActivitiesService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def create_tour_activity(self, tour_activity_data: CreateTourActivitySchema) -> TourActivitySchema:
        tour_activity_dict = tour_activity_data.model_dump()
        async with self.uow:
            return await self.uow.tour_activities.create(tour_activity_dict)
        
    async def get_list_of_tours_and_activities(self, pagination: Pagination) -> list[TourActivitySchema]:
        async with self.uow:
            return await self.uow.tour_activities.get_all(pagination)
        
    async def get_tour_and_activity_by_id(self, tour_activity_id: int) -> TourActivitySchema:
        async with self.uow:
            return await self.uow.tour_activities.get_by_id(tour_activity_id)
        
    async def get_list_of_activities_of_tour(self, tour_id: int) -> list[TourActivitySchema]:
        async with self.uow:
            return await self.uow.tour_activities.get_list_of_activities_of_tour(tour_id)
        
    async def update_tour_activity(self, tour_activity_id: int, tour_activity_data: UpdateTourActivitySchema) -> TourActivitySchema:
        tour_activity_dict = tour_activity_data.model_dump()
        async with self.uow:
            return await self.uow.tour_activities.update(tour_activity_id, tour_activity_dict)
        
    async def delete_tour_activity(self, tour_activity_id: int) -> TourActivitySchema:
        async with self.uow:
            return await self.uow.tour_activities.delete(tour_activity_id)