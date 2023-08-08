from typing import Annotated

from fastapi import APIRouter, Depends, Query
from services.users import UsersService
from utils.dependency import get_users_services, get_current_user, RoleChecker
from schemas.users import UserCreateSchema, UserSchema, UserUpdateSchema, Token, ResetPasswordSchema
from database.mail import EmailSender
from utils.password import PasswordHandler
from repositories.base import Pagination
from fastapi import BackgroundTasks
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import EmailStr
router = APIRouter(
    prefix="/users",
    tags=["Authentication"],
)


@router.post('/login', name="get access token", response_model=Token)
async def login_in(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    users_service: UsersService = Depends(get_users_services)
):
    return await users_service.authenticate_user(form_data.username, form_data.password)

@router.post('/forgot/password', name="forgot password")
async def forgot_password(email: str, email_sender: EmailSender = Depends()):
    return await email_sender.send_reset_password_link(email)

@router.post('/reset/password', name="reset password")
async def reset_password(
    token: str, 
    user_password: ResetPasswordSchema,
    users_service: UsersService = Depends(get_users_services)
):
    await users_service.reset_password(token, user_password.password1)

    return {"message": "password has been changed successfully"}

@router.post('', name="Registration", response_model=UserSchema)
async def create_user(
    user_data: UserCreateSchema,
    users_service: UsersService = Depends(get_users_services)
):
   
    new_user = await users_service.register_user(user_data)    
    return new_user


@router.post('/update', name="Update User Data", response_model=UserSchema, dependencies=[Depends(get_current_user)])
async def update_user_data(
    user_id: int, 
    user_data: UserUpdateSchema,
    users_service: UsersService = Depends(get_users_services)
):
    """
    UserRole\n
    SUPERADMIN = "СуперАдмин"\n
    ADMIN = "Админ"\n
    EMPLOYEE = "Сотрудник"\n
    DEALER = "Дилер"
    """
    updated_user = await users_service.update_user(user_id, user_data)
    return updated_user


@router.get('', name="get_all_users", response_model=list[UserSchema])
async def get_all_users_data(
    pagination: Pagination = Depends(),
    users_service: UsersService = Depends(get_users_services)
):
    users = await users_service.get_all_users(pagination)
    return users


@router.get('/{user_id}', name="get user by ID", response_model=UserSchema)
async def get_user_data_by_id(
    user_id: int,
    users_service: UsersService = Depends(get_users_services)
):
    user = await users_service.get_user_by_id(user_id)

    return user


@router.delete('/{user_id}', name="delete user data", response_model=UserSchema)
async def delete_user_data(
    user_id: int,
    users_service: UsersService = Depends(get_users_services)
):
    return await users_service.delete_user(user_id)


@router.get('/own/me', name="get own user data", response_model=UserSchema)
async def get_own_user_data(
    current_user =Depends(get_current_user),
    users_service: UsersService = Depends(get_users_services)
):
    return await users_service.get_user_by_id(current_user.id)