from schemas.currencies import CreateCurrencySchema, UpdateCurrencySchema
from database.unitofwork import UnitOfWork
from utils.exceptions import CustomExceptions
import models

class CurrenciesService:
    def __init__(self):
        self.uow = UnitOfWork()

    async def create_currency(self, currency_data: CreateCurrencySchema) -> models.Currency:
        currency_dict = currency_data.model_dump()
        async with self.uow:
            currency = await self.uow.currencies.create(currency_dict)
            await self.uow.commit()
            return currency
        
    async def get_list_of_currencies(self) -> list[models.Currency]:
        async with self.uow:
            return await self.uow.currencies.get_all() 
    
    async def get_currency_by_id(self, id: int) -> models.Currency:
        async with self.uow:
            return await self.uow.currencies.get_by_id(id)
        
    async def update_currency(self, id: int, currency_data: UpdateCurrencySchema) -> models.Currency:
        currency_dict = currency_data.model_dump()
        async with self.uow:
            currency = await self.uow.currencies.update(id, currency_dict)
            await self.uow.commit()
            return currency
        
    async def delete_currency(self, currency_id: int) -> models.Currency:
        async with self.uow:
            try:
                currency = await self.uow.currencies.delete(currency_id)
                await self.uow.commit()
                return currency
            except:
                raise CustomExceptions.forbidden("Currency cant be deleted cause prices of tours use this currency")
            

currencies_service = CurrenciesService()