from schemas.tour_activity_levels import CreateTourActivityLevelSchema, UpdateTourActivityLevelSchema
from database import UnitOfWork
import models

class TourActivityLevelsService:
    
    async def create_activity_level(self, uow: UnitOfWork, activity_level_data: CreateTourActivityLevelSchema) -> models.TourActivityLevel:
        activity_level_dict = activity_level_data.model_dump()
        async with uow:
            activity_level = await uow.tour_activity_levels.create(activity_level_dict)
            await uow.commit()
            return activity_level
        
    async def get_list_of_activity_levels(self, uow: UnitOfWork) -> list[models.TourActivityLevel]:
        async with uow:
            return await uow.tour_activity_levels.get_all()
        
    async def get_activity_level_by_id(self, uow: UnitOfWork, id: int) -> models.TourActivityLevel:
        async with uow:
            return await uow.tour_activity_levels.get_by_id(id)
        
    async def update_activity_level(self, uow: UnitOfWork, id: int, activity_level_data: UpdateTourActivityLevelSchema) -> models.TourActivityLevel:
        activity_level_dict = activity_level_data.model_dump()
        async with uow:
            activity_level = await uow.tour_activity_levels.update(id, activity_level_dict)
            await uow.commit()
            return activity_level

    async def delete_activity_level(self, uow: UnitOfWork, id: int) -> models.TourActivityLevel:
        async with uow:
            activity_level = await uow.tour_activity_levels.delete(id)
            await uow.commit()
            return activity_level
        
tour_activity_levels_service = TourActivityLevelsService()