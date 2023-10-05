from schemas.types import CreateTypeSchema, UpdateTypeSchema
from database import UnitOfWork
from utils.exceptions import CustomExceptions
import models

class TypesService:
    def __init__(self):
        self.uow = UnitOfWork()

    async def create_type(self, type_data: CreateTypeSchema) -> models.Type:
        type_dict = type_data.model_dump()
        async with self.uow:
            type_instance = await self.uow.types.create(type_dict)
            await self.uow.commit()
            return type_instance
        
    async def get_list_of_types(self) -> list[models.Type]:
        async with self.uow:
            return await self.uow.types.get_all()
        
    async def get_type_by_id(self, id: int) -> models.Type:
        async with self.uow:
            return await self.uow.types.get_by_id(id)
        
    async def update_type(self, id: int, type_data: UpdateTypeSchema) -> models.Type:
        type_dict = type_data.model_dump()
        async with self.uow:
            type_instance = await self.uow.types.update(id, type_dict)
            await self.uow.commit()
            return type_instance        
        
    async def delete_type(self, id: int) -> models.Type:
        async with self.uow:
            type_instance = await self.uow.types.delete(id)
            await self.uow.commit()
            return type_instance
        
types_service = TypesService()

