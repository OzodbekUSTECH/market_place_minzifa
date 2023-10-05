from schemas.categories import CreateCategorySchema, UpdateCategorySchema
from database import UnitOfWork
from utils.exceptions import CustomExceptions
import models

class CategoriesService:
    def __init__(self):
        self.uow = UnitOfWork()

    async def create_category(self, category_data: CreateCategorySchema) -> models.Category:
        category_dict = category_data.model_dump()
        async with self.uow:
            category = await self.uow.categories.create(category_dict)
            await self.uow.commit()
            return category
        
    async def get_list_of_categories(self) -> list[models.Category]:
        async with self.uow:
            return await self.uow.categories.get_all()
        
    async def get_category_by_id(self, id: int) -> models.Category:
        async with self.uow:
            return await self.uow.categories.get_by_id(id)
        
    async def update_category(self, id: int, category_data: UpdateCategorySchema) -> models.Category:
        category_dict = category_data.model_dump()
        async with self.uow:
            category = await self.uow.categories.update(id, category_dict)
            await self.uow.commit()
            return category

    async def delete_category(self, id: int) -> models.Category:
        async with self.uow:
            category = await self.uow.categories.delete(id)
            await self.uow.commit()
            return category
        

categories_service = CategoriesService()