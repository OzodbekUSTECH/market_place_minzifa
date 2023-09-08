from schemas.languages import CreateLanguageSchema, UpdateLanguageSchema
from repositories import Pagination
from database.unitofwork import UnitOfWork
from utils.exceptions import CustomExceptions
from models import Language
from utils.locale_handler import LocaleHandler

class LanguagesService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def create_language(self, language_data: CreateLanguageSchema) -> Language:
        language_dict = language_data.model_dump()
        async with self.uow:
            return await self.uow.languages.create(language_dict)
        
    async def get_list_of_languages(self, locale: LocaleHandler, pagination: Pagination = None) -> list[Language]:
        async with self.uow:
            languages = await self.uow.languages.get_all(pagination)
            return await self.uow.serialize_one_or_all_models_by_locale(languages, locale)
        
    async def get_language_by_id(self, id: int, locale: LocaleHandler,) -> Language:
        async with self.uow:
            language = await self.uow.languages.get_by_id(id)
            return await self.uow.serialize_one_or_all_models_by_locale(language, locale)
        
    async def update_language(self, id: int, language_data: UpdateLanguageSchema) -> Language:
        language_dict = language_data.model_dump()
        async with self.uow:
            return await self.uow.languages.update(id, language_dict)

    async def delete_language(self, id: int) -> Language:
        async with self.uow:
            return await self.uow.languages.delete(id)