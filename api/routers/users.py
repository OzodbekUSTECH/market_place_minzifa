from typing import Annotated

from fastapi import APIRouter, Depends, Form
from services import users_service
from schemas.users import (
    CreateUserSchema,
    UserSchema,
    UpdateUserSchema,
    UserSchemaWithTravelExpertAndEmployees
)
from schemas import IdResponseSchema
from repositories import Page
from utils.locale_handler import LocaleHandler
from database import UOWDependency
router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("/{locale}", response_model=IdResponseSchema)
async def create_user(
    uow: UOWDependency,
    locale: Annotated[LocaleHandler, Depends()],
    user_data: CreateUserSchema,
):
    return await users_service.register_user(uow, user_data, locale)


@router.get("", response_model=Page[UserSchemaWithTravelExpertAndEmployees])
async def get_list_of_users(uow: UOWDependency):
    return await users_service.get_list_of_users(uow)

@router.get('/role/{role_id}', response_model=Page[UserSchemaWithTravelExpertAndEmployees])
async def get_list_of_users_of_role(
    uow: UOWDependency,
    role_id: int,
):
    return await users_service.get_list_of_users_by_role_id(uow, role_id)

@router.get("/{id}", response_model=UserSchemaWithTravelExpertAndEmployees)
async def get_user_by_id(
    uow: UOWDependency,
    id: int
):
    return await users_service.get_user_by_id(uow, id)


@router.put("/{id}", response_model=IdResponseSchema)
async def update_user(
    uow: UOWDependency,
    id: int,
    user_data: UpdateUserSchema,
):
    
    return await users_service.update_user(uow, id, user_data)


@router.put("/{id}/ban", response_model=IdResponseSchema)
async def ban_or_unban_user(
    uow: UOWDependency,
    id: int,
    ban: bool = Form(),
):
    """
    - Form-data: ban = True if you want to ban the user
    - Form-data: ban = False if you want to unban the user
    """
    return await users_service.ban_or_unban_user(uow, id, ban)


@router.delete("/{id}", response_model=IdResponseSchema)
async def delete_user(
    uow: UOWDependency,
    id: int,
):
    """
    WARNING!!!!
    - BE CAREFULL TO DELETE USER, SINCE EVERYTHING THAT RELATES TO HIM WILL BE DELETED!!!
    """
    return await users_service.delete_user(uow, id)
