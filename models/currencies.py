from models import BaseTable
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.dialects.postgresql import JSONB
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models import TourPrice

class Currency(BaseTable):
    __tablename__ = 'currencies'
    
    name: Mapped[str | None]
    symbol: Mapped[str]
    exchange_rate: Mapped[float | None]
    
    @hybrid_property
    def currency_id(self) -> int:
        return self.id

    @hybrid_property
    def price(self) -> int:
        return self.price_instance.price
    
    @hybrid_property
    def price_for_day(self) -> int:
        return self.price_instance.price_for_day
    
    @hybrid_property
    def discount_percentage(self) -> int | None:
        return round(self.price_instance.discount_percentage) if self.price_instance.discount_percentage else None

    @hybrid_property
    def new_price(self) -> int | None:
        return round(self.price_instance.new_price) if self.price_instance.new_price else None
    
    @hybrid_property
    def discount_start_date(self) -> str | None:
        return self.price_instance.discount_start_date
    
    @hybrid_property
    def discount_end_date(self) -> str | None:
        return self.price_instance.discount_end_date


    
    price_instance: Mapped["TourPrice"] = relationship(lazy="subquery")