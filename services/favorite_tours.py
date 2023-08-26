from schemas.favorite_tours import CreateFavoriteTourSchema, UpdateFavoriteTourSchema, FavoriteTourSchema
from repositories import Pagination
from database.unitofwork import UnitOfWork
from utils.exceptions import CustomExceptions


class FavoriteToursService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow


    async def create_favorite_tour(self, favorite_tour_data: CreateFavoriteTourSchema) -> FavoriteTourSchema:
        favorite_tour_dict = favorite_tour_data.model_dump()
        async with self.uow:
            return await self.uow.favorite_tours.create(favorite_tour_dict)
        
    async def get_list_of_favorite_tours(self, pagination: Pagination) -> list[FavoriteTourSchema]:
        async with self.uow:
            return await self.uow.favorite_tours.get_all(pagination)
        
    async def get_list_of_favorite_tours_of_user(self, user_id: int, pagination: Pagination) -> list[FavoriteTourSchema]:
        async with self.uow:
            return await self.uow.favorite_tours.get_list_of_favorite_tours_of_user(user_id, pagination)

    async def get_favorite_tour_by_id(self, favorite_tour_id: int) -> FavoriteTourSchema:
        async with self.uow:
            return await self.uow.favorite_tours.get_by_id(favorite_tour_id)
        
    async def update_favorite_tour(self, favorite_tour_id: int, favorite_tour_data: UpdateFavoriteTourSchema) -> FavoriteTourSchema:
        favorite_tour_dict = favorite_tour_data.model_dump()
        async with self.uow:
            return await self.uow.favorite_tours.update(favorite_tour_id, favorite_tour_dict)
        
    async def delete_favorite_tour(self, favorite_tour_id: int) -> FavoriteTourSchema:
        async with self.uow:
            return await self.uow.favorite_tours.delete(favorite_tour_id)
        
    
    