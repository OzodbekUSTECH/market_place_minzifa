from schemas.currencies import CreateCurrencySchema, UpdateCurrencySchema, CurrencySchema
from repositories import Pagination
from datetime import datetime
from database.unitofwork import UnitOfWork
from utils.exceptions import CustomExceptions

class CurrenciesService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def create_currency(self, currency_data: CreateCurrencySchema) -> CurrencySchema:
        currency_dict = currency_data.model_dump()
        async with self.uow:
            return await self.uow.currencies.create(currency_dict)
        
    async def get_list_of_currencies(self, pagination: Pagination) -> list[CurrencySchema]:
        async with self.uow:
            list_of_currencies = await self.uow.currencies.get_all(pagination)
            return list_of_currencies 
    
    async def get_currency_by_id(self, currency_id: int) -> CurrencySchema:
        async with self.uow:
            return await self.uow.currencies.get_by_id(currency_id)
        
    async def update_currency(self, currency_id: int, currency_data: UpdateCurrencySchema) -> CurrencySchema:
        currency_dict = currency_data.model_dump()
        async with self.uow:
            return await self.uow.currencies.update(currency_id, currency_dict)
        
    async def delete_currency(self, currency_id: int) -> CurrencySchema:
        async with self.uow:
            return await self.uow.currencies.delete(currency_id)