from schemas.tour_children_ages import CreateTourChildrenAgeSchema, UpdateTourChildrenAgeSchema
from database import UnitOfWork
from utils.exceptions import CustomExceptions
import models

class TourChildrenAgesService:
    def __init__(self):
        self.uow = UnitOfWork()

    async def create_children_age(self, children_age_data: CreateTourChildrenAgeSchema) -> models.TourChildrenAge:
        children_age_dict = children_age_data.model_dump()
        async with self.uow:
            children_age = await self.uow.tour_children_ages.create(children_age_dict)
            await self.uow.commit()
            return children_age
        
    async def get_list_of_children_ages(self) -> list[models.TourChildrenAge]:
        async with self.uow:
            return await self.uow.tour_children_ages.get_all()
        
    async def get_children_age_by_id(self, id: int) -> models.TourChildrenAge:
        async with self.uow:
            return await self.uow.tour_children_ages.get_by_id(id)
        
    async def update_children_age(self, id: int, children_age_data: UpdateTourChildrenAgeSchema) -> models.TourChildrenAge:
        children_age_dict = children_age_data.model_dump()
        async with self.uow:
            children_age = await self.uow.tour_children_ages.update(id, children_age_dict)
            await self.uow.commit()
            return children_age
        
    async def delete_children_age(self, id: int) -> models.TourChildrenAge:
        async with self.uow:
            children_age = await self.uow.tour_children_ages.delete(id)
            await self.uow.commit()
            return children_age
        

tour_children_ages_service = TourChildrenAgesService()