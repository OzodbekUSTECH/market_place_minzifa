from schemas.languages import CreateLanguageSchema, UpdateLanguageSchema
from database import UnitOfWork
from utils.exceptions import CustomExceptions
import models
class LanguagesService:
    def __init__(self):
        self.uow = UnitOfWork()

    async def create_language(self, language_data: CreateLanguageSchema) -> models.Language:
        language_dict = language_data.model_dump()
        async with self.uow:
            language = await self.uow.languages.create(language_dict)
            await self.uow.commit()
            return language
        
    async def get_list_of_languages(self) -> list[models.Language]:
        async with self.uow:
            return await self.uow.languages.get_all()
        
    async def get_language_by_id(self, id: int) -> models.Language:
        async with self.uow:
            return await self.uow.languages.get_by_id(id)
        
    async def update_language(self, id: int, language_data: UpdateLanguageSchema) -> models.Language:
        language_dict = language_data.model_dump()
        async with self.uow:
            language = await self.uow.languages.update(id, language_dict)
            await self.uow.commit()
            return language

    async def delete_language(self, id: int) -> models.Language:
        async with self.uow:
            try:
                language = await self.uow.languages.delete(id)
                await self.uow.commit()
                return language
            except:
                raise CustomExceptions.forbidden("Language cant be deleted since tours have this language")
            
languages_service = LanguagesService()