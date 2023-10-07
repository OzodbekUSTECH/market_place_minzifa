from models import BaseTable
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column


class StatisticOfViews(BaseTable):
    __tablename__ = 'statistics_of_views'
    
    date: Mapped[str]
    views: Mapped[int] = mapped_column(default=1, server_default="0")

    async def increase_view_counter(self) -> None:
        self.views += 1



    