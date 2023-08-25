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
            created_currency = await self.uow.currencies.create(currency_dict)
            await self.uow.commit()
            return created_currency
        
    async def get_list_of_currencies(self, pagination: Pagination) -> list[CurrencySchema]:
        async with self.uow:
            list_of_currencies = await self.uow.currencies.get_all(pagination)
            await self.uow.commit()
            return list_of_currencies