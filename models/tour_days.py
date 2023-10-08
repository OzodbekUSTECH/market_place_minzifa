from models import BaseTable, TourMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB

    
class TourDay(TourMixin, BaseTable):
    __tablename__ = 'tour_days'
    
    day: Mapped[int]
    name: Mapped[dict] = mapped_column(JSONB)
    description: Mapped[dict] = mapped_column(JSONB)
    

    