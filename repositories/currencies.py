from repositories import BaseRepository
from sqlalchemy import func



class CurrenciesRepository(BaseRepository):    
    async def get_by_name(self, name: str):
        currencies = self.session.query(self.model).filter(func.lower(self.model.name) == name.lower()).first()
        self.session.commit()
        return currencies
    
    