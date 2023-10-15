from schemas.tour_statuses import CreateTourStatusSchema, UpdateTourStatusSchema
from database.unitofwork import UnitOfWork
import models
class TourStatusesService:
    

    async def create_status(self, uow: UnitOfWork, tour_status_data: CreateTourStatusSchema) -> models.TourStatus:
        tour_status_dict = tour_status_data.model_dump()
        async with uow:
            tour_status = await uow.tour_statuses.create(tour_status_dict)
            await uow.commit()
            return tour_status
        
    async def get_list_of_statuses(self, uow: UnitOfWork) -> list[models.TourStatus]:
        async with uow:
            return await uow.tour_statuses.get_all()


    async def get_status_by_id(self, uow: UnitOfWork, id: int) -> models.TourStatus:
        async with uow:
            return await uow.tour_statuses.get_by_id(id)
        
    async def update_status(self, uow: UnitOfWork, id: int, tour_status_data: UpdateTourStatusSchema) -> models.TourStatus:
        tour_status_dict = tour_status_data.model_dump()
        async with uow:
            tour_status = await uow.tour_statuses.update(id, tour_status_dict)
            await uow.commit()
            return tour_status
        
    async def delete_status(self, uow: UnitOfWork, id: int) -> models.TourStatus:
        async with uow:
            tour_status = await uow.tour_statuses.delete(id)
            await uow.commit()
            return tour_status
            

tour_statuses_service = TourStatusesService()