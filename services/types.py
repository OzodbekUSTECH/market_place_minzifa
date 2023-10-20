from schemas.types import CreateTypeSchema, UpdateTypeSchema
from database import UnitOfWork
import models
from utils.media_handler import MediaHandler

class TypesService:
    

    async def create_type(self, uow: UnitOfWork, type_data: CreateTypeSchema) -> models.Type:
        type_dict = type_data.model_dump()
        if type_data.filename:
            filename = await MediaHandler.save_media(type_data.filename, MediaHandler.types_media_dir)
            type_dict["filename"] = filename
        async with uow:
            type_instance = await uow.types.create(type_dict)
            await uow.commit()
            return type_instance
        
    async def get_list_of_types(self, uow: UnitOfWork) -> list[models.Type]:
        async with uow:
            return await uow.types.get_all()
        
    async def get_type_by_id(self, uow: UnitOfWork, id: int) -> models.Type:
        async with uow:
            return await uow.types.get_by_id(id)
        
    async def update_type(self, uow: UnitOfWork, id: int, type_data: UpdateTypeSchema) -> models.Type:
        type_dict = type_data.model_dump(exclude={"filename"})
        if type_data.filename:
            filename = await MediaHandler.save_media(type_data.filename, MediaHandler.types_media_dir)
            type_dict["filename"] = filename
        async with uow:
            type_instance = await uow.types.update(id, type_dict)
            await uow.commit()
            return type_instance        
        
    async def delete_type(self, uow: UnitOfWork, id: int) -> models.Type:
        async with uow:
            type_instance = await uow.types.delete(id)
            await uow.commit()
            return type_instance
        
types_service = TypesService()

