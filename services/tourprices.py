from schemas.tour_prices import CreateTourPriceSchema, UpdateTourPriceSchema
from repositories import Pagination
from datetime import datetime
from models import TourPrice, Currency
from database.unitofwork import UnitOfWork
from utils.exceptions import CustomExceptions
from utils.currency_handler import CurrencyHandler
from utils.tour_prices import TourPriceHandler

class TourPricesService:
    def __init__(self):
        self.uow = UnitOfWork()

    
    async def _create_prices_for_tour(self, price_data: CreateTourPriceSchema) -> None:
        base_currency = await self.uow.currencies.get_by_id(price_data.currency_id)
        target_currencies = await self.uow.currencies.get_all_without_pagination()
        data_list = []

        for target_currency in target_currencies:
            price_dict = await TourPriceHandler.create_price_dict(
                target_currency, base_currency, price_data
            )
            data_list.append(price_dict)
        
        await self.uow.tour_prices.bulk_create(data_list)

    # async def create_tour_prices(self, price_data: CreateTourPriceSchema) -> None:
        
    #     await self._create_prices_for_tour(price_data)
        
   
    # async def _update_prices_for_tour(self, price_data: UpdateTourPriceSchema) -> list[TourPrice]:
    #     target_currencies = await self.uow.tour_prices.get_by_tour_id(price_data.tour_id)
    #     base_currency = await self.uow.currencies.get_by_id(price_data.currency_id)

    #     response = []
    #     for target_currency in target_currencies:
    #         price_dict = await TourPriceHandler.create_price_dict(
    #             target_currency.currency, base_currency, price_data
    #         )
    #         updated_price = await self.uow.tour_prices.update(target_currency.id, price_dict)
    #         response.append(updated_price)
    #     return response
    
    # async def update_tour_prices(self, price_data: UpdateTourPriceSchema) -> list[TourPrice]:
    #     async with self.uow:
    #         return await self._update_prices_for_tour(price_data)
    

        
tour_prices_service = TourPricesService()
    