from typing import Annotated
from fastapi import APIRouter, Depends
from services import tour_children_ages_service
from repositories import Page
from schemas.tour_children_ages import (
    CreateTourChildrenAgeSchema,
    UpdateTourChildrenAgeSchema,
    TourChildrenAgeSchema,
)
from schemas import IdResponseSchema
from utils.locale_handler import LocaleHandler

router = APIRouter(
    prefix="/tour/children-ages",
    tags=["Tour Children Ages"],
)


@router.post("", response_model=IdResponseSchema)
async def create_tour_children_age(children_age_data: CreateTourChildrenAgeSchema):
    """
    - name: dict[str, str]\n
    for example:\n
    name: {\n
        "ru": "1 год",\n
        "en": "1 Year"\n
    }

    """
    return await tour_children_ages_service.create_children_age(children_age_data)


@router.get("/{locale}", response_model=Page[TourChildrenAgeSchema])
@LocaleHandler.serialize_one_all_models_by_locale
async def get_list_of_tour_children_ages(
    locale: Annotated[LocaleHandler, Depends()],
):
    return await tour_children_ages_service.get_list_of_children_ages()


@router.get("/{locale}/{id}", response_model=TourChildrenAgeSchema)
@LocaleHandler.serialize_one_all_models_by_locale
async def get_tour_children_age_by_id(
    locale: Annotated[LocaleHandler, Depends()],
    id: int,
):
    return await tour_children_ages_service.get_children_age_by_id(id)


@router.put("/{id}", response_model=IdResponseSchema)
async def update_tour_children_age(
    id: int, children_age_data: UpdateTourChildrenAgeSchema
):
    """
    - name: dict[str, str]\n
    for example:\n
    name: {\n
        "ru": "1 год",\n
        "en": "1 Year"\n
    }

    """
    return await tour_children_ages_service.update_children_age(id, children_age_data)


@router.delete("/{id}", response_model=IdResponseSchema)
async def delete_tour_children_age(
    id: int,
):
    return await tour_children_ages_service.delete_children_age(id)
