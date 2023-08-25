from schemas.tourprices import CreateTourPriceSchema, UpdateTourPriceSchema, TourPriceSchema
from repositories import Pagination
from datetime import datetime
from models import Tour
from database.unitofwork import UnitOfWork
from utils.exceptions import CustomExceptions
from utils.currency import CurrencyHandler

class TourPricesService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def _create_prices_for_tour(self, price_data: CreateTourPriceSchema):
        base_currency = await self.uow.currencies.get_by_name('USD')
        target_currencies = await self.uow.currencies.get_all()
        response = []        
        for target_currency in target_currencies:
            converted_price = price_data.price if target_currency == base_currency else price_data.price * target_currency.exchange_rate
            
            
            price_dict = {
                "tour_id": price_data.tour_id,
                "currency_id": target_currency.id,
                "price": converted_price
            }
            created_price = await self.uow.tour_prices.create(price_dict)
            response.append(TourPriceSchema(**created_price.__dict__))
        return response
    
    async def create_tour_prices(self, price_data: CreateTourPriceSchema) -> list[TourPriceSchema]:
        async with self.uow:
            list_of_prices_for_tour = await self._create_prices_for_tour(price_data)
            return list_of_prices_for_tour
        
    async def get_list_of_prices(self, pagination: Pagination) -> list[TourPriceSchema]:
        async with self.uow:
            return await self.uow.tour_prices.get_all(pagination)
    
    async def get_price_by_id(self, price_id: int) -> TourPriceSchema:
        async with self.uow:
            return await self.uow.tour_prices.get_by_id(price_id)

    async def get_list_of_prices_of_tour(self, tour_id: int) -> list[TourPriceSchema]:
        async with self.uow:
            return await self.uow.tour_prices.get_by_tour_id(tour_id)
        

    async def update_tour_prices(self, tour_id: int, price_data: UpdateTourPriceSchema) -> list[TourPriceSchema]:
        async with self.uow:
            prices = await self.uow.tour_prices.get_by_tour_id(tour_id)
            base_currency = await self.uow.currencies.get_by_name('USD')

            response = []
            for price in prices:
                if price.currency_id == base_currency.id:
                    converted_price = price_data.price
                else:
                    target_currency = await self.uow.currencies.get_by_id(price.currency_id)
                    exchange_rate = CurrencyHandler.get_exchange_rate(target_currency.name)
                    converted_price = price_data.price * exchange_rate

                price_dict = {
                    "price": converted_price,
                }
                updated_price = await self.uow.tour_prices.update(price.id, price_dict)
                response.append(TourPriceSchema(**updated_price.__dict__))

            
        return response
        

    