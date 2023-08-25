from typing import Annotated
from fastapi import APIRouter, Depends
from services import CurrenciesService
from utils.dependency import get_currencies_services, get_current_user
from repositories import Pagination
from schemas.currencies import CurrencySchema, CreateCurrencySchema, UpdateCurrencySchema
from models import User
from security.permissionhandler import PermissionHandler, Permissions

router = APIRouter(
    prefix="/currencies",
    tags=["Currencies"],
)


@router.post('')
async def create_currency(
    currency_data: CreateCurrencySchema,
    currencies_service: Annotated[CurrenciesService, Depends(get_currencies_services)],
):
    created_currency = await currencies_service.create_currency(currency_data)
    return created_currency

@router.get('')
async def get_list_of_tours(
    pagination: Annotated[Pagination, Depends()],
    currencies_service: Annotated[CurrenciesService, Depends(get_currencies_services)],
):
    return await currencies_service.get_list_of_currencies(pagination)