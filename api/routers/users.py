from typing import Annotated

from fastapi import APIRouter, Depends
from services.users import UsersService
from utils.dependency import get_users_services, get_current_user
from schemas.users import UserCreateSchema, UserSchema, UserUpdateSchema, TokenSchema, ResetPasswordSchema
from database.mail import EmailSender
from repositories.base import Pagination
from fastapi.security import OAuth2PasswordRequestForm
from utils.permissions import register_user, read_users, read_user, update_user, delete_user

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post('/login', name="get access token", response_model=TokenSchema)
async def login_in(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    users_service: Annotated[UsersService, Depends(get_users_services)]
) -> TokenSchema:
    """
    Get Access Token
    - param username: The email of the user.
    - param password: The password of the user.
    - return: Access Token and Type.
    """
    return await users_service.authenticate_user(form_data.username, form_data.password)


@router.get('/me', name="get own user data", response_model=UserSchema)
async def get_own_user_data(
    current_user = Depends(get_current_user),
) -> UserSchema:
    """
    Get Own User Data
    - return: User data.
    """
    return current_user

@router.post('/forgot/password', name="forgot password")
async def forgot_password(
    email: str, 
    email_sender: EmailSender = Depends()
):
    """
    Forgot Password:
    - return: Message success or error

    :send a link to reset password to the email address.
    """
    return await email_sender.send_reset_password_link(email)

@router.post('/reset/password', name="reset password")
async def reset_password(
    token: str, 
    user_password: ResetPasswordSchema,
    users_service: Annotated[UsersService, Depends(get_users_services)]
):
    """
    Reset password:
    - return: Message that password has been changed or something went wrong.
    """
    await users_service.reset_password(token, user_password.password1)

    return {"message": "password has been changed successfully"}

@router.post('', name="Registration", response_model=UserSchema)
async def create_user(
    user_data: UserCreateSchema,
    users_service: Annotated[UsersService, Depends(get_users_services)]
) -> UserSchema:
    """
    Create User:
    - return: User data.

    UserRole:
    - SUPERADMIN: СуперАдмин
    - ADMIN: Админ
    - EMPLOYEE: Сотрудник
    - DEALER: Дилер
    """
    return await users_service.register_user(user_data) 


@router.put('/{user_id}', name="Update User Data", response_model=UserSchema, dependencies=[Depends(update_user)]) #update user its permissions checker with required permission for this router
async def update_user_data(
    user_id: int, 
    user_data: UserUpdateSchema,
    users_service: Annotated[UsersService, Depends(get_users_services)]
) -> UserSchema:
    """
    Update User Data
    - param user_id: The ID of the user to update.
    - return: Updated user data.

    UserRole:
    - SUPERADMIN: СуперАдмин
    - ADMIN: Админ
    - EMPLOYEE: Сотрудник
    - DEALER: Дилер
    """
    return await users_service.update_user(user_id, user_data)



@router.get('', name="get_all_users", response_model=list[UserSchema], dependencies=[Depends(read_users)])
async def get_all_users_data(
    pagination: Annotated[Pagination, Depends()],
    users_service: Annotated[UsersService, Depends(get_users_services)]
) -> list[UserSchema]:
    """
    Get All Users Data:
    - param page: The page.
    - param page_size: The quantity of users per page.
    - return: list of all users.
    """
    users = await users_service.get_all_users(pagination)
    return users


@router.get('/{user_id}', name="get user by ID", response_model=UserSchema, dependencies=[Depends(read_user)])
async def get_user_data_by_id(
    user_id: int,
    users_service: Annotated[UsersService, Depends(get_users_services)]
) -> UserSchema:
    """
    Get User By ID:
    - param user_id: The ID of the user to get.
    - return: User data.
    """
    return await users_service.get_user_by_id(user_id)


@router.delete('/{user_id}', name="delete user data", response_model=UserSchema, dependencies=[Depends(delete_user)])
async def delete_user_data(
    user_id: int,
    users_service: Annotated[UsersService, Depends(get_users_services)]
) -> UserSchema:
    """
    Delete User:
    - param user_id: The id of the user to delete.
    - return: User data.
    """
    return await users_service.delete_user(user_id)


