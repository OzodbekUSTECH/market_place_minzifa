from typing import Annotated
from fastapi import APIRouter, Depends
from services import CurrenciesService
from utils.dependency import get_currencies_services, get_current_user
from repositories import Pagination
from schemas.currencies import CurrencySchema, CreateCurrencySchema, UpdateCurrencySchema
from models import User
from security.permissionhandler import PermissionHandler, Permissions

router = APIRouter(
    prefix="/tours",
    tags=["Tours"],
)


@router.post('')
async def create_currency(
    currency_data: CreateCurrencySchema,
    currency_service: Annotated[CurrenciesService, Depends(get_currencies_services)],
):
    return await currency_service.create_currency(currency_data)

@router.get('')
async def get_list_of_tours(
    pagination: Annotated[Pagination, Depends()],
    currency_service: Annotated[CurrenciesService, Depends(get_currencies_services)],
):
    return await currency_service.get_list_of_currencies(pagination)