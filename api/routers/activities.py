from typing import Annotated
from fastapi import APIRouter, Depends
from services import activities_service
from repositories import Page
from schemas.activities import (
    CreateActivitySchema,
    UpdateActivitySchema,
    ActivitySchema,
)
from schemas import IdResponseSchema
from utils.locale_handler import LocaleHandler

router = APIRouter(
    prefix="/activities",
    tags=["Acitivities"],
)


@router.post("", response_model=IdResponseSchema)
async def create_activity(
    activity_data: CreateActivitySchema,
) -> ActivitySchema:
    """
    - name: dict[str, str]\n
    for example:\n
    name: {\n
        "ru": "Активность на русском",\n
        "en": "Acitivity in english"\n
    }
    """
    return await activities_service.create_activity(activity_data)


@router.get("/{locale}", response_model=Page[ActivitySchema])
@LocaleHandler.serialize_one_all_models_by_locale
async def get_list_of_activities(
    locale: Annotated[LocaleHandler, Depends()],
) -> list[ActivitySchema]:
    return await activities_service.get_list_of_activities()


@router.get("/{locale}/{id}", response_model=ActivitySchema)
@LocaleHandler.serialize_one_all_models_by_locale
async def get_activity_by_id(
    locale: Annotated[LocaleHandler, Depends()],
    id: int,
) -> ActivitySchema:
    return await activities_service.get_activity_by_id(id)


@router.put("/{id}", response_model=IdResponseSchema)
async def update_activity(
    id: int,
    activity_data: UpdateActivitySchema,
) -> ActivitySchema:
    """
    - name: dict[str, str]\n
    for example:\n
    name: {\n
        "ru": "Активность на русском",\n
        "en": "Acitivity in english"\n
    }
    """
    return await activities_service.update_activity(id, activity_data)


@router.delete("/{id}", response_model=IdResponseSchema)
async def delete_activity(
    id: int,
) -> ActivitySchema:
    return await activities_service.delete_activity(id)
