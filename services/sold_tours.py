from repositories import Pagination
from schemas.sold_tours import CreateSoldTourSchema, UpdateSoldTourSchema
from database import UnitOfWork
from utils.exceptions import CustomExceptions
import models

class SoldToursService:
    def __init__(self):
        self.uow = UnitOfWork()

    async def sell_tour(self, sold_tour_data: CreateSoldTourSchema) -> models.SoldTour:
        sold_tour_dict = sold_tour_data.model_dump()
        async with self.uow:
            sold_tour = await self.uow.sold_tours.create(sold_tour_dict)
            await self.uow.commit()
            return sold_tour
        
    async def get_list_of_sold_tours(self) -> list[models.SoldTour]:
        async with self.uow:
            return await self.uow.sold_tours.get_all()
        
    async def get_sold_tour_by_id(self, id: int) -> models.SoldTour:
        async with self.uow:
            return await self.uow.sold_tours.get_by_id(id)

    async def update_sold_tour(self, id: int, sold_tour_data: UpdateSoldTourSchema) -> models.SoldTour:
        sold_tour_dict = sold_tour_data.model_dump()
        async with self.uow:
            sold_tour = await self.uow.sold_tours.update(id, sold_tour_dict)
            await self.uow.commit()
            return sold_tour
        
    async def delete_sold_tour(self, id: int) -> models.SoldTour:
        async with self.uow:
            sold_tour = await self.uow.sold_tours.delete(id)
            await self.uow.commit()
            return sold_tour
            
sold_tours_service = SoldToursService()

    