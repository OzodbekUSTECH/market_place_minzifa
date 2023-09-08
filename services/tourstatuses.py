from schemas.tourstatuses import CreateTourStatusSchema, UpdateTourStatusSchema, TourStatusSchema
from repositories import Pagination
from datetime import datetime
from database.unitofwork import UnitOfWork
from utils.exceptions import CustomExceptions
from utils.locale_handler import LocaleHandler
from models import TourStatus
class TourStatusesService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def create_status(self, tour_status_data: CreateTourStatusSchema) -> TourStatus:
        tour_status_dict = tour_status_data.model_dump()
        async with self.uow:
            return await self.uow.tour_statuses.create(tour_status_dict)
        
    async def get_list_of_statuses(self, locale: LocaleHandler, pagination: Pagination = None) -> list[TourStatus]:
        async with self.uow:
            statuses = await self.uow.tour_statuses.get_all(pagination)
            return await self.uow.serialize_one_or_all_models_by_locale(statuses, locale)

    async def get_status_by_id(self, tour_status_id: int, locale: LocaleHandler):
        async with self.uow:
            status = await self.uow.tour_statuses.get_by_id(tour_status_id)
            return await self.uow.serialize_one_or_all_models_by_locale(status, locale)
        
    async def update_status(self, tour_status_id: int, tour_status_data: UpdateTourStatusSchema) -> TourStatus:
        tour_status_dict = tour_status_data.model_dump()
        async with self.uow:
            return await self.uow.tour_statuses.update(tour_status_id, tour_status_dict)
        
    async def delete_status(self, tour_status_id: int) -> TourStatus:
        async with self.uow:
            return await self.uow.tour_statuses.delete(tour_status_id)
            
