from schemas.tours import CreateTourSchema, UpdateTourSchema, TourSchema
from repositories import Pagination
from utils.filter_tours import FilterTours
from fastapi import Request
from datetime import datetime, date
from models import Tour, IPTourView
from database.unitofwork import UnitOfWork
from utils.exceptions import CustomExceptions
from utils.currency import CurrencyHandler
from fuzzywuzzy import fuzz, process
from utils.locale_handler import LocaleHandler

class ToursService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    # Ваш метод для создания тура с ценами
    async def create_tour(self, tour_data: CreateTourSchema) -> Tour:
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
        
            

    async def get_list_of_tours(self, locale: LocaleHandler, pagination: Pagination = None) -> Tour:
        async with self.uow:
            tours = await self.uow.tours.get_all(pagination)
            return await self.uow.serialize_one_or_all_models_by_locale(tours, locale)
    
    async def get_list_of_tours_of_user(self, user_id: int, locale: LocaleHandler, pagination: Pagination = None) -> list[Tour]:
        async with self.uow:
            user = await self.uow.users.get_by_id(user_id)
            user_tours = user.tours[pagination.offset:pagination.offset + pagination.limit]
            return await self.uow.serialize_one_or_all_models_by_locale(user_tours, locale)
    ###################################################################################
    ###################################################################################
    ###################################################################################
    async def get_tour_by_id(self, tour_id: int, request: Request, locale: LocaleHandler) -> Tour:
        async with self.uow:
            ip_of_user = request.client.host
            ip_address = await self._get_or_create_ip_address(ip_of_user)
            
            list_of_tour_ids = ip_address.get_list_of_tour_ids()
            
            if tour_id not in list_of_tour_ids:
                await self._add_tour_view(ip_address, tour_id)
            
            await self._update_tour_view(ip_address, tour_id)
            
            tour = await self.uow.tours.get_by_id(tour_id)
            return await self.uow.serialize_one_or_all_models_by_locale(tour, locale)
    ######################################################################################
    async def _get_or_create_ip_address(self, ip_address: str) -> IPTourView:
        existing_ip_address = await self.uow.ip_tour_view.get_by_ip_address(ip_address)
        if not existing_ip_address:
            ip_address_dict = {
                "ip_address": ip_address,
            }
            existing_ip_address = await self.uow.ip_tour_view.create(ip_address_dict)
        return existing_ip_address

    async def _add_tour_view(self, ip_address, tour_id: int):
        ip_and_tour_dict = {
            "ip_id": ip_address.id,
            "tour_id": tour_id
        }
        created_ip_and_tour = await self.uow.ip_and_tours_view.create(ip_and_tour_dict)
        created_ip_and_tour.increase_visited_times()
        await self.uow.commit()

    async def _update_tour_view(self, ip_address, tour_id: int):
        ip_and_tour_view = await self.uow.ip_and_tours_view.get_by_ip_id_and_tour_id(ip_address.id, tour_id)
        ip_and_tour_viewed_date = ip_and_tour_view.updated_at.date() if ip_and_tour_view else None
        current_date = datetime.now().date()
        if ip_address and tour_id in ip_address.get_list_of_tour_ids() and ip_and_tour_viewed_date != current_date:
            ip_and_tour_view.increase_visited_times()
            await self.uow.commit()
    ###################################################################################
    ###################################################################################
    ###################################################################################
    
    async def update_tour(self, tour_id: int, tour_data: UpdateTourSchema) -> Tour:
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
            pagination: Pagination,
            locale: LocaleHandler,
        ) -> list[Tour]:
        async with self.uow:
            users = await self.uow.users.get_all(pagination)
            matched_tours = []

            for user in users:
                for tour in user.tours:
                    if filters.filter_tour(tour, locale.get_language):
                        matched_tours.append(tour)

            return await self.uow.serialize_one_or_all_models_by_locale(matched_tours, locale)
    

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