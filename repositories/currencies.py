from repositories import BaseRepository
from sqlalchemy import insert, select, update, delete
from sqlalchemy import func



class CurrenciesRepository(BaseRepository):    
    async def get_all_without_pagination(self):
        stmt =  select(self.model)
        result = await self.session.execute(stmt)
        return result.scalars().all()
    
    