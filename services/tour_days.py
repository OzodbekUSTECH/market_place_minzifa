from schemas.tour_comments import (
    CreateTourCommentSchema, 
    UpdateTourCommentSchema, 

    CreateCommentMediaSchema,

)
from database import UnitOfWork
from repositories import paginate
from utils.exceptions import CustomExceptions
from utils.media_handler import MediaHandler
import models
from utils.filters.filter_comments import FilterCommentsParams
from fastapi import UploadFile
class TourDaysService:
    def __init__(self):
        self.uow = UnitOfWork()

    async def delete_tour_day(self, id: int) -> models.TourDay:
        async with self.uow:
            tour_day = await self.uow.tour_days.delete(id)
            await self.uow.commit()
            return tour_day
        

tour_days_service = TourDaysService()
