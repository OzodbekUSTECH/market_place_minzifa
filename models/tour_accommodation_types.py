from models import BaseTable, TourMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

    
class TourAccommodationType(TourMixin, BaseTable):
    __tablename__ = 'tour_accommodation_types'
    
    accommodation_type_id: Mapped[int] = mapped_column(ForeignKey("accommodation_types.id"))

    