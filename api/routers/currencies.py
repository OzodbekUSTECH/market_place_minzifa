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


@router.post('', response_model=CurrencySchema)
async def create_currency(
    currency_data: CreateCurrencySchema,
    currencies_service: Annotated[CurrenciesService, Depends(get_currencies_services)],
) -> CurrencySchema:
    return await currencies_service.create_currency(currency_data)

@router.get('', response_model=list[CurrencySchema])
async def get_list_of_currencies(
    pagination: Annotated[Pagination, Depends()],
    currencies_service: Annotated[CurrenciesService, Depends(get_currencies_services)],
) -> list[CurrencySchema]:
    return await currencies_service.get_list_of_currencies(pagination)

@router.get('/{id}', response_model=CurrencySchema)
async def get_currency_by_id(
    id: int,
    currencies_service: Annotated[CurrenciesService, Depends(get_currencies_services)],
) -> CurrencySchema:
    return await currencies_service.get_currency_by_id(id)

@router.put('/{id}', response_model=CurrencySchema)
async def update_currency(
    id: int,
    currency_data: UpdateCurrencySchema,
    currencies_service: Annotated[CurrenciesService, Depends(get_currencies_services)],
) -> CurrencySchema:
    return await currencies_service.update_currency(id, currency_data)

@router.delete('/{id}', response_model=CurrencySchema)
async def delete_currency(
    id: int,
    currencies_service: Annotated[CurrenciesService, Depends(get_currencies_services)],
) -> CurrencySchema:
    return await currencies_service.delete_currency(id)