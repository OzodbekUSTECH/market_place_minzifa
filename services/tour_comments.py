from schemas.tour_comments import (
    CreateTourCommentSchema, 
    UpdateTourCommentSchema, 

    CreateCommentMediaSchema,

)
from database import UnitOfWork
from repositories import paginate
from utils.media_handler import MediaHandler
import models
from utils.filters.filter_comments import FilterCommentsParams
from fastapi import UploadFile
class TourCommentsService:
    

    async def create_comment(self, uow: UnitOfWork, comment_data: CreateTourCommentSchema) -> models.TourComment:
        comment_dict = comment_data.model_dump()
        async with uow:
            comment: models.TourComment = await uow.tour_comments.create(comment_dict)
            if comment_data.media:
                filenames = await MediaHandler.save_media(comment_data.media, MediaHandler.tour_comments_media_dir)

                await uow.tour_comments_media.bulk_create(
                    data_list=[CreateCommentMediaSchema(
                        comment_id=comment.id,
                        filename=filename,
                    ).model_dump() for filename in filenames]
                )
            await uow.commit()
            return comment
    
   

    async def get_list_of_comments(self, uow: UnitOfWork, filter_params: FilterCommentsParams) -> list[models.TourComment]:
        async with uow:
            comments = await uow.tour_comments.get_all(reverse=True)
            return paginate(await filter_params.get_filtered_items(comments.items))
        
    async def get_comment_by_id(self, uow: UnitOfWork, id: int) -> models.TourComment:
        async with uow:
            return await uow.tour_comments.get_by_id(id)
        
    async def update_comment(self, uow: UnitOfWork, id: int, comment_data: UpdateTourCommentSchema) -> models.TourComment:
        comment_dict = comment_data.model_dump()
        async with uow:
            comment = await uow.tour_comments.update(id, comment_dict)
            await uow.commit()
            return comment
        
   
        
    async def delete_comment(self, uow: UnitOfWork, id: int) -> models.TourComment:
        async with uow:
            comment = await uow.tour_comments.delete(id)
            await uow.commit()
            return comment
        
    
    ##################################################################
    async def create_media(self, uow: UnitOfWork, comment_id: int, media_group: list[UploadFile]) -> None:
        async with uow:
            filenames = await MediaHandler.save_media(media_group, MediaHandler.tour_comments_media_dir)
            await uow.tour_comments_media.bulk_create(
                data_list=[CreateCommentMediaSchema(
                    comment_id=comment_id,
                    filename=filename
                ).model_dump() for filename in filenames]
            )
            await uow.commit()


    async def delete_media(self, uow: UnitOfWork, id: int) -> models.TourCommentMedia:
        async with uow:
            comment_media = await uow.tour_comments_media.delete(id)
            await uow.commit()
            return comment_media

tour_comments_service = TourCommentsService()