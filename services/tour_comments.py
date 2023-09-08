from schemas.tour_comments import CreateTourCommentSchema, UpdateTourCommentSchema, TourCommentSchema
from repositories import Pagination
from datetime import datetime
from database.unitofwork import UnitOfWork
from utils.exceptions import CustomExceptions
from models import TourComment
class TourCommentsService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def create_tour_comment(self, tour_comment_data: CreateTourCommentSchema) -> TourComment:
        tour_comment_dict = tour_comment_data.model_dump()
        async with self.uow:
            return await self.uow.tour_comments.create(tour_comment_dict)
        

    async def get_list_of_tour_comments(self, pagination: Pagination) -> list[TourComment]:
        async with self.uow:
            return await self.uow.tour_comments.get_all(pagination)
        
    async def get_tour_comment_by_id(self, tour_comment_id: int) -> TourComment:
        async with self.uow:
            return await self.uow.tour_activities.get_by_id(tour_comment_id)
        
    async def get_list_of_comments_of_tour(self, tour_id: int, pagination: Pagination) -> list[TourComment]:
        async with self.uow:
            return await self.uow.tour_comments.get_list_of_comments_of_tour(tour_id, pagination)

    async def update_tour_comment(self, tour_comment_id: int, tour_comment_data: UpdateTourCommentSchema) -> TourComment:
        tour_comment_dict = tour_comment_data.model_dump()
        async with self.uow:
            return await self.uow.tour_comments.update(tour_comment_id, tour_comment_dict)
        
    async def delete_tour_comment(self, tour_comment_id: int) -> TourComment:
        async with self.uow:
            return await self.uow.tour_comments.delete(tour_comment_id)