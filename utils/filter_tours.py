from fastapi import Query
from datetime import date
from fuzzywuzzy import fuzz, process
class FilterTours:
    def __init__(
            self,
            query: str = Query(None),
            status_id: int = Query(None),
            tour_rating: float = Query(None, le=5.0, ge=0.0),
            start_date: date = Query(None),
            end_date: date = Query(None),
            country: str = Query(None),
            region: str = Query(None),
            currency_id: int = Query(None),
            price: int = Query(None),
            age_group: str = Query(None),
            children_age: str = Query(None),
            level_of_activity: str = Query(None),
            language_id: int = Query(None), 
    ):
        self.query = query
        self.status_id = status_id
        self.tour_rating = tour_rating
        self.start_date = start_date
        self.end_date = end_date
        self.country = country
        self.region = region
        self.currency_id = currency_id
        self.price = price
        self.age_group = age_group
        self.children_age = children_age
        self.level_of_activity = level_of_activity
        self.language_id = language_id

    def filter_tour(self, tour, locale: str):
        if self.status_id and tour.status_id != self.status_id:
            return False

        if self.query and fuzz.partial_ratio(self.query.lower(), tour.title[locale].lower()) <= 60:
            return False
        
        if self.tour_rating and (tour.user.rating < self.tour_rating or tour.user.rating >= self.tour_rating + 0.5):
            return False

        if self.start_date and tour.start_date != self.start_date:
            return False

        if self.end_date and tour.end_date != self.end_date:
            return False

        if self.country and tour.country[locale] != self.country:
            return False

        if self.region and tour.region[locale] != self.region:
            return False
        
        if self.age_group and tour.age_group != self.age_group:
            return False
        
        if self.children_age and tour.children_age != self.children_age:
            return False
        
        if self.level_of_activity and tour.level_of_activity[locale] != self.level_of_activity:
            return False

        if self.language_id:
            lang_ids = tour.get_list_of_language_ids()
            if self.language_id not in lang_ids:
                return False
        if self.currency_id is not None and self.price is not None:
            for tour_price in tour.prices:
                if tour_price.currency_id == self.currency_id and tour_price.price >= self.price:
                    return True
            return False

        return True