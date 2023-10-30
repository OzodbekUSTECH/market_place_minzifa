from repositories import BaseRepository
from utils.filters.filter_tours import FilterToursParams
from sqlalchemy import insert, select, update, delete, literal_column
from fastapi_pagination.ext.async_sqlalchemy import paginate
from utils.locale_handler import LocaleHandler
from fuzzywuzzy import fuzz


from sqlalchemy.sql import select, and_
from sqlalchemy.sql.expression import cast
from sqlalchemy.types import ARRAY, Integer

class ToursRepository(BaseRepository):
    async def get_filtered_tours(self, filter_params: FilterToursParams, locale: LocaleHandler):
        stmt = select(self.model)

        if filter_params.start_month:
            stmt = stmt.filter(self.model.free_places.contains(3))

        return await paginate(self.session, stmt)

        


# filter_data = {'poster_id': poster_id, 'referenced_politician_id': referenced_politician_id, 'referenced_bill_id': referenced_bill_id}

# filter_data = {key: value for (key, value) in filter_data.items() if value}

# posts = SocialPost.query.filter_by(**filter_data).order_by(SocialPost.id.desc()).all()


class IPTourViewRepository(BaseRepository):
    ...
    
class IPAndToursViewRepository(BaseRepository):
    ...


        
    

    