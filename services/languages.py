from schemas.languages import CreateLanguageSchema, UpdateLanguageSchema
from database import UnitOfWork
from utils.exceptions import CustomExceptions
import models
class LanguagesService:
    

    async def create_language(self, uow: UnitOfWork, language_data: CreateLanguageSchema) -> models.Language:
        language_dict = language_data.model_dump()
        async with uow:
            language = await uow.languages.create(language_dict)
            await uow.commit()
            return language
        
    async def get_list_of_languages(self, uow: UnitOfWork) -> list[models.Language]:
        async with uow:
            return await uow.languages.get_all()
        
    async def get_language_by_id(self, uow: UnitOfWork, id: int) -> models.Language:
        async with uow:
            return await uow.languages.get_by_id(id)
        
    async def update_language(self, uow: UnitOfWork, id: int, language_data: UpdateLanguageSchema) -> models.Language:
        language_dict = language_data.model_dump()
        async with uow:
            language = await uow.languages.update(id, language_dict)
            await uow.commit()
            return language

    async def delete_language(self, uow: UnitOfWork, id: int) -> models.Language:
        async with uow:
            try:
                language = await uow.languages.delete(id)
                await uow.commit()
                return language
            except:
                raise CustomExceptions.forbidden("Language cant be deleted since tours have this language")
            
languages_service = LanguagesService()