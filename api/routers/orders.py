from schemas.orders import (
    CreateOrderSchema,
    UpdateOrderSchema,
    OrderSchema
)
from typing import Annotated
from fastapi import APIRouter, Depends
from services import orders_service
from repositories import Page
from schemas import IdResponseSchema
from utils.locale_handler import LocaleHandler
from utils.filters.filter_orders import FilterOrderParams
from database import UOWDependency

router = APIRouter(
    prefix="/orders",
    tags=["Orders (tours)"],
)

@router.post('', response_model=IdResponseSchema)
async def create_order(
    uow: UOWDependency,
    order_data: CreateOrderSchema
):
    return await orders_service.create_order(uow, order_data)

@router.get('/{locale}', response_model=Page[OrderSchema])
@LocaleHandler.serialize_one_all_models_by_locale
async def get_orders(
    uow: UOWDependency,
    filter_params: Annotated[FilterOrderParams, Depends()],
    locale: Annotated[LocaleHandler, Depends()]
):
    return await orders_service.get_orders(uow, filter_params, locale)

@router.get('/{locale}/{id}', response_model=OrderSchema)
@LocaleHandler.serialize_one_all_models_by_locale
async def get_order_by_id(
    uow: UOWDependency,
    id: int,
    locale: Annotated[LocaleHandler, Depends()] 
):
    return await orders_service.get_order_by_id(uow, id)

@router.put('/{id}', response_model=IdResponseSchema)
async def update_order(
    uow: UOWDependency,
    id: int,
    order_data: UpdateOrderSchema
):
    return await orders_service.update_order(uow, id, order_data)

@router.delete('/{id}', response_model=IdResponseSchema)
async def delete_order(
    uow: UOWDependency,
    id: int
):
    return await orders_service.delete_order(uow, id)