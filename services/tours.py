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
    async def create_tour(self, tour_data: CreateTourSchema) -> TourSchema:
        tour_dict = tour_data.model_dump(exclude={"price"})
        price = tour_data.price
        async with self.uow:
            created_tour = await self.uow.tours.create(tour_dict)
            base_currency = await self.uow.currencies.get_by_name('USD')
            target_currencies = await self.uow.currencies.get_all()        
            for target_currency in target_currencies:
                converted_price = price if target_currency == base_currency else price * target_currency.exchange_rate
                
                create_price_data = CreateTourPriceSchema(
                    tour_id=created_tour.id,
                    currency_id=target_currency.id,
                    price=converted_price
                )
                await self.uow.tour_prices.create(create_price_data.model_dump())
        
            #had to use get_by_id for the response model in the router! Otherwise it doesn't work
            #i got a fastapi.exceptions.ResponseValidationError
            # tour = await self.uow.tours.get_by_id(created_tour.id)
            return created_tour

    async def _create_prices_for_tour(self, tour: Tour, price: float):
        base_currency = await self.uow.currencies.get_by_name('USD')
        target_currencies = await self.uow.currencies.get_all()        
        for target_currency in target_currencies:
            converted_price = price if target_currency == base_currency else price * target_currency.exchange_rate
            
            create_price_data = CreateTourPriceSchema(
                tour_id=tour.id,
                currency_id=target_currency.id,
                price=converted_price
            )
            await self.uow.tour_prices.create(create_price_data.model_dump())
        
            

    async def get_list_of_tours(self, pagination: Pagination) -> TourSchema:
        async with self.uow:
            list_of_tours = await self.uow.tours.get_all(pagination)
            return list_of_tours
        
    async def get_tour_by_id(self, tour_id: int) -> TourSchema:
        async with self.uow:
            return await self.uow.tours.get_by_id(tour_id)
        
    async def update_tour(self, tour_id: int, tour_data: UpdateTourSchema) -> TourSchema:
        ...