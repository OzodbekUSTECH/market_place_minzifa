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
        base_currency = await self.uow.currencies.get_by_id(price_data.currency_id)
        target_currencies = await self.uow.currencies.get_all()
        response = []        
        for target_currency in target_currencies:
            if target_currency == base_currency:
                converted_price = price_data.price
            else:
                exchange_rate = await CurrencyHandler.get_exchange_rate(base_currency.name, target_currency.name)
                if exchange_rate:
                    converted_price = price_data.price * exchange_rate
                else:
                    converted_price = price_data.price * target_currency.exchange_rate
            
            
            price_dict = {
                "tour_id": price_data.tour_id,
                "currency_id": target_currency.id,
                "price": converted_price
            }
            if price_data.new_price > 0 and price_data.discount_percentage > 0:
                raise CustomExceptions.conflict("You can only fill either the new price or the discount")
            if price_data.discount_percentage:
                new_price = await self._calculate_new_price(converted_price, price_data.discount_percentage)
                price_dict = {
                    "tour_id": price_data.tour_id,
                    "currency_id": target_currency.id,
                    "price": converted_price,
                    "discount_percentage": price_data.discount_percentage,
                    "new_price": new_price
                }
            if price_data.new_price:
                discount_percentage = await self._calculate_discount(converted_price, price_data.new_price)
                price_dict = {
                    "tour_id": price_data.tour_id,
                    "currency_id": target_currency.id,
                    "price": converted_price,
                    "discount_percentage": discount_percentage,
                    "new_price": price_data.new_price
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
            base_currency = await self.uow.currencies.get_by_id(price_data.currency_id)

            response = []
            for price in prices:
                if price.currency_id == base_currency.id:
                    converted_price = price_data.price
                else:
                    target_currency = await self.uow.currencies.get_by_id(price.currency_id)
                    exchange_rate = await CurrencyHandler.get_exchange_rate(base_currency.name, target_currency.name)
                    if exchange_rate:
                        converted_price = price_data.price * exchange_rate
                    else:
                        converted_price = price_data.price * target_currency.exchange_rate

                price_dict = {
                    "price": converted_price,
                }
                if price_data.new_price > 0 and price_data.discount_percentage > 0:
                    raise CustomExceptions.conflict("You can only fill either the new price or the discount")
                if price_data.discount_percentage:
                    new_price = await self._calculate_new_price(converted_price, price_data.discount_percentage)
                    price_dict = {
                        "price": converted_price,
                        "discount_percentage": price_data.discount_percentage,
                        "new_price": new_price
                    }
                if price_data.new_price:
                    discount_percentage = await self._calculate_discount(converted_price, price_data.new_price)
                    price_dict = {
                        "price": converted_price,
                        "discount_percentage": discount_percentage,
                        "new_price": price_data.new_price
                    }
                updated_price = await self.uow.tour_prices.update(price.id, price_dict)
                response.append(TourPriceSchema(**updated_price.__dict__))

            
        return response
    
    async def _calculate_discount(self, previous_price: int, new_price: int):
            discount_percentage = ((previous_price - new_price) / previous_price) * 100
            return discount_percentage

    async def _calculate_new_price(self, previous_price: int, discount_percentage: int):
            new_price = previous_price - (previous_price * discount_percentage / 100)
            return new_price


        

    