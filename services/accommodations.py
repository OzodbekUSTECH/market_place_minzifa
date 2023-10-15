from schemas.accommodations import CreateAccommodationSchema, UpdateAccommodationSchema
from database import UnitOfWork
from utils.exceptions import CustomExceptions
import models

class AccommodationsService:
   

    async def create_accommodation(self,uow: UnitOfWork, accommodation_data: CreateAccommodationSchema) -> models.Accommodation:
        accommodation_dict = accommodation_data.model_dump()
        async with uow:
            accommodation = await uow.accommodations.create(accommodation_dict)
            await uow.commit()
            return accommodation
        
    async def get_list_of_accommodations(self, uow: UnitOfWork) -> list[models.Accommodation]:
        async with uow:
            return await uow.accommodations.get_all()
        
    async def get_accommodation_by_id(self, uow: UnitOfWork, id: int) -> models.Accommodation:
        async with uow:
            return await uow.accommodations.get_by_id(id)
        
    async def update_accommodation(self,uow: UnitOfWork, id: int, accommodation_data: UpdateAccommodationSchema) -> models.Accommodation:
        accommodation_dict = accommodation_data.model_dump()
        async with uow:
            accommodation = await uow.accommodations.update(id, accommodation_dict)
            await uow.commit()
            return accommodation
        
    async def delete_accommodation(self,uow: UnitOfWork, id: int) -> models.Accommodation:
        async with uow:
            accommodation = await uow.accommodations.delete(id)
            await uow.commit()
            return accommodation
        
accommodations_service = AccommodationsService()

