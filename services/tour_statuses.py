from schemas.tour_statuses import CreateTourStatusSchema, UpdateTourStatusSchema
from database.unitofwork import UnitOfWork
from utils.exceptions import CustomExceptions
import models
class TourStatusesService:
    def __init__(self):
        self.uow = UnitOfWork()

    async def create_status(self, tour_status_data: CreateTourStatusSchema) -> models.TourStatus:
        tour_status_dict = tour_status_data.model_dump()
        async with self.uow:
            tour_status = await self.uow.tour_statuses.create(tour_status_dict)
            await self.uow.commit()
            return tour_status
        
    async def get_list_of_statuses(self) -> list[models.TourStatus]:
        async with self.uow:
            return await self.uow.tour_statuses.get_all()


    async def get_status_by_id(self, id: int) -> models.TourStatus:
        async with self.uow:
            return await self.uow.tour_statuses.get_by_id(id)
        
    async def update_status(self, id: int, tour_status_data: UpdateTourStatusSchema) -> models.TourStatus:
        tour_status_dict = tour_status_data.model_dump()
        async with self.uow:
            tour_status = await self.uow.tour_statuses.update(id, tour_status_dict)
            await self.uow.commit()
            return tour_status
        
    async def delete_status(self, id: int) -> models.TourStatus:
        async with self.uow:
            try:
                tour_status = await self.uow.tour_statuses.delete(id)
                await self.uow.commit()
                return tour_status
            except:
                raise CustomExceptions.forbidden("Status cant be deleted since tours use this status")
            


tour_statuses_service = TourStatusesService()