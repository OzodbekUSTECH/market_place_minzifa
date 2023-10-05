from repositories import BaseRepository
from utils.filters.filter_tours import FilterToursParams
from sqlalchemy import insert, select, update, delete
from fastapi_pagination.ext.async_sqlalchemy import paginate
from utils.locale_handler import LocaleHandler
from fuzzywuzzy import fuzz

class ToursRepository(BaseRepository):
    ...





class IPTourViewRepository(BaseRepository):
    ...
    
class IPAndToursViewRepository(BaseRepository):
    ...


        
    

    