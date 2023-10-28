from typing import Annotated
from fastapi import APIRouter, Depends
from services import favorite_tours_service
from repositories import Page
from schemas.tours_package.favorite_tours import (
    CreateFavoriteTourSchema,
    FavoriteTourSchema
)
from schemas import IdResponseSchema
from database import UOWDependency
from utils.locale_handler import LocaleHandler

router = APIRouter(
    prefix="/favorite-tours",
    tags=["Favorite tours"],
)

@router.post('', response_model=IdResponseSchema)
async def create_favorite_tour(
    uow: UOWDependency,
    favorite_tour_data: CreateFavoriteTourSchema,
):
    return await favorite_tours_service.create_favorite_tour(uow, favorite_tour_data)

@router.get('/{user_id}', response_model=Page[FavoriteTourSchema])
@LocaleHandler.serialize_one_all_models_by_locale
async def get_favorite_tours_of_user(
    uow: UOWDependency,
    locale: Annotated[LocaleHandler, Depends()],
    user_id: int
):
    return await favorite_tours_service.get_favorite_tours_of_user(uow, user_id)

@router.delete('/{id}', response_model=IdResponseSchema)
async def delete_favorite_tour(
    uow: UOWDependency,
    id: int
):
    return await favorite_tours_service.delete_favorite_tour(uow, id)