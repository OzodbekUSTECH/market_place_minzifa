from schemas.tour_comments_photos import TourCommentPhotoSchema
from fastapi import UploadFile, File, Request
from repositories import Pagination
from datetime import datetime
from database.unitofwork import UnitOfWork
from utils.exceptions import CustomExceptions
from utils.mediahandler import MediaHandler

class TourCommentsPhotosService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def create_tour_comment_photos(
            self,
            tour_comment_id: int,
            media_group: list[UploadFile],
    ) -> list[TourCommentPhotoSchema]:
        urls = await MediaHandler.save_media(media_group)
        async with self.uow:
            response = []
            for url in urls:
                tour_comment_dict = {
                    "tour_comment_id": tour_comment_id,
                    "photo_url": url
                }
                created_tour_comment_photo = await self.uow.tour_comments_photos.create(tour_comment_dict)
                response.append(created_tour_comment_photo)
            return response
        
    
    async def get_list_of_tour_comments_photos(self, pagination: Pagination) -> list[TourCommentPhotoSchema]:
        async with self.uow:
            return await self.uow.tour_comments_photos.get_all(pagination)
        
        

