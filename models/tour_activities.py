from models import BaseTable, TourMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

    
class TourActivity(TourMixin, BaseTable):
    __tablename__ = 'tour_activities'
    
    activity_id: Mapped[int] = mapped_column(ForeignKey("activities.id"))

    