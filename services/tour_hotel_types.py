from schemas.tour_hotels import (
    CreateTourHotelTypeSchema,
    UpdateTourHotelTypeSchema,

)
from database import UnitOfWork
import models
class TourHotelTypesService:
    def __init__(self):
        self.uow = UnitOfWork()

    async def create_hotel_type(self, type_data: CreateTourHotelTypeSchema) -> models.TourHotelType:
        async with self.uow:
            hotel_type = await self.uow.tour_hotel_types.create(type_data.model_dump())
            await self.uow.commit()
            return hotel_type
        
    async def get_hotel_types(self):
        async with self.uow:
            return await self.uow.tour_hotel_types
        
    async def get_hotel_type_by_id(self, id: int) -> models.TourHotelType:
        async with self.uow:
            return await self.uow.tour_hotel_types.get_by_id(id)
        
    async def update_hotel_type(self, id: int, type_data: UpdateTourHotelTypeSchema) -> models.TourHotelType:
        async with self.uow:
            hotel_type: models.TourHotelType = await self.uow.tour_hotel_types.get_by_id(id)
            await self.uow.tour_hotel_types.update(hotel_type.id, type_data.model_dump())
            await self.uow.commit()
            return hotel_type
        
    async def delete_hotel_type(self, id: int) -> models.TourHotelType:
        async with self.uow:
            hotel_type: models.TourHotelType = await self.uow.tour_hotel_types.get_by_id(id)
            await self.uow.tour_hotel_types.delete(hotel_type.id)
            await self.uow.commit()
            return hotel_type

    

tour_hotel_types_service = TourHotelTypesService()