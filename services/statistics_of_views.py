from schemas.statistics_of_views import CreateStatisticView
from database import UnitOfWork
from utils.exceptions import CustomExceptions
import models
import datetime
class StatisticsOfViewsService:
    def __init__(self):
        self.uow = UnitOfWork()

    async def increase_statistics_views(self):
        current_date = datetime.datetime.now().strftime("%d.%m.%Y")
        async with self.uow:
            current_date_statistics = await self.uow.statistics_of_views.get_one_by(date=current_date)
            if not current_date_statistics:
                current_date_statistics: models.StatisticOfViews = await self.uow.statistics_of_views.create(CreateStatisticView(date=current_date).model_dump())

            await current_date_statistics.increase_view_counter()
            await self.uow.commit()

    async def get_percentage_statistics(self):
        today = datetime.date.today()
        one_day_ago = today - datetime.timedelta(days=1)
        seven_days_ago = today - datetime.timedelta(days=7)
        thirty_days_ago = today - datetime.timedelta(days=30)
        
        today_str = today.strftime("%d.%m.%Y")
        one_day_ago_str = one_day_ago.strftime("%d.%m.%Y")
        seven_days_ago_str = seven_days_ago.strftime("%d.%m.%Y")
        thirty_days_ago_str = thirty_days_ago.strftime("%d.%m.%Y")

        async with self.uow:
            today_statistics = await self.uow.statistics_of_views.get_one_by(date=today_str)
            one_day_ago_statistics = await self.uow.statistics_of_views.get_one_by(date=one_day_ago_str)
            seven_days_ago_statistics = await self.uow.statistics_of_views.get_one_by(date=seven_days_ago_str)
            thirty_days_ago_statistics = await self.uow.statistics_of_views.get_one_by(date=thirty_days_ago_str)

            # Получаем общее количество просмотров за каждый период
            total_views_today = today_statistics.views if today_statistics else 0
            total_views_one_day_ago = one_day_ago_statistics.views if one_day_ago_statistics else 0
            total_views_seven_days_ago = seven_days_ago_statistics.views if seven_days_ago_statistics else 0
            total_views_thirty_days_ago = thirty_days_ago_statistics.views if thirty_days_ago_statistics else 0

            # Вычисляем общее количество просмотров за каждый период
            total_views_1_day = total_views_today
            total_views_7_days = total_views_1_day + total_views_one_day_ago
            total_views_30_days = total_views_7_days + total_views_seven_days_ago

            # Рассчитываем проценты относительно общего количества просмотров за 30 дней
            percent_today = (total_views_1_day / total_views_30_days) * 100
            percent_7_days_ago = (total_views_7_days / total_views_30_days) * 100
            percent_30_days_ago = (total_views_30_days / total_views_30_days) * 100

        return {
            "1_day_percent": round(percent_today, 2),
            "7_days_percent": round(percent_7_days_ago, 2),
            "30_days_percent": round(percent_30_days_ago, 2),
        }




    async def get_statistics_by_period(self, start_date: str | None, end_date: str | None) -> list[models.StatisticOfViews]:
        async with self.uow:
            return await self.uow.statistics_of_views.get_by_period(start_date, end_date)          
        

statistics_of_views_service = StatisticsOfViewsService()