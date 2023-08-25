from schemas.tourprices import CreateTourPriceSchema, UpdateTourPriceSchema, TourPriceSchema
from repositories import Pagination
from datetime import datetime
from models import Tour
from database.unitofwork import UnitOfWork
from utils.exceptions import CustomExceptions

class TourPricesService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def _create_prices_for_tour(self, price_data: CreateTourPriceSchema):
        base_currency = await self.uow.currencies.get_by_name('USD')
        target_currencies = await self.uow.currencies.get_all()
        response = []        
        for target_currency in target_currencies:
            converted_price = price_data.price if target_currency == base_currency else price_data.price * target_currency.exchange_rate
            
            create_price_data = CreateTourPriceSchema(
                tour_id=price_data.tour_id,
                currency_id=target_currency.id,
                price=converted_price
            )
            created_price = await self.uow.tour_prices.create(create_price_data.model_dump())
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
        

    