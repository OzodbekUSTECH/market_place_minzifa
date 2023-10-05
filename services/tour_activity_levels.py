from schemas.tour_activity_levels import CreateTourActivityLevelSchema, UpdateTourActivityLevelSchema
from database import UnitOfWork
from utils.exceptions import CustomExceptions
import models

class TourActivityLevelsService:
    def __init__(self):
        self.uow = UnitOfWork()

    async def create_activity_level(self, activity_level_data: CreateTourActivityLevelSchema) -> models.TourActivityLevel:
        activity_level_dict = activity_level_data.model_dump()
        async with self.uow:
            activity_level = await self.uow.tour_activity_levels.create(activity_level_dict)
            await self.uow.commit()
            return activity_level
        
    async def get_list_of_activity_levels(self) -> list[models.TourActivityLevel]:
        async with self.uow:
            return await self.uow.tour_activity_levels.get_all()
        
    async def get_activity_level_by_id(self, id: int) -> models.TourActivityLevel:
        async with self.uow:
            return await self.uow.tour_activity_levels.get_by_id(id)
        
    async def update_activity_level(self, id: int, activity_level_data: UpdateTourActivityLevelSchema) -> models.TourActivityLevel:
        activity_level_dict = activity_level_data.model_dump()
        async with self.uow:
            activity_level = await self.uow.tour_activity_levels.update(id, activity_level_dict)
            await self.uow.commit()
            return activity_level

    async def delete_activity_level(self, id: int) -> models.TourActivityLevel:
        async with self.uow:
            activity_level = await self.uow.tour_activity_levels.delete(id)
            await self.uow.commit()
            return activity_level
        
tour_activity_levels_service = TourActivityLevelsService()