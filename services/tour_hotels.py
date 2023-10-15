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
    

    async def create_hotel(self, uow: UnitOfWork, hotel_data: CreateTourHotelSchema) -> models.TourHotel:
        async with uow:
            hotel: models.TourHotel = await uow.tour_hotels.create(hotel_data.model_dump())
            filenames = await MediaHandler.save_media(hotel_data.photos, MediaHandler.tour_hotels_media_dir)
            await uow.tour_hotel_media_groups.bulk_create(
                data_list=[CreateTourHotelMediaGroup(
                    tour_hotel_id=hotel.id,
                    filename=filename
                ).model_dump() for filename in filenames]
            )
            await uow.commit()
            return hotel
        
        
    async def create_hotel_media_group(self, uow: UnitOfWork, tour_hotel_id: int, media_group: list[UploadFile]) -> None:
        filenames = await MediaHandler.save_media(media_group, MediaHandler.tour_hotels_media_dir)
        async with uow:
            await uow.tour_hotel_media_groups.bulk_create(
                data_list=[CreateTourHotelMediaGroup(
                    tour_hotel_id=tour_hotel_id,
                    filename=filename
                ).model_dump() for filename in filenames]
            )

            await uow.commit()

    async def update_hotel(self, uow: UnitOfWork, id: int, hotel_data: UpdateTourHotelSchema) -> models.TourHotel:
        async with uow:
            hotel = await uow.tour_hotels.update(id, hotel_data.model_dump())
            await uow.commit()
            return hotel
        
    async def delete_hotel(self, uow: UnitOfWork, id: int) -> models.TourHotel:
        async with uow:
            hotel = await uow.tour_hotels.delete(id)
            await uow.commit()
            return hotel
        
    async def delete_hotel_media(self, uow: UnitOfWork, id: int) -> models.TourHotelMediaGroup:
        async with uow:
            hotel = await uow.tour_hotel_media_groups.delete(id)
            await uow.commit()
            return hotel
        

tour_hotels_service = TourHotelsService()