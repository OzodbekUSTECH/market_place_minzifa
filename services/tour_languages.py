from schemas.tour_languages import CreateTourLanguageSchema, UpdateTourLanguageSchema
from repositories import Pagination
from database.unitofwork import UnitOfWork
from utils.exceptions import CustomExceptions
from models import TourLanguage

class TourLanguagesService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def create_tour_language(self, tour_language_data: CreateTourLanguageSchema) -> TourLanguage:
        tour_language_dict = tour_language_data.model_dump()
        async with self.uow:
            return await self.uow.tour_lagnuages.create(tour_language_dict)
    async def get_list_of_tours_languages(self, pagination: Pagination = None) -> list[TourLanguage]:
        async with self.uow:
            return await self.uow.tour_lagnuages.get_all(pagination)
            
    async def get_tour_language_by_id(self, id: int) -> TourLanguage:
        async with self.uow:
            return await self.uow.tour_lagnuages.get_by_id(id)
        
    async def get_languages_of_tour(self, tour_id: int) -> list[TourLanguage]:
        async with self.uow:
            tour = await self.uow.tours.get_by_id(tour_id)
            return tour.languages
        
    async def update_tour_languages(self, id: int, tour_language_data: UpdateTourLanguageSchema) -> TourLanguage:
        tour_language_dict = tour_language_data.model_dump(exclude=["tour_id"])
        async with self.uow:
            return await self.uow.tour_lagnuages.update(id, tour_language_dict)
        
    async def delete_tour_language(self, id: int) -> TourLanguage:
        async with self.uow:
            return await self.uow.tour_lagnuages.delete(id)