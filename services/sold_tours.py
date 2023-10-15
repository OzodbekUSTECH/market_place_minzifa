from schemas.sold_tours import CreateSoldTourSchema, UpdateSoldTourSchema
from database import UnitOfWork
import models

class SoldToursService:
    

    async def sell_tour(self, uow: UnitOfWork, sold_tour_data: CreateSoldTourSchema) -> models.SoldTour:
        sold_tour_dict = sold_tour_data.model_dump()
        async with uow:
            sold_tour = await uow.sold_tours.create(sold_tour_dict)
            await uow.commit()
            return sold_tour
        
    async def get_list_of_sold_tours(self, uow: UnitOfWork, ) -> list[models.SoldTour]:
        async with uow:
            return await uow.sold_tours.get_all()
        
    async def get_sold_tour_by_id(self, uow: UnitOfWork, id: int) -> models.SoldTour:
        async with uow:
            return await uow.sold_tours.get_by_id(id)

    async def update_sold_tour(self, uow: UnitOfWork, id: int, sold_tour_data: UpdateSoldTourSchema) -> models.SoldTour:
        sold_tour_dict = sold_tour_data.model_dump()
        async with uow:
            sold_tour = await uow.sold_tours.update(id, sold_tour_dict)
            await uow.commit()
            return sold_tour
        
    async def delete_sold_tour(self, uow: UnitOfWork, id: int) -> models.SoldTour:
        async with uow:
            sold_tour = await uow.sold_tours.delete(id)
            await uow.commit()
            return sold_tour
            
sold_tours_service = SoldToursService()

    