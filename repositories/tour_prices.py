from repositories import BaseRepository
from datetime import datetime
from sqlalchemy import select


class TourPricesRepository(BaseRepository):
    async def get_expired_discounts(self):
        current_date = datetime.now().strftime("%d.%m.%Y")
        stmt = select(self.model).where(self.model.discount_end_date == current_date)
        result = await self.session.execute(stmt)
        return result.scalars().all()
    
    
    