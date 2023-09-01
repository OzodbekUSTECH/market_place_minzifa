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

    async def create_tour_comments_media(
            self,
            tour_comment_id: int,
            media_group: list[UploadFile],
    ) -> list[TourCommentMediaSchema]:
        if len(media_group) > 3:
            raise CustomExceptions.forbidden("Maximum number of media is 3")
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
        
    async def update_tour_comments_media(
            self, 
            tour_comments_media_id: int,
            media: UploadFile
    ) -> TourCommentMediaSchema:
        url = await MediaHandler.update_media(media, MediaHandler.comment_media_dir)
        async with self.uow:
            media_dict = {
                "url": url
            }

            return await self.uow.tour_comments_media.update(tour_comments_media_id, media_dict)
        

    async def delete_tour_comments_media(self, tour_comment_media_id: int) -> TourCommentMediaSchema:
        async with self.uow:
            return await self.uow.tour_comments_media.delete(tour_comment_media_id)