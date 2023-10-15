from schemas.tour_children_ages import CreateTourChildrenAgeSchema, UpdateTourChildrenAgeSchema
from database import UnitOfWork
import models

class TourChildrenAgesService:
    

    async def create_children_age(self, uow: UnitOfWork, children_age_data: CreateTourChildrenAgeSchema) -> models.TourChildrenAge:
        children_age_dict = children_age_data.model_dump()
        async with uow:
            children_age = await uow.tour_children_ages.create(children_age_dict)
            await uow.commit()
            return children_age
        
    async def get_list_of_children_ages(self, uow: UnitOfWork) -> list[models.TourChildrenAge]:
        async with uow:
            return await uow.tour_children_ages.get_all()
        
    async def get_children_age_by_id(self, uow: UnitOfWork, id: int) -> models.TourChildrenAge:
        async with uow:
            return await uow.tour_children_ages.get_by_id(id)
        
    async def update_children_age(self, uow: UnitOfWork, id: int, children_age_data: UpdateTourChildrenAgeSchema) -> models.TourChildrenAge:
        children_age_dict = children_age_data.model_dump()
        async with uow:
            children_age = await uow.tour_children_ages.update(id, children_age_dict)
            await uow.commit()
            return children_age
        
    async def delete_children_age(self, uow: UnitOfWork, id: int) -> models.TourChildrenAge:
        async with uow:
            children_age = await uow.tour_children_ages.delete(id)
            await uow.commit()
            return children_age
        

tour_children_ages_service = TourChildrenAgesService()