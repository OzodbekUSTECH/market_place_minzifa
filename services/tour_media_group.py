from database import UnitOfWork
from schemas.tour_media_group import CreateTourMediaSchema
import models
from fastapi import UploadFile
from utils.media_handler import MediaHandler
class TourMediaGroupService:
    

    async def create_media_group(
            self,
            uow: UnitOfWork,
            tour_id: int,
            media_group: list[UploadFile]
    ) -> list[models.TourMedia]:
        async with uow:
            tour: models.Tour = await uow.tours.get_by_id(tour_id)
            filenames = await MediaHandler.save_media(media_group, MediaHandler.tours_media_dir)
                
            await uow.tour_media_group.bulk_create(
                    data_list=[CreateTourMediaSchema(
                        tour_id=tour.id,
                        filename=filename
                    ).model_dump() for filename in filenames]
            )
            
            await uow.commit()
        
    
        
    async def delete_media(self, uow: UnitOfWork, id: int) -> models.TourMedia:
        async with uow:
            tour_media: models.TourMedia = await uow.tour_media_group.get_by_id(id)
            await uow.tour_media_group.delete(id)
            await uow.commit()
            return tour_media
        

tour_media_group_service = TourMediaGroupService()

                

