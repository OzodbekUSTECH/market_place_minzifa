from typing import Annotated
from fastapi import APIRouter, Depends
from services import roles_service
from schemas.roles import (
    RoleSchema,
    CreateRoleSchema,
    UpdateRoleSchema,
)
from schemas import IdResponseSchema
from repositories import Page
from utils.locale_handler import LocaleHandler
from database import UOWDependency

router = APIRouter(
    prefix="/roles",
    tags=["Roles"],
)


@router.post("", response_model=IdResponseSchema)
async def create_role(
    uow: UOWDependency,
    role_data: CreateRoleSchema,
) -> RoleSchema:
    """
    - name: dict[str, str]\n
    for example:\n
    name: {\n
        "ru": "Название роли на русском",\n
        "en": "Name of the role in english"\n
    }
    """
    return await roles_service.create_role(uow, role_data)


@router.get("/{locale}", response_model=Page[RoleSchema])
@LocaleHandler.serialize_one_all_models_by_locale
async def get_list_of_roles(
    uow: UOWDependency,
    locale: Annotated[LocaleHandler, Depends()],
) -> list[RoleSchema]:
    """
    LOCALE:
    - ru/en/etc: returns data in chosen language
    - returns all languages if your LOCALE doesnt exist
    """
    return await roles_service.get_all_roles(uow)


@router.get("/{locale}/{id}", name="get role by ID", response_model=RoleSchema)
@LocaleHandler.serialize_one_all_models_by_locale
async def get_role_data_by_id(
    uow: UOWDependency,
    locale: Annotated[LocaleHandler, Depends()],
    id: int,
) -> RoleSchema:
    """
    LOCALE:
    - ru/en/etc: returns data in chosen language
    - returns all languages if your LOCALE doesnt exist
    """
    return await roles_service.get_role_by_id(uow, id)


@router.put("/{id}", response_model=IdResponseSchema)
async def update_role(
    uow: UOWDependency,
    id: int,
    role_data: UpdateRoleSchema,
) -> RoleSchema:
    """
    - name: dict[str, str]\n
    for example:\n
    name: {\n
        "ru": "Название роли на русском",\n
        "en": "Name of the role in english"\n
    }
    """
    return await roles_service.update_role(uow, id, role_data)


@router.delete("/{id}", response_model=IdResponseSchema)
async def delete_role(
    uow: UOWDependency,
    id: int,
) -> RoleSchema:
    return await roles_service.delete_role(uow, id)
