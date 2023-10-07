from models import BaseTable, TourMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models import (
        Tour,
        User
    )
    
class SoldTour(TourMixin, BaseTable):
    __tablename__ = 'sold_tours'
    
    buyer_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    seller_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    price: Mapped[float]

    tour: Mapped["Tour"] = relationship(lazy="subquery")
    buyer: Mapped["User"] = relationship(lazy="subquery", foreign_keys=[buyer_id])
    seller: Mapped["User"] = relationship(lazy="subquery", foreign_keys=[seller_id])