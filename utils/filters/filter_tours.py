from fastapi import Query
from fuzzywuzzy import fuzz
import models
from utils.locale_handler import LocaleHandler
from utils.filters.base import BaseFilterParams
from typing import Union
def return_none():
    return None

class FilterToursParams(BaseFilterParams):
    def __init__(
        self,
        country_id:  str| None  = Query(None),
        region_id: str | None= Query(None),
        start_month: str | None= Query(None),
        query: str | None= Query(None),
        user_id: str | None= Query(None),
        rating: str | None = Query(None),
        status_id: str | None= Query(None),
        duration_from: str | None = Query(None),
        duration_to: str | None = Query(None),
        category_id: str | None = Query(None),
        type_id: str | None = Query(None),
        accommodation_id: str | None = Query(None),
        age_group_from: str | None = Query(None),
        age_group_to: str | None = Query(None),
        is_one_day_tour: bool = Query(False),
        children_age_id: str | None = Query(None),
        activity_level_id: str | None = Query(None),
        language_id: str | None = Query(None),

        is_price_for_day: bool = Query(False),
        currency_id: str | None = Query(None),

        price_from: str | None = Query(None),
        price_to: str | None = Query(None),

        only_with_discounts: bool = Query(False),
    ):
        self.country_id = country_id
        self.region_id = region_id
        self.start_month = start_month 
        self.query = query
        self.user_id = user_id
        self.rating = rating
        self.status_id = status_id
        self.duration_from = duration_from
        self.duration_to = duration_to
        self.category_id = category_id
        self.type_id = type_id
        self.accommodation_id = accommodation_id
        self.age_group_from = age_group_from
        self.age_group_to = age_group_to
        self.is_one_day_tour = is_one_day_tour
        self.children_age_id = children_age_id
        self.activity_level_id = activity_level_id
        self.language_id = language_id

        self.is_price_for_day = is_price_for_day
        self.currency_id = currency_id
        self.price_from = price_from
        self.price_to = price_to

        self.only_with_discounts = only_with_discounts


    def filter_item(self, tour: models.Tour, locale: LocaleHandler):
        # Список условий фильтрации
        filters = []

        #проверка параметра country_id
        if self.country_id is not None:
            filters.append(int(self.country_id) in tour.country_ids)

        if self.region_id is not None:
            filters.append(int(self.region_id) in tour.region_ids)

        #проверка параметра start_month
        if self.start_month is not None:
            filters.append(int(self.start_month) == tour.start_month)

        # Проверка параметра query
        if self.query:
            filters.append(
                fuzz.partial_ratio(
                    self.query.lower(), tour.title[locale.get_language].lower()
                ) >= 60
            )

        if self.user_id is not None:
            filters.append(int(tour.user_id) == self.user_id)

        if self.rating is not None:
            filters.append(float(self.rating) == tour.user.rating)

        # Проверка параметра status_id
        if self.status_id is not None:
            filters.append(int(self.status_id) == tour.status_id)

        # Проверка параметра duration_from
        if self.duration_from is not None:
            filters.append(tour.duration >= int(self.duration_from))

        # Проверка параметра duration_to
        if self.duration_to is not None:
            filters.append(tour.duration <= int(self.duration_to))

        #Проверка параметра category_id
        # if self.category_id is not None:
        #     filters.append(self.category_id in tour.category_ids)
        if self.category_id is not None:
            filters.append(int(self.category_id) == tour.category_id)

        if self.type_id is not None:
            filters.append(int(self.type_id) == tour.main_type_id)

        if self.accommodation_id is not None:
            filters.append(int(self.accommodation_id) in tour.accommodation_ids)

        if self.age_group_from is not None:
            filters.append(tour.age_group_from >= int(self.age_group_from))

        # Проверка параметра age_group_to
        if self.age_group_to is not None:
            filters.append(tour.age_group_to <= int(self.age_group_to))
        # Проверка параметра is_one_day_tour
        if self.is_one_day_tour is not None:
            filters.append(tour.is_one_day_tour == self.is_one_day_tour)

        # Проверка параметра children_age_id
        if self.children_age_id is not None:
            filters.append(tour.children_age_id == int(self.children_age_id))

        # Проверка параметра activity_level_id
        if self.activity_level_id is not None:
            filters.append(tour.activity_level_id == int(self.activity_level_id))

        if self.language_id is not None:
            filters.append(int(self.language_id) in tour.language_ids)

        if self.currency_id is not None:
            price_filters = []
            
            for tour_price in tour.prices:
                if self.is_price_for_day is not None:
                    price_filters.append(
                        int(self.currency_id) == tour_price.currency_id and
                        float(self.price_from) <= tour_price.price_for_day <= float(self.price_to)
                    )
                else:
                    price_filters.append(
                        int(self.currency_id) == tour_price.currency_id and
                        float(self.price_from) <= tour_price.price <= float(self.price_to)
                    )
            
            # Use any() to check if at least one price filter condition is satisfied
            filters.append(any(price_filters))

        if self.only_with_discounts:
            filters.append(self.only_with_discounts == tour.has_discount)
        # Применение всех условий с использованием логического оператора "и" (AND)
        return all(filters)
