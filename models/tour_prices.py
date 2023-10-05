from models import BaseTable, TourMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.hybrid import hybrid_property
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models import Tour
    
class TourPrice(TourMixin, BaseTable):
    __tablename__ = 'tour_prices'

    currency_id: Mapped[int] = mapped_column(ForeignKey("currencies.id"))
    price: Mapped[int]
    discount_percentage: Mapped[float | None]
    new_price: Mapped[float | None]
    discount_start_date: Mapped[str | None]
    discount_end_date: Mapped[str | None]

    @hybrid_property
    def price_for_day(self) -> int:
        return self.price // self.tour.duration
        
    tour: Mapped["Tour"] = relationship(
        lazy="immediate",
        overlaps="prices"  # Add this parameter
    )
 