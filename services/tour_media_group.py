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
        filenames = await MediaHandler.save_media(media_group, MediaHandler.tours_media_dir)
        async with self.uow:
            response = []
            for filename in filenames:
                media_dict = CreateTourMediaSchema(
                    tour_id=tour_id,
                    filename=filename
                ).model_dump
                
                tour_media = await self.uow.tour_media_group.create(media_dict)
                response.append(tour_media)
            
            await self.uow.commit()
            return response
        
    
        
    async def delete_media(self, id: int) -> models.TourMedia:
        async with self.uow:
            tour_media = await self.uow.tour_media_group.delete(id)
            await self.uow.commit()
            return tour_media
        

tour_media_group_service = TourMediaGroupService()

                

