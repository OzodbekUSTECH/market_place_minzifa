from fastapi import Query
from datetime import date

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