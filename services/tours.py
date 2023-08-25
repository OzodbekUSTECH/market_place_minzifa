from schemas.tours import CreateTourPriceSchema, UpdateTourPriceSchema, CreateTourSchema, UpdateTourSchema, TourSchema, TourPriceSchema
from repositories import Pagination
from datetime import datetime
from database.unitofwork import UnitOfWork
from utils.exceptions import CustomExceptions

class ToursService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def create_tour(self, tour_data: CreateTourSchema):
        tour_dict = tour_data.model_dump()
        async with self.uow:
            created_tour = await self.uow.tours.create(tour_dict)
            # await self._create_prices_for_tour(created_tour, tour_data.prices)
            await self.uow.commit()
            return created_tour

    async def _create_prices_for_tour(self, tour, prices_data):
        base_currency = await self.uow.currencies.get_by_name('USD')

        for price_data in prices_data:
            base_price = price_data.price

            for target_currency in self.uow.currencies.get_all():
                converted_price = base_price * (target_currency.exchange_rate / base_currency.exchange_rate)

                price_to_create = CreateTourPriceSchema(
                    tour_id=tour.id,
                    currency_id=target_currency.id,
                    price=converted_price
                )
                await self.uow.tour_prices.create(price_to_create)
        
    async def get_list_of_tours(self, pagination: Pagination):
        async with self.uow:
            list_of_tours = await self.uow.tours.create(pagination)
            await self.uow.commit()
            return list_of_tours