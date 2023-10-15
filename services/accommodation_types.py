from schemas.accommodation_types import (
    CreateAccommodationTypeSchema,
    UpdateAccommodationTypeSchema,

)
from database import UnitOfWork
import models
class AccommodationTypesService:
    

    async def create_type(self, uow: UnitOfWork, type_data: CreateAccommodationTypeSchema) -> models.AccommodationType:
        async with uow:
            accommodation_type = await uow.accommodation_types.create(type_data.model_dump())
            await uow.commit()
            return accommodation_type
        
    async def get_types(self, uow: UnitOfWork):
        async with uow:
            return await uow.accommodation_types.get_all()
        
    async def get_type_by_id(self, uow: UnitOfWork, id: int) -> models.AccommodationType:
        async with uow:
            return await uow.accommodation_types.get_by_id(id)
        
    async def update_type(self, uow: UnitOfWork, id: int, type_data: UpdateAccommodationTypeSchema) -> models.AccommodationType:
        async with uow:
            type: models.AccommodationType = await uow.accommodation_types.get_by_id(id)
            await uow.accommodation_types.update(type.id, type_data.model_dump())
            await uow.commit()
            return type
        
    async def delete_type(self, uow: UnitOfWork, id: int) -> models.AccommodationType:
        async with uow:
            hotel_type: models.AccommodationType = await uow.accommodation_types.get_by_id(id)
            await uow.accommodation_types.delete(hotel_type.id)
            await uow.commit()
            return hotel_type

    

accommodation_types_service = AccommodationTypesService()