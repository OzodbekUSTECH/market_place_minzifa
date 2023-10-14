from schemas.accommodation_types import (
    CreateAccommodationTypeSchema,
    UpdateAccommodationTypeSchema,

)
from database import UnitOfWork
import models
class AccommodationTypesService:
    def __init__(self):
        self.uow = UnitOfWork()

    async def create_type(self, type_data: CreateAccommodationTypeSchema) -> models.AccommodationType:
        async with self.uow:
            accommodation_type = await self.uow.accommodation_types.create(type_data.model_dump())
            await self.uow.commit()
            return accommodation_type
        
    async def get_types(self):
        async with self.uow:
            return await self.uow.accommodation_types.get_all()
        
    async def get_type_by_id(self, id: int) -> models.AccommodationType:
        async with self.uow:
            return await self.uow.accommodation_types.get_by_id(id)
        
    async def update_type(self, id: int, type_data: UpdateAccommodationTypeSchema) -> models.AccommodationType:
        async with self.uow:
            type: models.AccommodationType = await self.uow.accommodation_types.get_by_id(id)
            await self.uow.accommodation_types.update(type.id, type_data.model_dump())
            await self.uow.commit()
            return type
        
    async def delete_type(self, id: int) -> models.AccommodationType:
        async with self.uow:
            hotel_type: models.AccommodationType = await self.uow.accommodation_types.get_by_id(id)
            await self.uow.accommodation_types.delete(hotel_type.id)
            await self.uow.commit()
            return hotel_type

    

accommodation_types_service = AccommodationTypesService()