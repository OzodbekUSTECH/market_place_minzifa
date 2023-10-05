from schemas.activities import CreateActivitySchema, UpdateActivitySchema
from database import UnitOfWork
from utils.exceptions import CustomExceptions
import models

class ActivitiesService:
    def __init__(self):
        self.uow = UnitOfWork()

    async def create_activity(self, activity_data: CreateActivitySchema) -> models.Activity:
        activity_data_dict = activity_data.model_dump()
        async with self.uow:
            activity = await self.uow.activities.create(activity_data_dict)
            await self.uow.commit()
            return activity
        
    async def get_list_of_activities(self) -> list[models.Activity]:
        async with self.uow:
            return await self.uow.activities.get_all()
        
    async def get_activity_by_id(self, activity_id: int) -> models.Activity:
        async with self.uow:
            return await self.uow.activities.get_by_id(activity_id)
        
    async def update_activity(self, activity_id: int, activity_data: UpdateActivitySchema) -> models.Activity:
        activity_dict = activity_data.model_dump()
        async with self.uow:
            activity = await self.uow.activities.update(activity_id, activity_dict)
            await self.uow.commit()
            return activity
        
    async def delete_activity(self, activity_id: int) -> models.Activity:
        async with self.uow:
            try:
                activity = await self.uow.activities.delete(activity_id)
                await self.uow.commit()
                return activity
            except:
                raise CustomExceptions.conflict("Cant be deleted activity since tours use this activity") 
        
activities_service = ActivitiesService()