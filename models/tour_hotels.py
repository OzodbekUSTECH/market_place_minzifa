from models import BaseTable, TourMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.hybrid import hybrid_property
from config import settings
from typing import TYPE_CHECKING
    
class TourHotel(TourMixin, BaseTable):
    __tablename__ = 'tour_hotels'
    
    name: Mapped[dict] = mapped_column(JSONB)
    # hotel_type_id: Mapped[int] = mapped_column(ForeignKey("tour_hotel_types.id"))
    description: Mapped[dict | None] = mapped_column(JSONB)
    stars: Mapped[int | None]

    
    media: Mapped[list["TourHotelMediaGroup"]] = relationship(lazy="subquery", cascade="all, delete-orphan")
    # hotel_type: Mapped["TourHotelType"] = relationship(lazy="subquery", single_parent=True, cascade="all, delete-orphan")

class TourHotelMediaGroup(BaseTable):
    __tablename__ = "tour_hotel_media_groups"

    tour_hotel_id: Mapped[int] = mapped_column(ForeignKey("tour_hotels.id", ondelete="CASCADE"))
    filename: Mapped[str]

    @hybrid_property
    def photo_url(self):
        return f"{settings.TOUR_HOTEL_MEDIA_URL}{self.filename}"
    


