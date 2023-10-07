from repositories import BaseRepository
from sqlalchemy import select, and_, cast, Date
from datetime import datetime, timedelta

class StatisticsOfViewsRepository(BaseRepository):
    async def get_by_period(self, start_date: str | None, end_date: str | None):
        if not start_date:
            # Если start_date не передан, то устанавливаем его на 7 дней назад от текущей даты
            start_date = datetime.now() - timedelta(days=7)
        else:
            # Преобразуем переданные строки с датами в объекты datetime
            start_date = datetime.strptime(start_date, "%d.%m.%Y")

        if not end_date:
            # Если end_date не передан, то устанавливаем его на текущую дату
            end_date = datetime.now()
        else:
            # Преобразуем переданные строки с датами в объекты datetime
            end_date = datetime.strptime(end_date, "%d.%m.%Y")

        stmt = select(self.model).where(
            and_(
                cast(self.model.date, Date) >= start_date.date(),
                cast(self.model.date, Date) <= end_date.date()
            )
        ).order_by(self.model.id)
        result = await self.session.execute(stmt)
        return result.scalars().all()
