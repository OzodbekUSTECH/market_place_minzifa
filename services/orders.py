from schemas.orders import (
    CreateOrderSchema,
    UpdateOrderSchema
)
from repositories import paginate
from utils.filters.filter_orders import FilterOrderParams
from utils.locale_handler import LocaleHandler
from database import UnitOfWork
from utils.exceptions import CustomExceptions
import models

class OrdersService:
    
    async def create_order(self, uow: UnitOfWork, order_data: CreateOrderSchema) -> models.Order:
        async with uow:
            order = await uow.orders.create(order_data.model_dump())
            await uow.commit()
            return order
        
    async def get_orders(
            self,
            uow: UnitOfWork,
            filter_params: FilterOrderParams,
            locale: LocaleHandler
    ) -> list[models.Order]:
        async with uow:

            orders: list[models.Order] = await uow.orders.get_all()
            filtered_orders = await filter_params.get_filtered_items(orders.items, locale)
            return paginate(filtered_orders)        
        

    async def get_order_by_id(self, uow: UnitOfWork, id: int) -> models.Order:
        async with uow:
            return await uow.orders.get_by_id(id)
        
    async def update_order(self, uow: UnitOfWork, id: int, order_data: UpdateOrderSchema) -> models.Order:
        async with uow:
            order: models.Order = await uow.orders.get_by_id(id)
            await uow.orders.update(order.id, order_data.model_dump())
            await uow.commit()
            return order
        
    async def delete_order(self, uow: UnitOfWork, id: int) -> models.Order:
        async with uow:
            order: models.Order = await uow.orders.get_by_id(id)
            await uow.orders.delete(order.id)
            await uow.commit()
            return order
        
orders_service = OrdersService()