from typing import Annotated
from fastapi import APIRouter, Depends
from services import tour_activity_levels_service
from repositories import Page
from schemas.tour_activity_levels import (
    CreateTourActivityLevelSchema,
    UpdateTourActivityLevelSchema,
    TourActivityLevelSchema

)
from schemas import IdResponseSchema
from utils.locale_handler import LocaleHandler
from database import UOWDependency

router = APIRouter(
    prefix="/tour/activity-levels",
    tags=["Tour Activity Levels"],
)



@router.post('', response_model=IdResponseSchema)
async def create_tour_activity_level(
    uow: UOWDependency,
    activity_level_data: CreateTourActivityLevelSchema,
):
    """
    - name: dict[str, str]\n
    for example:\n
    name: {\n
        "ru": "Спокойный",\n
        "en": "Calm"\n
    }
    """
    return await tour_activity_levels_service.create_activity_level(uow, activity_level_data)

@router.get('{locale}', response_model=Page[TourActivityLevelSchema])
@LocaleHandler.serialize_one_all_models_by_locale
async def get_list_of_tour_activity_levels(
    uow: UOWDependency,
    locale: Annotated[LocaleHandler, Depends()]
):
    return await tour_activity_levels_service.get_list_of_activity_levels(uow)

@router.get('/{locale}/{id}', response_model=TourActivityLevelSchema)
@LocaleHandler.serialize_one_all_models_by_locale
async def get_tour_activity_level_by_id(
    uow: UOWDependency,
    locale: Annotated[LocaleHandler, Depends()],
    id: int
):
    return await tour_activity_levels_service.get_activity_level_by_id(uow, id)

@router.put('/{id}', response_model=IdResponseSchema)
async def update_tour_activity_level(
    uow: UOWDependency,
    id: int,
    activity_level_data: UpdateTourActivityLevelSchema
):
    """
    - name: dict[str, str]\n
    for example:\n
    name: {\n
        "ru": "Спокойный",\n
        "en": "Calm"\n
    }
    """
    return await tour_activity_levels_service.update_activity_level(uow, id, activity_level_data)

@router.delete('/{id}', response_model=IdResponseSchema)
async def delete_tour_activity_level(
    uow: UOWDependency,
    id: int
):
    return await tour_activity_levels_service.delete_activity_level(uow, id)