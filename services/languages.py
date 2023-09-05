from schemas.languages import CreateLanguageSchema, UpdateLanguageSchema
from repositories import Pagination
from database.unitofwork import UnitOfWork
from utils.exceptions import CustomExceptions
from models import Language

class LanguagesService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def create_language(self, language_data: CreateLanguageSchema) -> Language:
        language_dict = language_data.model_dump()
        async with self.uow:
            return await self.uow.languages.create(language_dict)
        
    async def get_list_of_languages(self, pagination: Pagination = None) -> list[Language]:
        async with self.uow:
            return await self.uow.languages.get_all(pagination)
        
    async def get_language_by_id(self, id: int) -> Language:
        async with self.uow:
            return await self.uow.languages.get_by_id(id)
        
    async def update_language(self, id: int, language_data: UpdateLanguageSchema) -> Language:
        language_dict = language_data.model_dump()
        async with self.uow:
            return await self.uow.languages.update(id, language_dict)

    async def delete_language(self, id: int) -> Language:
        async with self.uow:
            return await self.uow.languages.delete(id)