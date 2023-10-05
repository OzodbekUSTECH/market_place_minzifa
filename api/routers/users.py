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
router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("/{locale}", response_model=IdResponseSchema)
async def create_user(
    locale: Annotated[LocaleHandler, Depends()],
    user_data: CreateUserSchema,
):
    return await users_service.register_user(user_data, locale)


@router.get("", response_model=Page[UserSchemaWithTravelExpertAndEmployees])
async def get_list_of_users():
    return await users_service.get_list_of_users()

@router.get('/role/{role_id}', response_model=Page[UserSchemaWithTravelExpertAndEmployees])
async def get_list_of_users_of_role(
    role_id: int,
):
    return await users_service.get_list_of_users_by_role_id(role_id)

@router.get("/{id}", response_model=UserSchemaWithTravelExpertAndEmployees)
async def get_user_by_id(id: int) -> UserSchema:
    return await users_service.get_user_by_id(id)


@router.put("/{id}", response_model=IdResponseSchema)
async def update_user(
    id: int,
    user_data: UpdateUserSchema,
):
    
    return await users_service.update_user(id, user_data)


@router.put("/{id}/ban", response_model=IdResponseSchema)
async def ban_or_unban_user(
    id: int,
    ban: bool = Form(),
):
    """
    - Form-data: ban = True if you want to ban the user
    - Form-data: ban = False if you want to unban the user
    """
    return await users_service.ban_or_unban_user(id, ban)


@router.delete("/{id}", response_model=IdResponseSchema)
async def delete_user(
    id: int,
):
    """
    WARNING!!!!
    - BE CAREFULL TO DELETE USER, SINCE EVERYTHING THAT RELATES TO HIM WILL BE DELETED!!!
    """
    return await users_service.delete_user(id)
