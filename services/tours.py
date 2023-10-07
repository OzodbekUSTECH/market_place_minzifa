from schemas.tours import CreateTourSchema, UpdateTourSchema
# from schemas.tour_categories import CreateTourCategorySchema
# from schemas.tour_additional_types import CreateTourAdditionalTypeSchema
from schemas.tour_languages import CreateTourLanguageSchema
from schemas.tour_activities import CreateTourActivitySchema
from schemas.tour_accommodations import CreateTourAccommodationSchema
from schemas.tour_countries import CreateTourCountrySchema
from schemas.tour_regions import CreateTourRegionSchema
from schemas.tour_prices import CreateTourPriceSchema
from repositories import paginate
import models
from database import UnitOfWork
from utils.exceptions import CustomExceptions
from utils.filters.filter_tours import FilterToursParams
from utils.locale_handler import LocaleHandler
from typing import Set, Callable
from utils.tour_prices import TourPriceHandler

class ToursService:
    def __init__(self):
        self.uow = UnitOfWork()

    async def _bulk_create(
            self,
            data_list: list[dict],
            bulk_create_func: Callable
    ):
        await bulk_create_func(data_list)

    async def create_tour(self, tour_data: CreateTourSchema) -> models.Tour:
        tour_dict = tour_data.model_dump()
        async with self.uow:
            tour: models.Tour = await self.uow.tours.create(tour_dict)
            
            
            data_list = await self._create_update_prices(tour, tour_data)
            await self.uow.tour_prices.bulk_create(data_list)

            # Создайте список словарей для категорий
            # await self._bulk_create(
            #     data_list=[CreateTourCategorySchema(tour_id=tour.id, category_id=category_id).model_dump() for category_id in tour_data.category_ids],
            #     bulk_create_func=self.uow.tour_categories.bulk_create
            # )
            # await self._bulk_create(
            #     data_list=[CreateTourAdditionalTypeSchema(tour_id=tour.id, type_id=additional_type_id).model_dump() for additional_type_id in tour_data.additional_type_ids],
            #     bulk_create_func=self.uow.tour_additional_types.bulk_create
            # )

            await self._bulk_create(
                data_list=[CreateTourLanguageSchema(tour_id=tour.id, language_id=language_id).model_dump() for language_id in tour_data.language_ids],
                bulk_create_func=self.uow.tour_languages.bulk_create
            )

            await self._bulk_create(
                data_list=[CreateTourActivitySchema(tour_id=tour.id, activity_id=activity_id).model_dump() for activity_id in tour_data.activity_ids],
                bulk_create_func=self.uow.tour_activities.bulk_create
            )
            await self._bulk_create(
                data_list = [CreateTourAccommodationSchema(tour_id=tour.id, accommodation_id=accommodation_id).model_dump() for accommodation_id in tour_data.accommodation_ids],
                bulk_create_func=self.uow.tour_accommodations.bulk_create
            )

            await self._bulk_create(
                data_list=[CreateTourCountrySchema(tour_id=tour.id, country_id=country_id).model_dump() for country_id in tour_data.country_ids],
                bulk_create_func=self.uow.tour_countries.bulk_create
            )

            await self._bulk_create(
                data_list=[CreateTourRegionSchema(tour_id=tour.id, region_id=region_id).model_dump() for region_id in tour_data.region_ids],
                bulk_create_func=self.uow.tour_regions.bulk_create
            )
            
        
            await self.uow.commit()
            return tour

    async def _delete_expired_discounts(self) -> bool:
        
        expired_discounts: list[models.TourPrice] = await self.uow.tour_prices.get_expired_discounts()
        if expired_discounts:
            null_sign = None
            for expired_discount in expired_discounts:
                null_discount_dict = {
                    "discount_percentage": null_sign,
                    "new_price": null_sign,
                    "discount_start_date": null_sign,
                    "discount_end_date": null_sign
                }
                
                await self.uow.tour_prices.update(expired_discount.id, null_discount_dict)
            
            await self.uow.commit()
        
        


    async def get_list_of_tours(
        self,
        filter_params: FilterToursParams,
        locale: LocaleHandler,
    ) -> list[models.Tour]:
        async with self.uow:
            await self._delete_expired_discounts()
            tours = await self.uow.tours.get_all()
            filtered_tours = await filter_params.get_filtered_items(tours.items, locale)
            return paginate(filtered_tours)

    async def get_tour_by_id(self, id: int) -> models.Tour:
        async with self.uow:
            return await self.uow.tours.get_by_id(id)

    async def _update_items(
        self, 
        current_items: set[int], 
        new_items: set[int], 
        add_item_func: callable, 
        remove_item_func: callable, 
    ):
        items_to_add = new_items - current_items
        items_to_remove = current_items - new_items
        
        for item_id in items_to_add:
            await add_item_func(item_id)
        
        for item_id in items_to_remove:
            await remove_item_func(item_id)

    async def update_tour(self, id: int, tour_data: UpdateTourSchema) -> models.Tour:
        async with self.uow:
            existing_tour: models.Tour = await self.uow.tours.get_by_id(id)

            if not existing_tour:
                raise CustomExceptions.not_found()
            
            await self._create_update_prices(existing_tour, tour_data, update_mode=True)

            # await self._update_items(
            #     set(existing_tour.category_ids), 
            #     set(tour_data.category_ids),
            #     lambda category_id: self.uow.tour_categories.create(
            #         CreateTourCategorySchema(
            #             tour_id=existing_tour.id,
            #             category_id=category_id
            #         ).model_dump()
            #     ),
            #     lambda category_id: self.uow.tour_categories.delete_by(
            #         tour_id=existing_tour.id,
            #         category_id=category_id
            #     )
            # )

            # await self._update_items(
            #     set(existing_tour.additional_type_ids), 
            #     set(tour_data.additional_type_ids),
            #     lambda additional_type_id: self.uow.tour_additional_types.create(
            #         CreateTourAdditionalTypeSchema(
            #             tour_id=existing_tour.id,
            #             type_id=additional_type_id
            #         ).model_dump()
            #     ),
            #     lambda additional_type_id: self.uow.tour_additional_types.delete_by(
            #         tour_id=existing_tour.id,
            #         type_id=additional_type_id
            #     )
            # )

            await self._update_items(
                set(existing_tour.language_ids),
                set(tour_data.language_ids),
                lambda language_id: self.uow.tour_languages.create(
                    CreateTourLanguageSchema(
                        tour_id=existing_tour.id,
                        language_id=language_id,
                    ).model_dump()
                ),
                lambda language_id: self.uow.tour_languages.delete_by(
                    tour_id = existing_tour.id,
                    language_id = language_id
                )
            )

            await self._update_items(
                set(existing_tour.activity_ids),
                set(tour_data.activity_ids),
                lambda activity_id: self.uow.tour_activities.create(
                    CreateTourActivitySchema(
                        tour_id=existing_tour.id,
                        activity_id=activity_id
                    ).model_dump()
                ),
                lambda activity_id: self.uow.tour_activities.delete_by(
                    tour_id = existing_tour.id,
                    activity_id = activity_id
                )
            )

            await self._update_items(
                set(existing_tour.accommodation_ids),
                set(tour_data.accommodation_ids),
                lambda accommodation_id: self.uow.tour_accommodations.create(
                    CreateTourAccommodationSchema(
                        tour_id=existing_tour.id,
                        accommodation_id=accommodation_id
                    ).model_dump()
                ),
                lambda accommodation_id: self.uow.tour_accommodations.delete_by(
                    tour_id=existing_tour.id,
                    accommodation_id=accommodation_id
                )
            )

            await self._update_items(
                set(existing_tour.country_ids),
                set(tour_data.country_ids),
                lambda country_id: self.uow.tour_countries.create(
                    CreateTourCountrySchema(
                        tour_id=existing_tour.id,
                        country_id=country_id
                    ).model_dump()
                ),
                lambda country_id: self.uow.tour_countries.delete_by(
                    tour_id=existing_tour.id,
                    country_id=country_id
                )
            )

            await self._update_items(
                set(existing_tour.region_ids),
                set(tour_data.region_ids),
                lambda region_id: self.uow.tour_regions.create(
                    CreateTourRegionSchema(
                        tour_id=existing_tour.id,
                        region_id=region_id
                    ).model_dump()
                ),
                lambda region_id: self.uow.tour_regions.delete_by(
                    tour_id=existing_tour.id,
                    region_id=region_id
                )
            )
            

            tour_dict = tour_data.model_dump()
            updated_tour = await self.uow.tours.update(id, tour_dict)

            await self.uow.commit()

            return updated_tour
        
    async def _create_update_prices(
            self,
            tour: models.Tour,
            tour_data: CreateTourSchema,
            update_mode: bool = False
    ):
        price_data = CreateTourPriceSchema(
            tour_id=tour.id,
            currency_id=tour_data.currency_id,
            price=tour_data.price,
            discount_percentage=tour_data.discount_percentage,
            new_price=tour_data.new_price,
            discount_start_date=tour_data.discount_start_date,
            discount_end_date=tour_data.discount_end_date
        )

        data_list = []

        target_currencies: list[models.Currency] = await self.uow.currencies.get_all_without_pagination()
        base_currency = await self.uow.currencies.get_by_id(tour_data.currency_id)
        for target_currency in target_currencies:
            price_dict = await TourPriceHandler.create_price_dict(
                target_currency, base_currency, price_data
            )
            if update_mode:
                await self.uow.tour_prices.update(target_currency.price_instance.id, price_dict)
            else:
                data_list.append(price_dict)

        if data_list:
            return data_list
        

    async def delete_tour(self, id: int) -> models.Tour:
        async with self.uow:
            tour = await self.uow.tours.delete(id)
            await self.uow.commit()
            return tour
                   

tours_service = ToursService()
