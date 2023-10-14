from schemas.tour_hotels import (
    CreateTourHotelSchema,
    CreateTourHotelMediaGroup,

    UpdateTourHotelSchema
)
from database import UnitOfWork
from utils.media_handler import MediaHandler
import models
from fastapi import UploadFile
class TourHotelsService:
    def __init__(self):
        self.uow = UnitOfWork()

    async def create_hotel(self, hotel_data: CreateTourHotelSchema) -> models.TourHotel:
        async with self.uow:
            hotel: models.TourHotel = await self.uow.tour_hotels.create(hotel_data.model_dump())
            filenames = await MediaHandler.save_media(hotel_data.photos, MediaHandler.tour_hotels_media_dir)
            await self.uow.tour_hotel_media_groups.bulk_create(
                data_list=[CreateTourHotelMediaGroup(
                    tour_hotel_id=hotel.id,
                    filename=filename
                ).model_dump() for filename in filenames]
            )
            await self.uow.commit()
            return hotel
        
        
    async def create_hotel_media_group(self, tour_hotel_id: int, media_group: list[UploadFile]) -> None:
        filenames = await MediaHandler.save_media(media_group, MediaHandler.tour_hotels_media_dir)
        async with self.uow:
            await self.uow.tour_hotel_media_groups.bulk_create(
                data_list=[CreateTourHotelMediaGroup(
                    tour_hotel_id=tour_hotel_id,
                    filename=filename
                ).model_dump() for filename in filenames]
            )

            await self.uow.commit()

    async def update_hotel(self, id: int, hotel_data: UpdateTourHotelSchema) -> models.TourHotel:
        async with self.uow:
            hotel = await self.uow.tour_hotels.update(id, hotel_data.model_dump())
            await self.uow.commit()
            return hotel
        
    async def delete_hotel(self, id: int) -> models.TourHotel:
        async with self.uow:
            hotel = await self.uow.tour_hotels.delete(id)
            await self.uow.commit()
            return hotel
        
    async def delete_hotel_media(self, id: int) -> models.TourHotelMediaGroup:
        async with self.uow:
            hotel = await self.uow.tour_hotel_media_groups.delete(id)
            await self.uow.commit()
            return hotel
        

tour_hotels_service = TourHotelsService()