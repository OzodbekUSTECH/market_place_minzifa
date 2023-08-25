from schemas.tours import CreateTourPriceSchema, UpdateTourPriceSchema, CreateTourSchema, UpdateTourSchema, TourSchema, TourPriceSchema
from repositories import Pagination
from datetime import datetime
from models import Tour
from database.unitofwork import UnitOfWork
from utils.exceptions import CustomExceptions

class ToursService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    # Ваш метод для создания тура с ценами
    async def create_tour(self, tour_data: CreateTourSchema):
        async with self.uow:
            created_tour = await self.uow.tours.create({"name": tour_data.name})
            prices = await self._create_prices_for_tour(
                tour_id=created_tour.id,
                price=tour_data.price
            )
            if prices:
                tour = self.uow.tours.get_by_id(created_tour.id)
                return tour

    async def _create_prices_for_tour(self, tour_id: int, price: float):
        base_currency = await self.uow.currencies.get_by_name('USD')
        target_currencies = await self.uow.currencies.get_all()
        
        # prices_to_create = []
        
        for target_currency in target_currencies:
            converted_price = price if target_currency == base_currency else price * target_currency.exchange_rate
            
            create_price_data = CreateTourPriceSchema(
                tour_id=tour_id,
                currency_id=target_currency.id,
                price=converted_price
            )
            await self.uow.tour_prices.create(create_price_data.model_dump())
            # prices_to_create.append(TourPriceSchema(**created_price.__dict__))
        
        return True
            

    async def get_list_of_tours(self, pagination: Pagination):
        async with self.uow:
            list_of_tours = await self.uow.tours.get_all(pagination)
            # await self.uow.commit()
            return list_of_tours