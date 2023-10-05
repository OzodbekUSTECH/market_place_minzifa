from models import BaseTable, TourMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

    
class TourRegion(TourMixin, BaseTable):
    __tablename__ = 'tour_regions'
    
    region_id: Mapped[int] = mapped_column(ForeignKey("regions.id"))
    

    