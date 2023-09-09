from typing import Annotated
from fastapi import APIRouter, Depends
from services import FavoriteToursService
from utils.dependency import get_favorites_services, get_current_user
from repositories import Pagination
from schemas.favorite_tours import CreateFavoriteTourSchema, UpdateFavoriteTourSchema, FavoriteTourSchema
from models import User
from security.permissionhandler import PermissionHandler, Permissions

router = APIRouter(
    prefix="/favorite/tours",
    tags=["Favorite tours"],
)

@router.post('', response_model=FavoriteTourSchema)
async def create_favorite_tour(
    favorite_tour_data:CreateFavoriteTourSchema,
    favorite_tours_service: Annotated[FavoriteToursService, Depends(get_favorites_services)]
) -> FavoriteTourSchema:
    return await favorite_tours_service.create_favorite_tour(favorite_tour_data)

@router.get('', response_model=list[FavoriteTourSchema])
async def get_list_of_favorite_touts(
    pagination: Annotated[Pagination, Depends()],
    favorite_tours_service: Annotated[FavoriteToursService, Depends(get_favorites_services)]
) -> list[FavoriteTourSchema]:
    return await favorite_tours_service.get_list_of_favorite_tours(pagination)

@router.get('/user/{user_id}', response_model=list[FavoriteTourSchema])
async def get_list_of_favorite_tours_of_user(
    user_id: int,
    pagination: Annotated[Pagination, Depends()],
    favorite_tours_service: Annotated[FavoriteToursService, Depends(get_favorites_services)]
) -> list[FavoriteTourSchema]:
    return await favorite_tours_service.get_list_of_favorite_tours_of_user(user_id, pagination)

@router.get('/{id}', response_model=FavoriteTourSchema)
async def get_favorite_tour_by_id(
    id: int,
    favorite_tours_service: Annotated[FavoriteToursService, Depends(get_favorites_services)]
) -> FavoriteTourSchema:
    return await favorite_tours_service.get_favorite_tour_by_id(id)

@router.put('/{id}', response_model=FavoriteTourSchema)
async def update_favorite_tour(
    id: int,
    favorite_tour_data: UpdateFavoriteTourSchema,
    favorite_tours_service: Annotated[FavoriteToursService, Depends(get_favorites_services)]
) -> FavoriteTourSchema:
    return await favorite_tours_service.update_favorite_tour(id, favorite_tour_data)

@router.delete('/{id}', response_model=FavoriteTourSchema)
async def delete_favorite_tour(
    id: int,
    favorite_tours_service: Annotated[FavoriteToursService, Depends(get_favorites_services)]
) -> FavoriteTourSchema:
    return await favorite_tours_service.delete_favorite_tour(id)