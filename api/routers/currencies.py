from typing import Annotated
from fastapi import APIRouter, Depends
from services import currencies_service
from repositories import Page
from schemas.currencies import (
    CurrencySchema,
    CreateCurrencySchema,
    UpdateCurrencySchema,
)
from schemas import IdResponseSchema
from utils.locale_handler import LocaleHandler
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


@router.get("/{locale}", response_model=Page[CurrencySchema])
@LocaleHandler.serialize_one_all_models_by_locale
async def get_list_of_currencies(
    uow: UOWDependency,
    locale: Annotated[LocaleHandler, Depends()],
):
    return await currencies_service.get_list_of_currencies(uow)


@router.get("/{locale}/{id}", response_model=CurrencySchema)
@LocaleHandler.serialize_one_all_models_by_locale
async def get_currency_by_id(
    uow: UOWDependency,
    locale: Annotated[LocaleHandler, Depends()],
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
