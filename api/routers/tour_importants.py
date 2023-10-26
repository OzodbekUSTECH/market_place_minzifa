from schemas import IdResponseSchema
from typing import Annotated
from fastapi import APIRouter, Depends
from repositories import Page
from services import tour_importants_service
from schemas.tour_importants import (
    CreateTourImportantSchema,
    UpdateTourImportantSchema,
    TourImportantSchema
)
from database import UOWDependency
from utils.locale_handler import LocaleHandler

router = APIRouter(
    prefix="/tour-importants",
    tags=["Tour Importants to know"],
)

@router.post('', response_model=IdResponseSchema)
async def create_tour_important_info_to_know(
    uow: UOWDependency,
    data: CreateTourImportantSchema
):
    return await tour_importants_service.create_tour_important(uow, data)

@router.get('/{locale}/{tour_id}', response_model=Page[TourImportantSchema])
@LocaleHandler.serialize_one_all_models_by_locale
async def get_imporants_of_tour(
    uow: UOWDependency,
    locale: Annotated[LocaleHandler, Depends()],
    tour_id: int
):
    return await tour_importants_service.get_importants_of_tour(uow, tour_id)

@router.put('/{id}',response_model=IdResponseSchema)
async def update_tour_important_info_to_know(
    uow: UOWDependency,
    id: int, 
    data: UpdateTourImportantSchema
):
    return await tour_importants_service.update_tour_important(uow, id, data)

@router.delete('/{id}', response_model=IdResponseSchema)
async def delete_tour_important_info_to_know(uow: UOWDependency, id: int):
    return await tour_importants_service.delete_tour_important(uow, id)