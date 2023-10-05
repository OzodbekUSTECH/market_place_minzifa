from schemas.countries import CreateCountrySchema, UpdateCountrySchema
from database import UnitOfWork
from utils.exceptions import CustomExceptions
from utils.media_handler import MediaHandler
import models

class CountriesService:
    def __init__(self):
        self.uow = UnitOfWork()

    async def create_country(self, country_data: CreateCountrySchema) -> models.Country:
        country_dict = country_data.model_dump()
        filename = await MediaHandler.save_media(country_data.filename, MediaHandler.countries_media_dir)
        country_dict["filename"] = filename
        async with self.uow:
            country = await self.uow.countries.create(country_dict)
            await self.uow.commit()
            return country
        
    async def get_list_of_countries(self) -> list[models.Country]:
        async with self.uow:
            return await self.uow.countries.get_all()
        
    async def get_country_by_id(self, id: int) -> models.Country:
        async with self.uow:
            return await self.uow.countries.get_by_id(id)
        
    async def update_country(self, id: int, country_data: UpdateCountrySchema) -> models.Country:
        country_dict = country_data.model_dump(exclude={"filename"})
        if country_data.filename:
            filename = await MediaHandler.save_media(country_data.filename, MediaHandler.countries_media_dir)
            country_dict["filename"] = filename
        async with self.uow:
            country = await self.uow.countries.update(id, country_dict)
            await self.uow.commit()
            return country
        
    async def delete_country(self, id: int) -> models.Country:
        async with self.uow:
            country = await self.uow.countries.delete(id)
            await self.uow.commit()
            return country
        
countries_service = CountriesService()