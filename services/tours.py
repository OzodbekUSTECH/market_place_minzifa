from schemas.tours import CreateTourSchema, UpdateTourSchema, TourSchema
from repositories import Pagination
from utils.filter_tours import FilterTours
from fastapi import Request
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
        
    
    async def get_tour_by_id(self, tour_id: int, request: Request) -> TourSchema:

        async with self.uow:

            ip_tour_view = await self.uow.ip_tour_view.get_by_tour_id(tour_id)
            print(ip_tour_view)
            print("----------------------------------------------------------------")
            if not ip_tour_view:
                ip_tour_view_dict = {
                    "tour_id": tour_id,
                }
                ip_tour_view = await self.uow.ip_tour_view.create(ip_tour_view_dict)

            tour = await self.uow.tours.get_by_id(tour_id)
            ip_of_user = request.client.host
            # Извлекаем только дату из updated_at
            ip_address_date = ip_tour_view.updated_at.date() if ip_tour_view else None
            current_date = datetime.now().date()
            print(ip_tour_view)
            if ip_tour_view and ip_of_user not in ip_tour_view.ip_addresses:
                ip_tour_view.add_ip_address(ip_of_user)
                await self.uow.commit()
            if ip_of_user in ip_tour_view.ip_addresses and ip_address_date != current_date:
                ip_tour_view.add_ip_address(ip_of_user)
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
        

    async def search_tours(
            self, 
            filters: FilterTours,
            pagination: Pagination
        ):
        async with self.uow:
            users = await self.uow.users.get_all(pagination)
            matched_tours = []

            for user in users:
                for tour in user.tours:
                    if filters.filter_tour(tour):
                        matched_tours.append(tour)

            return matched_tours
    

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