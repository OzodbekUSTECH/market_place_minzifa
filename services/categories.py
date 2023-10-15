from schemas.categories import CreateCategorySchema, UpdateCategorySchema
from database import UnitOfWork
import models

class CategoriesService:
    

    async def create_category(self, uow: UnitOfWork, category_data: CreateCategorySchema) -> models.Category:
        category_dict = category_data.model_dump()
        async with uow:
            category = await uow.categories.create(category_dict)
            await uow.commit()
            return category
        
    async def get_list_of_categories(self, uow: UnitOfWork) -> list[models.Category]:
        async with uow:
            return await uow.categories.get_all()
        
    async def get_category_by_id(self, uow: UnitOfWork, id: int) -> models.Category:
        async with uow:
            return await uow.categories.get_by_id(id)
        
    async def update_category(self, uow: UnitOfWork, id: int, category_data: UpdateCategorySchema) -> models.Category:
        category_dict = category_data.model_dump()
        async with uow:
            category = await uow.categories.update(id, category_dict)
            await uow.commit()
            return category

    async def delete_category(self, uow: UnitOfWork, id: int) -> models.Category:
        async with uow:
            category = await uow.categories.delete(id)
            await uow.commit()
            return category
        

categories_service = CategoriesService()