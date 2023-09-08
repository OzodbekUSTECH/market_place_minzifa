from schemas.activities import CreateActivitySchema, UpdateActivitySchema, ActivitySchema
from repositories import Pagination
from datetime import datetime
from database.unitofwork import UnitOfWork
from utils.exceptions import CustomExceptions
from models import Activity
from utils.locale_handler import LocaleHandler
class ActivitiesService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def create_activity(self, activity_data: CreateActivitySchema) -> Activity:
        activity_data_dict = activity_data.model_dump()
        async with self.uow:
            return await self.uow.activities.create(activity_data_dict)
        
    async def get_list_of_activities(self, pagination:Pagination, locale: LocaleHandler) -> list[Activity]:
        async with self.uow:
            activities = await self.uow.activities.get_all(pagination)
            return await self.uow.serialize_one_or_all_models_by_locale(activities, locale)
        
    async def get_activity_by_id(self, activity_id: int, locale: LocaleHandler) -> Activity:
        async with self.uow:
            activity = await self.uow.activities.get_by_id(activity_id)
            return await self.uow.serialize_one_or_all_models_by_locale(activity, locale)
        
    async def update_activity(self, activity_id: int, activity_data: UpdateActivitySchema) -> Activity:
        activity_dict = activity_data.model_dump()
        async with self.uow:
            return await self.uow.activities.update(activity_id, activity_dict)
        
    async def delete_activity(self, activity_id: int) -> Activity:
        async with self.uow:
            return await self.uow.activities.delete(activity_id)