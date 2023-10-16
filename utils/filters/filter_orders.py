from fastapi import Query
import models
from utils.filters.base import BaseFilterParams


class FilterOrderParams(BaseFilterParams):
    def __init__(
        self,
        user_id: int = Query(None),
        tour_id: int = Query(None),
    ):
        self.user_id = user_id
        self.tour_id = tour_id 
       

   

    def filter_item(self, order: models.Order): #locale: LocaleHandler
        # Список условий фильтрации
        filters = []

        if self.user_id:
            filters.append(self.user_id == order.user_id)

        if self.tour_id:
            filters.append(self.tour_id == order.tour_id)

        return all(filters)

    