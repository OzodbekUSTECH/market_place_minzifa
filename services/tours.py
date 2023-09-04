from schemas.tours import CreateTourSchema, UpdateTourSchema, TourSchema
from repositories import Pagination, FilterTours
from datetime import datetime, date
from models import Tour
from database.unitofwork import UnitOfWork
from utils.exceptions import CustomExceptions
from utils.currency import CurrencyHandler
from fuzzywuzzy import fuzz, process

class ToursService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    # Ваш метод для создания тура с ценами
    async def create_tour(self, tour_data: CreateTourSchema) -> TourSchema:
        # tour_dict = tour_data.model_dump(exclude={"price"})
        tour_dict = tour_data.model_dump()

        async with self.uow:
            created_tour = await self.uow.tours.create(tour_dict)
            # await self._create_prices_for_tour(
            #     tour=created_tour,
            #     price=tour_data.price
            # )
            #had to use get_by_id for the response model in the router! Otherwise it doesn't work
            #i got a fastapi.exceptions.ResponseValidationError
            # tour = await self.uow.tours.get_by_id(created_tour.id)
            # return tour
            return created_tour

    # async def _create_prices_for_tour(self, tour: Tour, price: float):
    #     base_currency = await self.uow.currencies.get_by_name('USD')
    #     target_currencies = await self.uow.currencies.get_all()        
    #     for target_currency in target_currencies:
    #         converted_price = price if target_currency == base_currency else price * target_currency.exchange_rate
            
    #         create_price_data = CreateTourPriceSchema(
    #             tour_id=tour.id,
    #             currency_id=target_currency.id,
    #             price=converted_price
    #         )
    #         await self.uow.tour_prices.create(create_price_data.model_dump())
        
            

    async def get_list_of_tours(self, pagination: Pagination) -> TourSchema:
        async with self.uow:
            return await self.uow.tours.get_all(pagination)
        
    
    async def get_tour_by_id(self, tour_id: int) -> TourSchema:
        async with self.uow:
            tour = await self.uow.tours.get_by_id(tour_id)
            tour.increment_view_count()
            await self.uow.commit()
            return tour
        
    async def update_tour(self, tour_id: int, tour_data: UpdateTourSchema) -> TourSchema:
        tour_dict = tour_data.model_dump()
        async with self.uow:
            updated_tour = await self.uow.tours.update(tour_id, tour_dict)
            return updated_tour
        
    async def delete_tour(self, tour_id: int) -> TourSchema:
        async with self.uow:
            return await self.uow.tours.delete(tour_id)
        


    async def search_tours(self, query: str, status_id: int, tour_rating: float, pagination: Pagination):
        async with self.uow:
            filtered_tours =  await self.uow.tours.search_tours(query, status_id,tour_rating,pagination)
            return filtered_tours

    async def search_tours_second(
            self, 
            filters: FilterTours,
            pagination: Pagination
        ):
        async with self.uow:
            users = await self.uow.users.get_all(pagination)
            matched_tours = []
            for user in users:
                for tour in user.tours:
                    if not filters.status_id or tour.status_id == filters.status_id:
                            
                        if not filters.query or fuzz.partial_ratio(filters.query.lower(), tour.title.lower()) > 60:
                            if not filters.tour_rating or (user.rating >= filters.tour_rating and user.rating < (filters.tour_rating + 0.5)):
                                if not filters.start_date or filters.start_date == tour.start_date:
                                    if not filters.end_date or filters.end_date == tour.end_date:
                                        if not filters.country or filters.country == tour.country:
                                            if not filters.region or filters.region == tour.region:
                                                if filters.currency_id is None or filters.price is None:
                                                    matched_tours.append(tour)
                                                else:
                                                    # Получаем цену тура в указанной валюте
                                                    for tour_price in tour.prices:
                                                        if tour_price.currency_id == filters.currency_id and tour_price.price >= filters.price:
                                                            matched_tours.append(tour)

            return matched_tours
    async def filter_tours(self, query: str, status_id: int, tour_rating: float,
                        start_date: date, end_date: date, country: str, region: str,
                        currency_id: int, price: int, pagination):
        async with self.uow:
            users = await self.uow.users.get_all(pagination)
            matched_tours = []

            for user in users:
                for tour in user.tours:
                    if self._filter_tour(tour, query, status_id, tour_rating,
                                            start_date, end_date, country, region, currency_id, price):
                        matched_tours.append(tour)

            return matched_tours

    def _filter_tour(self, tour, query, status_id, tour_rating,
                     start_date, end_date, country, region, currency_id, price):
        if status_id and tour.status_id != status_id:
            return False

        if query and fuzz.partial_ratio(query.lower(), tour.title.lower()) <= 60:
            return False

        if tour_rating and (tour.user.rating < tour_rating or tour.user.rating >= tour_rating + 0.5):
            return False

        if start_date and tour.start_date != start_date:
            return False

        if end_date and tour.end_date != end_date:
            return False

        if country and tour.country != country:
            return False

        if region and tour.region != region:
            return False

        if currency_id is not None and price is not None:
            for tour_price in tour.prices:
                if tour_price.currency_id == currency_id and tour_price.price >= price:
                    return True
            return False

        return True

        # async def create_full_tour(self, tour_data: CreateTourSchema) -> TourSchema: 
    #     tour_dict = tour_data.model_dump(exclude=["price", "currency_id", "activities_ids"])
    #     async with self.uow:
    #         created_tour = await self.uow.tours.create(tour_dict)
    #         base_currency = await self.uow.currencies.get_by_id(tour_data.currency_id)
    #         target_currencies = await self.uow.currencies.get_all()
    #         for target_currency in target_currencies:
    #             if target_currency == base_currency:
    #                 converted_price = tour_data.price
    #             else:
    #                 exchange_rate = await CurrencyHandler.get_exchange_rate(base_currency.name, target_currency.name)
    #                 if exchange_rate:
    #                     converted_price = tour_data.price * exchange_rate
    #                 else:
    #                     converted_price = tour_data.price * target_currency.exchange_rate
                    
    #             price_dict = {
    #                 "tour_id": created_tour.id,
    #                 "currency_id": target_currency.id,
    #                 "price": converted_price
    #             }
    #             await self.uow.tour_prices.create(price_dict)
    #         for activity_id in tour_data.activities_ids:
    #             activity_dict = {
    #                 "tour_id": created_tour.id,
    #                 "activity_id": activity_id,
    #             }
    #             await self.uow.tour_activities.create(activity_dict)
            
    #         return await self.uow.tours.get_by_id(created_tour.id)