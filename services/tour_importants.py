from schemas.tour_importants import (
    CreateTourImportantSchema,
    UpdateTourImportantSchema,

)
from database import UnitOfWork
import models

class TourImportantsService:
    

    async def create_tour_important(self, uow: UnitOfWork, data: CreateTourImportantSchema) -> models.TourImportant:
        async with uow:
            tour_important = await uow.tour_importants.create(data.model_dump())
            await uow.commit()
            return tour_important
    
    async def update_tour_important(self, uow: UnitOfWork, id: int, data: UpdateTourImportantSchema) -> models.TourImportant:
        async with uow:
            tour_important = await uow.tour_importants.update(id, data.model_dump())
            await uow.commit()
            return tour_important
        
    async def delete_tour_important(self, uow: UnitOfWork, id: int) -> models.TourImportant:
        async with uow:
            tour_important = await uow.tour_importants.delete(id)
            await uow.commit()
            return tour_important
        
tour_importants_service = TourImportantsService()