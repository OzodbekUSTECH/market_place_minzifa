from schemas.activities import CreateActivitySchema, UpdateActivitySchema, ActivitySchema
from repositories import Pagination
from datetime import datetime
from database.unitofwork import UnitOfWork
from utils.exceptions import CustomExceptions

class ActivitiesService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def create_activity(self, activity_data: CreateActivitySchema) -> ActivitySchema:
        activity_data_dict = activity_data.model_dump()
        async with self.uow:
            return await self.uow.activities.create(activity_data_dict)
        
    async def get_list_of_activities(self, pagination:Pagination) -> list[ActivitySchema]:
        async with self.uow:
            return await self.uow.activities.get_all(pagination)
        
    async def get_activity_by_id(self, activity_id: int) -> ActivitySchema:
        async with self.uow:
            return await self.uow.activities.get_by_id(activity_id)
        
    async def update_activity(self, activity_id: int, activity_data: UpdateActivitySchema) -> ActivitySchema:
        activity_dict = activity_data.model_dump()
        async with self.uow:
            return await self.uow.activities.update(activity_id, activity_dict)
        
    async def delete_activity(self, activity_id: int) -> ActivitySchema:
        async with self.uow:
            return await self.uow.activities.delete(activity_id)