from schemas.tour_languages import CreateTourLanguageSchema, UpdateTourLanguageSchema, TourLanguageSchema
from typing import Annotated
from fastapi import APIRouter, Depends
from services import TourLanguagesService
from utils.dependency import get_tour_languages_services, get_current_user
from repositories import Pagination
from models import User
from security.permissionhandler import PermissionHandler, Permissions

router = APIRouter(
    prefix="/tour/languages",
    tags=["Tour Languages"],
)


@router.post('', response_model=TourLanguageSchema)
async def create_tour_language(
    tour_language_data: CreateTourLanguageSchema,
    tour_languages_service: Annotated[TourLanguagesService, Depends(get_tour_languages_services)]
):
    return await tour_languages_service.create_tour_language(tour_language_data)

@router.get('', response_model=list[TourLanguageSchema])
async def get_list_of_tours_languages(
    pagination: Annotated[Pagination, Depends()],
    tour_languages_service: Annotated[TourLanguagesService, Depends(get_tour_languages_services)]
):
    return await tour_languages_service.get_list_of_tours_languages(pagination)

@router.get('/tour/{tour_id}', response_model=list[TourLanguageSchema])
async def get_languages_of_tour(
    tour_id: int,
    tour_languages_service: Annotated[TourLanguagesService, Depends(get_tour_languages_services)]
):
    return await tour_languages_service.get_languages_of_tour(tour_id)
    
@router.get('/{id}', response_model=TourLanguageSchema)
async def get_tour_language_by_id(
    id: int,
    tour_languages_service: Annotated[TourLanguagesService, Depends(get_tour_languages_services)]
):
    return await tour_languages_service.get_tour_language_by_id(id)


@router.put('/{id}', response_model=TourLanguageSchema)
async def update_tour_languages(
    tour_language_data: UpdateTourLanguageSchema,
    tour_languages_service: Annotated[TourLanguagesService, Depends(get_tour_languages_services)]
):
    return await tour_languages_service.update_tour_languages(tour_language_data)

@router.delete('/{id}', response_model=TourLanguageSchema)
async def delete_tour_language(
    id: int,
    tour_languages_service: Annotated[TourLanguagesService, Depends(get_tour_languages_services)]
):
    return await tour_languages_service.delete_tour_language(id)