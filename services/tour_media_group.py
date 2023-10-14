from database import UnitOfWork
from schemas.tour_media_group import CreateTourMediaSchema
from utils.exceptions import CustomExceptions
import models
from fastapi import UploadFile
from utils.media_handler import MediaHandler
class TourMediaGroupService:
    def __init__(self):
        self.uow = UnitOfWork()

    async def create_media_group(
            self,
            tour_id: int,
            media_group: list[UploadFile]
    ) -> list[models.TourMedia]:
        async with self.uow:
            tour: models.Tour = await self.uow.tours.get_by_id(tour_id)
            filenames = await MediaHandler.save_media(media_group, MediaHandler.tours_media_dir)
                
            await self.uow.tour_media_group.bulk_create(
                    data_list=[CreateTourMediaSchema(
                        tour_id=tour.id,
                        filename=filename
                    ).model_dump() for filename in filenames]
            )
            
            await self.uow.commit()
        
    
        
    async def delete_media(self, id: int) -> models.TourMedia:
        async with self.uow:
            tour_media: models.TourMedia = await self.uow.tour_media_group.get_by_id(id)
            await self.uow.tour_media_group.delete(id)
            await self.uow.commit()
            return tour_media
        

tour_media_group_service = TourMediaGroupService()

                

