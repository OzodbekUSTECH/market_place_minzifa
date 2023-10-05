from schemas.accommodations import CreateAccommodationSchema, UpdateAccommodationSchema
from database import UnitOfWork
from utils.exceptions import CustomExceptions
import models

class AccommodationsService:
    def __init__(self):
        self.uow = UnitOfWork()

    async def create_accommodation(self, accommodation_data: CreateAccommodationSchema) -> models.Accommodation:
        accommodation_dict = accommodation_data.model_dump()
        async with self.uow:
            accommodation = await self.uow.accommodations.create(accommodation_dict)
            await self.uow.commit()
            return accommodation
        
    async def get_list_of_accommodations(self) -> list[models.Accommodation]:
        async with self.uow:
            return await self.uow.accommodations.get_all()
        
    async def get_accommodation_by_id(self, id: int) -> models.Accommodation:
        async with self.uow:
            return await self.uow.accommodations.get_by_id(id)
        
    async def update_accommodation(self, id: int, accommodation_data: UpdateAccommodationSchema) -> models.Accommodation:
        accommodation_dict = accommodation_data.model_dump()
        async with self.uow:
            accommodation = await self.uow.accommodations.update(id, accommodation_dict)
            await self.uow.commit()
            return accommodation
        
    async def delete_accommodation(self, id: int) -> models.Accommodation:
        async with self.uow:
            accommodation = await self.uow.accommodations.delete(id)
            await self.uow.commit()
            return accommodation
        
accommodations_service = AccommodationsService()

