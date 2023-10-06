from models import BaseTable, TourMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

    
class SoldTour(TourMixin, BaseTable):
    __tablename__ = 'sold_tours'
    
    buyer_id: Mapped[int] = ForeignKey("users.id")
    sellet_id: Mapped[int] = ForeignKey("users.id")

    price: Mapped[float]