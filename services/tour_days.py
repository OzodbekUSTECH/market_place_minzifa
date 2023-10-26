from schemas.tour_days import (
    CreateTourDaySchema,
    CreateTourDayMediaGroup,

    UpdateTourDaySchema
)
from database import UnitOfWork
from utils.media_handler import MediaHandler
import models
from fastapi import UploadFile
from repositories import paginate
class TourDaysService:
   

    async def create_tour_day(self, uow: UnitOfWork, day_data: CreateTourDaySchema) -> models.TourDay:
        async with uow:
            tour_day:models.TourDay = await uow.tour_days.create(day_data.model_dump())
            if day_data.photos:
                filenames = await MediaHandler.save_media(day_data.photos, MediaHandler.tour_days_media_dir)
                await uow.tour_day_media_groups.bulk_create(
                    data_list=[CreateTourDayMediaGroup(
                        tour_day_id=tour_day.id,
                        filename = filename
                    ).model_dump() for filename in filenames]
                )

            await uow.commit()
            return tour_day

    async def create_tour_day_media_group(self, uow: UnitOfWork, tour_day_id: int, media_group: list[UploadFile]) -> None:
        filenames = await MediaHandler.save_media(media_group, MediaHandler.tour_days_media_dir)
        async with uow:
            
            await uow.tour_day_media_groups.bulk_create(
                data_list=[CreateTourDayMediaGroup(
                    tour_day_id=tour_day_id,
                    filename=filename
                ).model_dump() for filename in filenames]
            )
            await uow.commit()

    async def get_days_of_tour(self, uow: UnitOfWork, tour_id: int) -> list[models.TourDay]:
        async with uow:
            return await uow.tour_days.get_all_by(tour_id=tour_id)

    async def update_tour_day(self, uow: UnitOfWork, id: int, day_data: UpdateTourDaySchema) -> models.TourDay:
        async with uow:
            tour_day = await uow.tour_days.update(id, day_data.model_dump())
            await uow.commit()
            return tour_day

    async def delete_tour_day(self, uow: UnitOfWork, id: int) -> models.TourDay:
        async with uow:
            tour_day = await uow.tour_days.delete(id)
            await uow.commit()
            return tour_day
        
    async def delete_tour_day_media_group(self, uow: UnitOfWork, id: int) -> models.TourDayMediaGroup:
        async with uow:
            tour_day_photo = await uow.tour_day_media_groups.delete(id)
            await uow.commit()
            return tour_day_photo
        

tour_days_service = TourDaysService()
