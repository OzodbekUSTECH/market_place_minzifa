from schemas.tour_comments_media import TourCommentMediaSchema
from fastapi import UploadFile, File, Request
from repositories import Pagination
from datetime import datetime
from database.unitofwork import UnitOfWork
from utils.exceptions import CustomExceptions
from utils.mediahandler import MediaHandler

class TourCommentsMediaService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def create_tour_comment_media(
            self,
            tour_comment_id: int,
            media_group: list[UploadFile],
    ) -> list[TourCommentMediaSchema]:
        urls = await MediaHandler.save_media(media_group, MediaHandler.comment_media_dir)
        async with self.uow:
            response = []
            for url in urls:
                tour_comment_dict = {
                    "tour_comment_id": tour_comment_id,
                    "media_url": url
                }
                created_tour_comment_photo = await self.uow.tour_comments_media.create(tour_comment_dict)
                response.append(created_tour_comment_photo)
            return response
        
    
    async def get_list_of_tour_comments_media(self, pagination: Pagination) -> list[TourCommentMediaSchema]:
        async with self.uow:
            return await self.uow.tour_comments_media.get_all(pagination)
        
    async def get_tour_comments_media_by_id(self, tour_comments_media_id: int) -> TourCommentMediaSchema:
        async with self.uow:
            return await self.uow.tour_comments_media.get_by_id(tour_comments_media_id)
        
    async def get_list_of_tour_comments_media_by_tour_comment_id(self, tour_comment_id: int) -> list[TourCommentMediaSchema]:
        async with self.uow:
            comment_instance = await self.uow.tour_comments.get_by_id(tour_comment_id)
            return comment_instance.media
        
        

