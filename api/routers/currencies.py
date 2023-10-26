from fastapi import APIRouter
from services import currencies_service
from repositories import Page
from schemas.currencies import (
    CurrencySchema,
    CreateCurrencySchema,
    UpdateCurrencySchema,
)
from schemas import IdResponseSchema
from database import UOWDependency

router = APIRouter(
    prefix="/currencies",
    tags=["Currencies"],
)


@router.post("", response_model=IdResponseSchema)
async def create_currency(
    uow: UOWDependency,
    currency_data: CreateCurrencySchema,
):
    """
    - name: dict[str, str]\n
    for example:\n
    name: {\n
        "ru": "Руб",\n
        "en": "Rub"\n
    }\n
    symbol: P\n
    exchange_rate: 60.53 
    
    """
    return await currencies_service.create_currency(uow, currency_data)


@router.get("", response_model=Page[CurrencySchema])
async def get_list_of_currencies(
    uow: UOWDependency,
):
    return await currencies_service.get_list_of_currencies(uow)


@router.get("/{id}", response_model=CurrencySchema)
async def get_currency_by_id(
    uow: UOWDependency,
    id: int,
):
    return await currencies_service.get_currency_by_id(uow, id)


@router.put("/{id}", response_model=IdResponseSchema)
async def update_currency(
    uow: UOWDependency,
    id: int,
    currency_data: UpdateCurrencySchema,
):
    """
    - name: dict[str, str]\n
    for example:\n
    name: {\n
        "ru": "Руб",\n
        "en": "Rub"\n
    }\n
    symbol: P\n
    exchange_rate: 60.53 
    
    """
    return await currencies_service.update_currency(uow, id, currency_data)


@router.delete("/{id}", response_model=IdResponseSchema)
async def delete_currency(uow: UOWDependency,id: int):
    return await currencies_service.delete_currency(uow, id)
