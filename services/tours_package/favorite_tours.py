from schemas.tours_package.favorite_tours import (
    CreateFavoriteTourSchema
)
from database import UnitOfWork
import models
class FavoriteToursService:

    async def create_favorite_tour(self, uow: UnitOfWork, favorite_tour_data: CreateFavoriteTourSchema) -> models.FavoriteTour:
        async with uow:
            favorite_tour = await uow.favorite_tours.create(favorite_tour_data.model_dump())
            await uow.commit()
            return favorite_tour
        
    async def get_favorite_tours_of_user(self, uow: UnitOfWork, user_id: int) -> list[models.FavoriteTour]:
        async with uow:
            return await uow.favorite_tours.get_all_by(user_id=user_id)
        
    async def delete_favorite_tour(self, uow: UnitOfWork, id: int) -> models.FavoriteTour:
        async with uow:
            favorite_tour: models.FavoriteTour = await uow.favorite_tours.get_by_id(id)
            await uow.favorite_tours.delete(favorite_tour.id)
            await uow.commit()
            return favorite_tour
        
favorite_tours_service = FavoriteToursService()