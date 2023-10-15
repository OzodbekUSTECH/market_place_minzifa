from typing import Annotated
from fastapi import APIRouter, Depends
from services import accommodations_service
from repositories import Page
from schemas.accommodations import (
    CreateAccommodationSchema,
    UpdateAccommodationSchema,
    AccommodationSchema,
)
from schemas import IdResponseSchema
from utils.locale_handler import LocaleHandler
from database import UOWDependency

router = APIRouter(prefix="/accommodations", tags=["Accomodations"])


@router.post("", response_model=IdResponseSchema)
async def create_accommodation(
    uow: UOWDependency,
    accommodation_data: CreateAccommodationSchema
):
    """
    - name: dict[str, str]\n
    for example:\n
    name: {\n
        "ru": "Палатки или кемпинги",\n
        "en": "Tents or campsites"\n
    }
    
    """
    return await accommodations_service.create_accommodation(uow, accommodation_data)


@router.get("/{locale}", response_model=Page[AccommodationSchema])
@LocaleHandler.serialize_one_all_models_by_locale
async def get_list_of_accommodations(
    uow: UOWDependency,
    locale: Annotated[LocaleHandler, Depends()]
):
    return await accommodations_service.get_list_of_accommodations(uow)


@router.get("/{locale}/{id}", response_model=AccommodationSchema)
@LocaleHandler.serialize_one_all_models_by_locale
async def get_accommodation_by_id(
    uow: UOWDependency,
    locale: Annotated[LocaleHandler, Depends()],
    id: int 
):
    return await accommodations_service.get_accommodation_by_id(uow, id)


@router.put("/{id}", response_model=IdResponseSchema)
async def update_accommodation(
    uow: UOWDependency,
    id: int, 
    accommodation_data: UpdateAccommodationSchema
):
    """
    - name: dict[str, str]\n
    for example:\n
    name: {\n
        "ru": "Палатки или кемпинги",\n
        "en": "Tents or campsites"\n
    }
    
    """
    return await accommodations_service.update_accommodation(uow, id, accommodation_data)


@router.delete("/{id}", response_model=IdResponseSchema)
async def delete_accommodation(
    uow: UOWDependency,
    id: int
):
    return await accommodations_service.delete_accommodation(uow, id)
