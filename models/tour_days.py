from models import BaseTable, TourMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.hybrid import hybrid_property
from config import settings
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models import Region
    
class TourDay(TourMixin, BaseTable):
    __tablename__ = 'tour_days'
    
    day: Mapped[int]
    name: Mapped[dict] = mapped_column(JSONB)
    description: Mapped[dict] = mapped_column(JSONB)
    region_id: Mapped[int] = mapped_column(ForeignKey("regions.id"))

    region: Mapped["Region"] = relationship(lazy="subquery")
    media: Mapped[list["TourDayMediaGroup"]] = relationship(lazy="subquery", cascade="all, delete-orphan")


class TourDayMediaGroup(BaseTable):
    __tablename__ = "tour_day_media_groups"

    tour_day_id: Mapped[int] = mapped_column(ForeignKey("tour_days.id", ondelete="CASCADE"))
    filename: Mapped[str]

    @hybrid_property
    def photo_url(self):
        return f"{settings.TOUR_DAY_MEDIA_URL}{self.filename}"