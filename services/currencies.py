from schemas.currencies import CreateCurrencySchema, UpdateCurrencySchema
from database.unitofwork import UnitOfWork
from utils.exceptions import CustomExceptions
import models

class CurrenciesService:
    

    async def create_currency(self, uow: UnitOfWork, currency_data: CreateCurrencySchema) -> models.Currency:
        currency_dict = currency_data.model_dump()
        async with uow:
            currency = await uow.currencies.create(currency_dict)
            await uow.commit()
            return currency
        
    async def get_list_of_currencies(self, uow: UnitOfWork) -> list[models.Currency]:
        async with uow:
            return await uow.currencies.get_all() 
    
    async def get_currency_by_id(self, uow: UnitOfWork, id: int) -> models.Currency:
        async with uow:
            return await uow.currencies.get_by_id(id)
        
    async def update_currency(self, uow: UnitOfWork, id: int, currency_data: UpdateCurrencySchema) -> models.Currency:
        currency_dict = currency_data.model_dump()
        async with uow:
            currency = await uow.currencies.update(id, currency_dict)
            await uow.commit()
            return currency
        
    async def delete_currency(self, uow: UnitOfWork, currency_id: int) -> models.Currency:
        async with uow:
            try:
                currency = await uow.currencies.delete(currency_id)
                await uow.commit()
                return currency
            except:
                raise CustomExceptions.forbidden("Currency cant be deleted cause prices of tours use this currency")
            

currencies_service = CurrenciesService()