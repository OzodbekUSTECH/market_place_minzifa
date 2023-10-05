from fastapi import Query
from fuzzywuzzy import fuzz
import models
from utils.filters.base import BaseFilterParams


class FilterCommentsParams(BaseFilterParams):
    def __init__(
        self,
        user_id: int = Query(None),
        tour_id: int = Query(None),
    ):
        self.user_id = user_id
        self.tour_id = tour_id 
       

   

    def filter_item(self, comment: models.TourComment, ): #locale: LocaleHandler
        # Список условий фильтрации
        filters = []

        #проверка параметра country_id
        filters.append(comment.parent_comment_id is None)
        if self.user_id is not None:
            filters.append(self.user_id == comment.user_id)

        #проверка параметра start_month
        if self.tour_id is not None:
            filters.append(self.tour_id == comment.tour_id)

        # Проверка параметра query
      
        # Применение всех условий с использованием логического оператора "и" (AND)
        return all(filters)
