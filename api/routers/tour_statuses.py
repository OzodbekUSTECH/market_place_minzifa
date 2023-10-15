from typing import Annotated
from fastapi import APIRouter, Depends
from services import tour_statuses_service
from repositories import Page
from schemas.tour_statuses import (
    CreateTourStatusSchema,
    UpdateTourStatusSchema,
    TourStatusSchema,
)
from schemas import IdResponseSchema
from utils.locale_handler import LocaleHandler
from database import UOWDependency

router = APIRouter(
    prefix="/tour/statuses",
    tags=["Tour Statuses"],
)


@router.post("", response_model=IdResponseSchema)
async def create_status(
    uow: UOWDependency,
    tour_status_data: CreateTourStatusSchema,
):
    """
    - name: dict[str, str]\n
    for example:\n
    name: {\n
        "ru": "Статус на русском",\n
        "en": "Status in english"\n
    }
    
    """
    return await tour_statuses_service.create_status(uow, tour_status_data)


@router.get("/{locale}", response_model=Page[TourStatusSchema])
@LocaleHandler.serialize_one_all_models_by_locale
async def get_list_of_statuses(
    uow: UOWDependency,
    locale: Annotated[LocaleHandler, Depends()],
):
    return await tour_statuses_service.get_list_of_statuses(uow)


@router.get("/{locale}/{id}", response_model=TourStatusSchema)
@LocaleHandler.serialize_one_all_models_by_locale
async def get_status_by_id(
    uow: UOWDependency,
    locale: Annotated[LocaleHandler, Depends()],
    id: int,
):
    return await tour_statuses_service.get_status_by_id(uow, id)


@router.put("/{id}", response_model=IdResponseSchema)
async def update_status(
    uow: UOWDependency,
    id: int,
    tour_status_data: UpdateTourStatusSchema,
):
    """
    - name: dict[str, str]\n
    for example:\n
    name: {\n
        "ru": "Статус на русском",\n
        "en": "Status in english"\n
    }
    
    """
    return await tour_statuses_service.update_status(uow, id, tour_status_data)


@router.delete("/{id}", response_model=IdResponseSchema)
async def delete_status(
    uow: UOWDependency,
    id: int,
):
    return await tour_statuses_service.delete_status(uow, id)
