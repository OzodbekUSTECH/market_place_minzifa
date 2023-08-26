from schemas.tourstatuses import CreateTourStatusSchema, UpdateTourStatusSchema, TourStatusSchema
from repositories import Pagination
from datetime import datetime
from database.unitofwork import UnitOfWork
from utils.exceptions import CustomExceptions

class TourStatusesService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def create_status(self, tour_status_data: CreateTourStatusSchema) -> TourStatusSchema:
        tour_status_dict = tour_status_data.model_dump()
        async with self.uow:
            return await self.uow.tour_statuses.create(tour_status_dict)
        
    async def get_list_of_statuses(self, pagination: Pagination) -> list[TourStatusSchema]:
        async with self.uow:
            return await self.uow.tour_statuses.get_all(pagination)
    
    async def get_status_by_id(self, tour_status_id: int):
        async with self.uow:
            return await self.uow.tour_statuses.get_by_id(tour_status_id)
        
    async def update_status(self, tour_status_id: int, tour_status_data: UpdateTourStatusSchema) -> TourStatusSchema:
        tour_status_dict = tour_status_data.model_dump()
        async with self.uow:
            return await self.uow.tour_statuses.update(tour_status_id, tour_status_dict)
        
    async def delete_status(self, tour_status_id: int) -> TourStatusSchema:
        async with self.uow:
            return await self.uow.tour_statuses.delete(tour_status_id)
            
