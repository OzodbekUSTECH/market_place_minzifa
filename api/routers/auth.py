from typing import Annotated
from fastapi import APIRouter, Depends, Form
from pydantic import EmailStr
from services import users_service
from utils.dependency import get_current_user
from schemas.users import (
    TokenSchema,
    ResetPasswordSchema,
    UserSchemaWithTravelExpertAndEmployees
)
from schemas import IdResponseSchema
from fastapi.security import OAuth2PasswordRequestForm
from database import UOWDependency

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/login", response_model=TokenSchema)
async def get_access_token(
    uow: UOWDependency,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
):
    return await users_service.authenticate_user(uow, form_data.username, form_data.password)


@router.get("/me", response_model=UserSchemaWithTravelExpertAndEmployees)
async def get_own_user(
    current_user=Depends(get_current_user),
):
    return current_user


@router.post("/{locale}/forgot/password")
async def forgot_password(
    uow: UOWDependency,
    locale: str,
    email: EmailStr = Form()
):
    """
    Forgot Password:
    - return: Message success or raise error

    send a link to reset password to the email address.
    """
    return await users_service.send_reset_password_link(uow, locale, email)


@router.put("/reset/password/{token}", response_model=IdResponseSchema)
async def reset_password(
    uow: UOWDependency,
    token: str,
    password_data: ResetPasswordSchema,
):
    return await users_service.reset_password(uow, token, password_data)
