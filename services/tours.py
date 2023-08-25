from schemas.tours import CreateTourPriceSchema, UpdateTourPriceSchema, CreateTourSchema, UpdateTourSchema, TourSchema, TourPriceSchema
from repositories import Pagination
from datetime import datetime
from models import Tour
from database.unitofwork import UnitOfWork
from utils.exceptions import CustomExceptions

class ToursService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def create_tour(self, tour_data: CreateTourSchema):
        tour_dict = {
            "name": tour_data.name
        }
        async with self.uow:
            created_tour = await self.uow.tours.create(tour_dict)
            
            base_currency = await self.uow.currencies.get_by_name('USD')
            target_currencies = await self.uow.currencies.get_all()
            res = []
            for target_currency in target_currencies:
                if target_currency == base_currency:
                    converted_price = tour_data.price
                else:
                    converted_price = tour_data.price * target_currency.exchange_rate

                create_price_data = CreateTourPriceSchema(
                    tour_id=created_tour.id,
                    currency_id=target_currency.id,
                    price=converted_price
                )
                created_price = await self.uow.tour_prices.create(create_price_data.model_dump())  # Создание цен для тура
                res_data = TourPriceSchema(
                    **created_price.__dict__
                )
                res.append(created_price)
            await self.uow.commit()
            response = TourSchema(
                **created_tour.__dict__,
                prices=res
            )
            return response

    async def _create_prices_for_tour(self, tour_id: int, price: float):
        base_currency = await self.uow.currencies.get_by_name('USD')
        target_currencies = await self.uow.currencies.get_all()
        res = []
        for target_currency in target_currencies:
            if target_currency == base_currency:
                converted_price = price
            else:
                converted_price = price * target_currency.exchange_rate

            create_price_data = CreateTourPriceSchema(
                tour_id=tour_id,
                currency_id=target_currency.id,
                price=converted_price
            )
            price_dict = create_price_data.model_dump()
            await self.uow.tour_prices.create(price_dict)
            res.append(price_dict)   
        return res

    async def get_list_of_tours(self, pagination: Pagination):
        async with self.uow:
            list_of_tours = await self.uow.tours.get_all(pagination)
            await self.uow.commit()
            return list_of_tours