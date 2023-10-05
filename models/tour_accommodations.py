from models import BaseTable, TourMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

    
class TourAccommodation(TourMixin, BaseTable):
    __tablename__ = 'tour_accommodations'
    
    accommodation_id: Mapped[int] = mapped_column(ForeignKey("accommodations.id"))

    