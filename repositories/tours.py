from repositories import BaseRepository
from utils.filters.filter_tours import FilterToursParams
from sqlalchemy import insert, select, update, delete
from fastapi_pagination.ext.async_sqlalchemy import paginate
from utils.locale_handler import LocaleHandler
from fuzzywuzzy import fuzz


class ToursRepository(BaseRepository):
    ...

        


# filter_data = {'poster_id': poster_id, 'referenced_politician_id': referenced_politician_id, 'referenced_bill_id': referenced_bill_id}

# filter_data = {key: value for (key, value) in filter_data.items() if value}

# posts = SocialPost.query.filter_by(**filter_data).order_by(SocialPost.id.desc()).all()


class IPTourViewRepository(BaseRepository):
    ...
    
class IPAndToursViewRepository(BaseRepository):
    ...


        
    

    