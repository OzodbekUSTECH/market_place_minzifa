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
class TourCommentsService:
    def __init__(self):
        self.uow = UnitOfWork()

    async def create_comment(self, comment_data: CreateTourCommentSchema) -> models.TourComment:
        comment_dict = comment_data.model_dump()
        async with self.uow:
            comment: models.TourComment = await self.uow.tour_comments.create(comment_dict)
            if comment_data.media:
                filenames = await MediaHandler.save_media(comment_data.media, MediaHandler.tour_comments_media_dir)

                await self.uow.tour_comments_media.bulk_create(
                    data_list=[CreateCommentMediaSchema(
                        comment_id=comment.id,
                        filename=filename,
                    ).model_dump() for filename in filenames]
                )
            await self.uow.commit()
            return comment
    
   

    async def get_list_of_comments(self, filter_params: FilterCommentsParams) -> list[models.TourComment]:
        async with self.uow:
            comments = await self.uow.tour_comments.get_all(reverse=True)
            return paginate(await filter_params.get_filtered_items(comments.items))
        
    async def get_comment_by_id(self, id: int) -> models.TourComment:
        async with self.uow:
            return await self.uow.tour_comments.get_by_id(id)
        
    async def update_comment(self, id: int, comment_data: UpdateTourCommentSchema) -> models.TourComment:
        comment_dict = comment_data.model_dump()
        async with self.uow:
            comment = await self.uow.tour_comments.update(id, comment_dict)
            await self.uow.commit()
            return comment
        
   
        
    async def delete_comment(self, id: int) -> models.TourComment:
        async with self.uow:
            comment = await self.uow.tour_comments.delete(id)
            await self.uow.commit()
            return comment
        
    
    ##################################################################
    async def create_media(self, comment_id: int, media_group: list[UploadFile]) -> None:
        async with self.uow:
            filenames = await MediaHandler.save_media(media_group, MediaHandler.tour_comments_media_dir)
            await self.uow.tour_comments_media.bulk_create(
                data_list=[CreateCommentMediaSchema(
                    comment_id=comment_id,
                    filename=filename
                ).model_dump() for filename in filenames]
            )
            await self.uow.commit()


    async def delete_media(self, id: int) -> models.TourCommentMedia:
        async with self.uow:
            comment_media = await self.uow.tour_comments_media.delete(id)
            await self.uow.commit()
            return comment_media

tour_comments_service = TourCommentsService()