from schemas.activities import CreateActivitySchema, UpdateActivitySchema
from database import UnitOfWork
from utils.exceptions import CustomExceptions
import models

class ActivitiesService:
    

    async def create_activity(self, uow: UnitOfWork, activity_data: CreateActivitySchema) -> models.Activity:
        activity_data_dict = activity_data.model_dump()
        async with uow:
            activity = await uow.activities.create(activity_data_dict)
            await uow.commit()
            return activity
        
    async def get_list_of_activities(self, uow: UnitOfWork,) -> list[models.Activity]:
        async with uow:
            return await uow.activities.get_all()
        
    async def get_activity_by_id(self,uow: UnitOfWork, activity_id: int) -> models.Activity:
        async with uow:
            return await uow.activities.get_by_id(activity_id)
        
    async def update_activity(self,uow: UnitOfWork, activity_id: int, activity_data: UpdateActivitySchema) -> models.Activity:
        activity_dict = activity_data.model_dump()
        async with uow:
            activity = await uow.activities.update(activity_id, activity_dict)
            await uow.commit()
            return activity
        
    async def delete_activity(self,uow: UnitOfWork, activity_id: int) -> models.Activity:
        async with uow:
            try:
                activity = await uow.activities.delete(activity_id)
                await uow.commit()
                return activity
            except:
                raise CustomExceptions.conflict("Cant be deleted activity since tours use this activity") 
        
activities_service = ActivitiesService()