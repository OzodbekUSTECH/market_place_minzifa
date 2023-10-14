from schemas.tour_importants import (
    CreateTourImportantSchema,
    UpdateTourImportantSchema,

)
from database import UnitOfWork
import models

class TourImportantsService:
    def __init__(self):
        self.uow = UnitOfWork()

    async def create_tour_important(self, data: CreateTourImportantSchema) -> models.TourImportant:
        async with self.uow:
            tour_important = await self.uow.tour_importants.create(data.model_dump())
            await self.uow.commit()
            return tour_important
    
    async def update_tour_important(self, id: int, data: UpdateTourImportantSchema) -> models.TourImportant:
        async with self.uow:
            tour_important = await self.uow.tour_importants.update(id, data.model_dump())
            await self.uow.commit()
            return tour_important
        
    async def delete_tour_important(self, id: int) -> models.TourImportant:
        async with self.uow:
            tour_important = await self.uow.tour_importants.delete(id)
            await self.uow.commit()
            return tour_important
        
tour_importants_service = TourImportantsService()