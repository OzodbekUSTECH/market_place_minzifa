from schemas.tour_days import (
    CreateTourDaySchema,
    CreateTourDayMediaGroup,

    UpdateTourDaySchema
)
from database import UnitOfWork
from utils.media_handler import MediaHandler
import models
from fastapi import UploadFile
class TourDaysService:
    def __init__(self):
        self.uow = UnitOfWork()

    async def create_tour_day(self, day_data: CreateTourDaySchema) -> models.TourDay:
        async with self.uow:
            tour_day = await self.uow.tour_days.create(day_data.model_dump())
            await self.uow.commit()
            return tour_day

    async def create_tour_day_media_group(self, tour_day_id: int, media_group: list[UploadFile]) -> None:
        filenames = await MediaHandler.save_media(media_group, MediaHandler.tour_days_media_dir)
        async with self.uow:
            
            await self.uow.tour_day_media_groups.bulk_create(
                data_list=[CreateTourDayMediaGroup(
                    tour_day_id=tour_day_id,
                    filename=filename
                ).model_dump() for filename in filenames]
            )
            await self.uow.commit()

    async def update_tour_day(self, id: int, day_data: UpdateTourDaySchema) -> models.TourDay:
        async with self.uow:
            tour_day = await self.uow.tour_days.update(id, day_data.model_dump())
            await self.uow.commit()
            return tour_day

    async def delete_tour_day(self, id: int) -> models.TourDay:
        async with self.uow:
            tour_day = await self.uow.tour_days.delete(id)
            await self.uow.commit()
            return tour_day
        
    async def delete_tour_day_media_group(self, id: int) -> models.TourDayMediaGroup:
        async with self.uow:
            tour_day_photo = await self.uow.tour_day_media_groups.delete(id)
            await self.uow.commit()
            return tour_day_photo
        

tour_days_service = TourDaysService()
